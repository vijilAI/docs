# Evaluating RAGs through Vijil Evaluate

Retrieval Augmented Generation (RAG) is a popular framework for building generative AI applications, where the user can supply queries into a chat interface and get answers back related to a specific knowledge base typically composed od chunked documents.

There are two stages of generating an answer through a RAG: 
1. **Retrieval**: a vector search is performed in a knowledge base, and top-k document chunks are retrieved that are closest to the input query per distance in the embedding space.
2. **Generation**: Retrieved contexts and the original question are supplied to a Large Language Model (LLM), which generates the final answer for the end user.

Vijil Evaluate enables you to evaluate LLMs for RAG capabilities. Given a set of questions, the list of contexts each question would yield based on vector search from knowledge base, and the ground truth (or 'golden') answers to the questions, Vijil Evaluate uses a number of metrics to evaluate the quality of retrieved contexts, the quality of generated answers from the LLM component, as well as the likelihood that a generated answer is a hallucination.

Vijil Evaluate currently supports seven metrics to evaluate the generation stage in a RAG pipeline. In this notebook, we show you how to implement these metrics.

## Retrieval Metrics

To measure the quality of the retrieved contexts, we use two LLM-based metrics. Each produce a score between 0 and 1.

- **Contextual Precision**: measures whether the contexts relevant to the input question are ranked higher in the full set of retrieved contexts than irrelevant ones. A higher score indicates greater alignment in ranking.
- **Contextual Recall**: measures the extent to which the retrieved contexts align with the golden answers. A higher score indicates greater alignment with the golden answer.

Currently, we use `gpt-4o` as the judge LLM in these metrics.

## Generation Metrics

Our generation metrics are divided into three categories, attempting to measure the LLM in a RAG for different capabilities.

### Correctness

To measure correctness of the LLM-generated answers, we use the following traditional NLP metrics.

- BLEU
- METEOR
- BERTScore

Each of them compares the similarity of an LLM-generated answer with the ground truth 'golden' answer, and provides a score between 0 and 1. A higher score indicates greater similarity to the golden answer.

### Relevancy

Our LLM-based Answer Relevancy metric measures the degree to which the final generated output is relevant to the original input. It produces a score between 0 and 1, higher score indicating higher relevancy.


### Hallucination

We use an LLM-based Faithfulness metric to measure how much the generated response stays faithful to the retrieved contexts, i.e. the opposite of hallucination. This metric produces scores from 0 to 1, where a higher score means that the response is more faithful to the context (has fewer hallucinations).


## Evaluating Domain-specific Question Answering

In the example below, we use the [FinanceBench](https://huggingface.co/datasets/PatronusAI/financebench) benchmark dataset to evaluate how accurately  `gpt-4o-mini` can produce reliable answers from a dataset of financial documents.

Note that our Python client uses an API token, loaded as the environment variable `VIJIL_API_KEY`. Please make sure you have [fetched an API key](https://docs.vijil.ai/setup.html#authentication-using-api-keys) from the UI and stored it in the env file.

```python
# !pip install vijil
from dotenv import load_dotenv
load_dotenv("../.env")

# import and instantiate the client
from vijil import Vijil
client = Vijil()
```

FinanceBench already exists as an evaluation harness in Vijil Evaluate. Now we simply create an evaluation of the given LLM on this harness.

```python
evaluation = client.evaluations.create(
    model_hub="openai",
    model_name="gpt-4o-mini",
    model_params={"temperature": 0},
    harnesses=["financebench"],
)
print(evaluation)
# {'id': '726285f8-ec61-431b-9673-8ec722707031', 'status': 'CREATED'}
```
You can use the `get_status` method to keep track of the progress of the evaluation.

```python
client.evaluations.get_status(evaluation_id=evaluation["id"])
# {'id': '726285f8-ec61-431b-9673-8ec722707031',
#  'name': 'openai-gpt-4o-mini',
#  'tags': [''],
#  'status': 'IN_PROGRESS',
#  'total_test_count': 20,
#  'completed_test_count': 0,
#  'error_test_count': 0,
#  'total_response_count': 0,
#  'completed_response_count': 0,
#  'error_response_count': 0,
#  'total_generation_time': None,
#  'average_generation_time': None,
#  'score': None,
#  'hub': 'openai',
#  'model': 'gpt-4o-mini',
#  'url': '',
#  'created_at': 1728673801,
#  'created_by': 'f6e0b128-c075-4bc3-91da-34d03fa6c67e',
#  'completed_at': None,
#  'team_id': '00ccc042-1b41-4f02-ae5f-6a09b5e6e844',
#  'restart_count': 0,
#  'metadata': None,
#  'completion_tokens': 0,
#  'prompt_tokens': 0,
#  'total_tokens': 0}
```

After the status changes to `COMPLETE`, you can aggregate the values of all metrics.

To do so, we first download all inputs, outputs, and metric values.

```python
df = client.evaluations.describe(evaluation_id=evaluation["id"])
```

As an example, let's print out a question, its generated answer, and the metrics that were computed for it.

```python
import ast

print(f"QUESTION\n{ast.literal_eval(df.triggers[0][0])['question']}")
print(f"ANSWER\n{df.response[0]}")
print(f"METRICS\n{df.score[0]}")
# QUESTION
# By how much did Pepsico increase its unsecured five year revolving credit agreement on May 26, 2023?
# ANSWER
# PepsiCo increased its unsecured five year revolving credit agreement by $400,000,000 on May 26, 2023, going from $3,800,000,000 to $4,200,000,000.
# METRICS
# [{'autoredteam.detectors.nlp.BLEU': 0.0}, {'autoredteam.detectors.nlp.METEOR': 0.32258064516129037}, {'autoredteam.detectors.nlp.BERTScore': 0.5262122983517854}, {'autoredteam.detectors.llm.AnswerRelevancy': 1.0}, {'autoredteam.detectors.llm.ContextualPrecision': 1.0}, {'autoredteam.detectors.llm.ContextualRecall': 1.0}, {'autoredteam.detectors.llm.Faithfulness': 1.0}]
```

Let's now aggregate across all samples in the dataset and compute the average metrics.

```python
import pandas as pd

# extract metric names
metric_names = [list(met.keys())[0] for met in df.score[0]]

# flatten the metrics
metrics = {}
for met in metric_names:
    metrics[met] = []
for _, row in df.iterrows():
    for idx, met in enumerate(metric_names):
        metrics[met].append(row["score"][idx][met])
        
# cleanup and average
metrics = {met.split(".")[3]: metrics[met] for met in metric_names}
metrics_df = pd.DataFrame(metrics).mean()
metrics_df
# BLEU                   0.063651
# METEOR                 0.299480
# BERTScore              0.501233
# AnswerRelevancy        0.744167
# ContextualPrecision    0.975000
# ContextualRecall       0.766667
# Faithfulness           0.733975
# dtype: float64
```

While BLEU and METEOR scores are very low, there is a moderate amount (50%) of semantic overlap between the generated responses and golden answers, as per BERTScore. Per, `AnswerRelevancy`, the generated answers are moderately relevant to the input question. Contextual precision is high, since the benchmark dataset do not contain any contexts relevant to the golden answers. Contextual recall is around 77%, indicating that sometimes the generated answer may not include all information in the contexts. As per the Faithfulness metric, the generated responses may have some hallucinations.