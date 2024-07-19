# Quickstart Tutorial

## Running Evaluations

Once the Python client installed, you can instantiate a client class and kick off an evaluation job.
For example, the following command kicks off a full trust evaluation job on GPT-3.5-Turbo, setting temperature at 0.

````{tab} Python
```python
from vijil import Vijil

client = Vijil()
client.evaluations.create(
    model_hub="openai",
    model_name="gpt-3.5-turbo",
    model_params={"temperature": 0},
    harnesses=["trust_score"]
)
```
````

To keep tab on the progress of the job, you can use the `get_status` command or utilize the UI. After the evaluation finishes,
use the command again to retrieve the Trust Score for the LLM you tested.

````{tab} Python
```python
client.evaluations.get_status()
# {'id': 'a595100d-b06b-426d-a857-6915b00e0ea7',
#  'status': 'COMPLETED',
#  'total_test_count': 111979,
#  'completed_test_count': 111979,
#  'error_test_count': 0,
#  'total_response_count': 111979,
#  'completed_response_count': 111979,
#  'error_response_count': 0,
#  'total_generation_time': '1672.000000',
#  'average_generation_time': '1.3183721947865225',
#  'score': 0.7017487392615686,
#  'model': 'gpt-3.5-turbo',
#  'created_at': 1721018860,
#  'created_by': '48d03cb8-0fbb-4b32-8b52-bfa9229896b7',
#  'completed_at': 1721020964}
```
````

<!-- **Parameters**

- **model_hub** (str): the model provider where an LLM you want to evaluated is hosted at:
OpenAI (`openai`), Together (`together`), or OctoAI (`octoai`).

- **model_name** (str):   -->

Under the argument `harnesses`, you can also supply a list of trust dimensions or evaluation scenarios.
We look into them in [later examples](python-sdk/examples/evaluations.md).

## Setting up Guardrails

You can put together components of the Vijil Dome library into input and output guard configurations for an LLM, AI application, or agent.
Configurations can either be defined inside code as a dictionary, or saved and loaded from disk.

A minimal code example to set up input and output guards is given below, where a Dome client is initialized and implemented using default configuration.

````{tab} Python
```python
from vijil_dome import Dome

default_config = Dome.get_default_config()
dome = Dome.Dome(default_config.default_guardrail_config)

input_guard = dome.input_guard()
output_guard = dome.output_guard()
```
````

Following this, `input_guard.scan` or `output_guard.scan` can be called to use the respective guardrails on an input prompt or output response, respectively. Later on in the documentation, we [present](dome/examples.md) detailed usage examples.