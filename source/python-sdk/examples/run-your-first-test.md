# Run your First Test

This is an example of using the Vijil Python client. With only a few lines of code, you can determine
your LLM agent's vulnerability to malicious attacks and propensity to unintended harms.

<!-- ## Installation
 -->
<!-- Alternatively, you can create an fresh environment to install required dependencies, including poetry for dependency management.

```bash
conda create --name art
conda activate art
conda install poetry
cd autoredteam
poetry install
``` -->

## Setup

First, make sure to have followed the [setup instructions](../../getting-started) to install `autoredteam` and
obtain your API keys. As a deminder, we support the following model vendors:

* [Anyscale](https://docs.endpoints.anyscale.com/guides/authenticate)
* [Hugging Face](https://huggingface.co/docs/hub/security-tokens)
* [Mistral](https://docs.mistral.ai/)
* [OctoAI](https://docs.octoai.cloud/reference/authentication-for-requests)
* [OpenAI](https://platform.openai.com/docs/introduction)
* [Replicate](https://replicate.com/docs/reference/http#authentication)
* [Together](https://docs.together.ai/docs/inference-rest)

There are three ways you can use these keys.

1. You can store them in a `.env` locally and load that file here using [`python-dotenv`](https://pypi.org/project/python-dotenv/).
2. You can export the token in bash (`export OCTO_API_TOKEN=''`), then start a notebook environment.
3. Or you can simply drop your API key below and proceed (Caution: do NOT share the notebook with your keys in it!)

```python
import os
os.environ['OCTO_API_TOKEN'] = 'your-octo-token'
```

## Loading the client

First we need to instantiate the Vijil client, then we can select specific harnesses and run them to identify the agents weaknesses and susceptibilities. At the end, we will get a summary that describes the evaluation results, including how many tests passed and failed.


```python
from vijil import Vijil
client = Vijil(api_key=YOUR_API_KEY)
```

## Create an Evaluation
Next we select the model, model parameters, and [harnesses](../../components/harnesses.md) we want to run. Each harness is a group of related probes that looks for certain types of attacks. Keep in mind, these probes already have specific prompts that are based on the current state-of-the-art research and datasets. Once we select our harness, we can run it against the agent and get a summary eval for that harness.

```python
client.score.evaluations.create(
    model_hub="openai",
    model_name="gpt-3.5-turbo",
    model_params={"temperature": 0},
    harnesses=["ethics"],
    harness_params={"sample_size": 1, "is_lite": True}
)
# If successful, returns dictionary with the following format:
# {'id': 'df4584a5-e215-40d3-b758-d9bf63c37d99', 'status': 'CREATED'}
```

## View evaluation status

Take note of the `id` returned when you create an evaluation. Using that id, you can view the status of an evaluation:

```python
client.score.evaluations.get_status(evaluation_id="df4584a5-e215-40d3-b758-d9bf63c37d99")
```

## View score report

You also can view summary scores of an evaluation:

```python
client.score.evaluations.summarize(evaluation_id="df4584a5-e215-40d3-b758-d9bf63c37d99")
```

## View granular prompt-level logs

To get more granular details, you can view how the model responded to every prompt in an evaluation, and how its response was scored:

```python
client.score.evaluations.describe(evaluation_id="65e263b5-95b1-4685-a382-38b0e43b1c24")
```

## List all evaluations

You can also see a list of evaluations you've created:

```python
client.score.evaluations.list()
```