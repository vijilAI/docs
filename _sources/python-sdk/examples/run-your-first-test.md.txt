# Run your First Test

This is an example of using the Vijil Python client. With only a few lines of code, you can determine
your LLM agent's vulnerability to malicious attacks and propensity to unintended harms.

## Loading the client

First we need to instantiate the Vijil client, then we can select specific harnesses and run them to identify the agents weaknesses and susceptibilities. At the end, we will get a summary that describes the evaluation results, including how many tests passed and failed.


```python
from vijil import Vijil
client = Vijil(api_key=YOUR_API_KEY)
```

## Add an API key

If you don't already have a model hub API key stored for the model/hub you want to use, add one now:

```python
client.api_keys.create(name="openAI20240630-2", model_hub="openai", api_key="sk+++")
```

## Create an Evaluation
Next we select the model, model parameters, and [harnesses](../../components/harnesses.md) we want to run. Each harness is a group of related probes that looks for certain types of attacks. Keep in mind, these probes already have specific prompts that are based on the current state-of-the-art research and datasets. Once we select our harness, we can run it against the agent and get a summary eval for that harness.

```python
client.evaluations.create(
    model_hub="openai",
    model_name="gpt-4o-mini",
    model_params={"temperature": 0},
    harnesses=["ethics"],
    harness_params={"is_lite": True}
)
# If successful, returns dictionary with the following format:
# {'id': 'df4584a5-e215-40d3-b758-d9bf63c37d99', 'status': 'CREATED'}
```

## View evaluation status

Take note of the `id` returned when you create an evaluation. Using that id, you can view the status of an evaluation:

```python
client.evaluations.get_status(evaluation_id="df4584a5-e215-40d3-b758-d9bf63c37d99")
```

## View score report

You also can view summary scores of an evaluation:

```python
client.evaluations.summarize(evaluation_id="df4584a5-e215-40d3-b758-d9bf63c37d99")
```

## View granular prompt-level logs

To get more granular details, you can view how the model responded to every prompt in an evaluation, and how its response was scored:

```python
client.evaluations.describe(evaluation_id="65e263b5-95b1-4685-a382-38b0e43b1c24")
```

## List all evaluations

You can also see a list of evaluations you've created:

```python
client.evaluations.list()
```