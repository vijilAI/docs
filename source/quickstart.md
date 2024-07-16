# Quickstart Tutorial

### Running Evaluations

Once the Python package is installed, you can instantiate a client class and kick off an evaluation job.
For example, the following command evaluates GPT-3.5-Turbo for toxicity while setting temperature at 0.

````{tab} Python
```python
from vijil import Vijil

client = Vijil()
client.evaluations.create(
    model_hub="openai",
    model_name="gpt-3.5-turbo",
    model_params={"temperature": 0},
    harnesses=["toxicity"]
)
```
````

**Parameters**

- **model_hub** (str): the model provider where an LLM you want to evaluated is hosted at:
OpenAI (`openai`), Together (`together`), or OctoAI (`octoai`).

- **model_name** (str):  

## Setting up Guardrails

You can use toml-based config files or inbuilt presets to configure guardrails for an LLM, AI application, or agent.
After loading up 