# Run your First Test

<!-- <a target="_blank" href="https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/model_monitoring/model_monitoring.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a> -->

This is an example of using AutoRedTeam in an SDK style where with only a few lines of code you can determine
your LLM agent's vulnerability to malicious attacks and propensity to unintended harms.

## Installation

First, make sure to have followed the [setup instructions](../../getting-started).
Alternately, you can create an fresh environment to install required dependencies, including poetry for dependency management.

```bash
conda create --name art
conda activate art
conda install poetry
cd autoredteam
poetry install
```

After the above steps, we should be good to go!

## Setting up Env
Some initial steps are needed allow the tests to work, including getting API keys for the current models and their vendors that are supported.
Currently, we support the following model vendors:

* [Anyscale](https://docs.endpoints.anyscale.com/guides/authenticate)
* [Hugging Face](https://huggingface.co/docs/hub/security-tokens)
* [OctoAI](https://docs.octoai.cloud/reference/authentication-for-requests)
* [OpenAI](https://platform.openai.com/docs/introduction)
* [Replicate](https://replicate.com/docs/reference/http#authentication)

You must also store these keys in a `.env` file in the local directory relative to ART so it can be accessed. 

```{eval-rst}
.. caution::
    We highly encourage that you add the `.env` to `.gitignore` and use best practices to keep your personal keys private.
```

An example of what's expected in the `.env` is the following:

```text
OCTO_API_TOKEN = "insert your token"
```

Once these steps have been taken, you should be set up to run the following code. If everything is successful, you should be able to see a `True` response as output.

```python
import sys
from dotenv import load_dotenv
load_dotenv("/path/to/.env")
# True
```

## Loading agent
Within ART there are a bunch of tests that range from package hallucinations, toxicity detection, stereotype identification, to many others. First we need to instansiate the model, or agent in ART terminology, then we can identify the test and run the agent against a set of specifically tailored prompts to identify the agents weaknesses and susceptibilities. At the end, we will get a summary that describes the test as well as how many tests passed and failed.

Let's assume we want to test Mistral-7B-Instruct-v0.1 hosted by OctoAI. To do this, we instantiate a wrapper class for the Octo inference API.

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

