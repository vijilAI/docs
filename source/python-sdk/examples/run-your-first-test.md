# Run your First Test

<a target="_blank" href="https://colab.research.google.com/github/vijilAI/docs/blob/main/notebooks/run-your-first-test.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

This is an example of using ART in an SDK style where with only a few lines of code you can determine
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

## Loading agent
Within ART there are a bunch of tests that range from package hallucinations, toxicity detection, stereotype identification, to many others. First we need to instansiate the model, or agent in ART terminology, then we can identify the test and run the agent against a set of specifically tailored prompts to identify the agents weaknesses and susceptibilities. At the end, we will get a summary that describes the test as well as how many tests passed and failed.

Let's assume we want to test Mistral-7B-Instruct hosted by OctoAI. To do this, we instantiate a wrapper class for the Octo inference API.

```python
from autoredteam.agents.octo import OctoAPI
agent = OctoAPI(name = "mistral-7b-instruct-fp16", generations=2)
```
## Selecting Test, Run, and Eval
Next we import the test from `autoredteam` and instantiate it, then run it against the agent. Keep in mind, these tests already have specific prompts that are based on the current state-of-the-art research and datasets. Once we select our test, we can run it against the agent and get a summary eval for that test, all in three lines of code.

```python
from autoredteam.tests.goodside import WhoIsRiley
test_instance = WhoIsRiley()
test_instance.run(agent)
# goodside.WhoIsRiley                   goodside.RileyIsnt:    9/  12 (  75.0%) passed
```

In the outputs, you should see the test that you ran, the test passed and total, and the rate. Congrats, you ran your first test with ART!

