# Evaluating RAGs through Vijil Evaluate

Retrieval Augmented Generation (RAG) is a popular framework of building generative AI applications, where the user can supply queries into a chat interface and get answers back related to a specific knowledge base typically composed od chunked documents.

There are two stages of generating an answer through a RAG: 
1. **Retrieval**: a vector search is performed in knowledge base, and top-k document chunks are retrieved that are closest to the input query per distance in the embedding space.
2. **Generation**: Retrieved contexts and the original question are supplied to a Large Language Model (LLM), which generates the final answer for the end user.

Vijil Evaluate enables you to evaluate LLMs for RAG capabilities. Given a set of questions, the list of contexts each question would yield based on vector search from knowledge base, and the ground truth (or 'golden') answers to the questions, Vijil Evaluate uses a number of metrics to evaluate the quality of generated answers from the LLM component, as well as the likelihood that a generated answer is a hallucination.

Vijil Evaluate currently supports four metrics to evaluate the generation stage in a RAG pipeline. In this notebook, we show you how to implement these metrics.

## Correctness Metrics

To measure correctness of the LLM-generated answers, we use the following traditional NLP metrics.

- BLEU
- METEOR
- BERTScore

Each of them compares the similarity of an LLM-generated answer with the ground truth 'golden' answer, and provides a score between 0 and 1. A higher score indicates greater similarity to the golden answer.


## Hallucination Metrics

We use the [HHEM](https://huggingface.co/vectara/hallucination_evaluation_model) Hallucination Evaluation classifier to measure the propensity that the generated response is hallucinated. To do so, we supply the generated response and concatenated contexts to the model, and take the output probability that the two input strings are consistent with each other as the final score. HHEM produces scores from 0 to 1, where a higher score means that the response is more faithful to the context (has fewer hallucinations).

## Evaluating Domain-specific Question Answering

In the example below, we use the [financebench](https://huggingface.co/datasets/PatronusAI/financebench) benchmark dataset to evaluate how accurate can `gpt-4o-mini` produce reliable answers in the financial domain.

We have already loaded the benchmark as an evaluation harness in Vijil Evaluate. Now we simply create an evaluation of the given LLM on this harness.