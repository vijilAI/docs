# Custom Endpoints

If your agent is accessible using an OpenAI-style chat completion API that takes in a base URL and a model name, we can help you evaluate it.

To do so, first store the API key by going to **Keys > Add new key** in the Evaluate platform. From the Model Hub dropdown, select *Custom* as your chosen hub, and add your API key.

You can also [add an API key](../python-sdk/examples/api-keys.md#add-an-api-key) using the python client.

## Run an Evaluation

To run an evaluation from the UI, simply select *Custom* as the Model Hub, then paste your custom endpoint as the *Model URL*.

To [run an evaluation using the Python client](../python-sdk/examples/evaluations.md), use the following code pattern, with your custom endpoint as `model_url`, model name as `model_name`, and a harness of your choice.

````{tab} Python
```python
client.evaluations.create(
    api_key_name="your_key_name",
    model_hub="custom",
    model_url="https://your_model_url",
    model_name="your_model_name",
    model_params={"temperature": 0},
    harnesses=["hallucination"],
)
```
````
````{note}
You may need to store multiple API keys that are tied to different custom agent endpoints. Given that, we have made `api_key_name` an additional mandatory parameter to be supplied for evaluating custom endpoints.
````

