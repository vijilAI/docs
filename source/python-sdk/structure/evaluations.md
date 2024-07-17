# Working with Evaluations

You can create, view, and summarize evaluation with the Vijil Python client.

Before doing any of this, you'll need to [instantiate](agents.md) your Vijil client.

## Create an evaluation

Assuming you've instantiated a Vijil client called `client`, you can use the `score.evaluations.create` method to create an evaluation:


```python
client.evaluations.create(
    model_hub="openai",
    model_name="gpt-3.5-turbo",
    model_params={"temperature": 0},
    harnesses=["ethics"],
    harness_params={"sample_size": 1, "is_lite": True}
)
# If successful, returns dictionary with the following format:
# {'id': YOUR_GUID, 'status': 'CREATED'}
```

The relevant parameters are as follows:

- `model_hub`: The model hub your model is on. Currently we support `openai`, `octo`, and `together` as model hubs.
- `model_name`: The name of the model you want to use on the hub. You can get this from the relevant hub's documentation.
- `model_params`: Inference parameters like temperature and top_p.
- `harnesses`: [Harnesses](../../components/harnesses.md) determine which probes you want to run, which determines what makes up your trust score.
- `harness_params`: `sample_size` determines how many prompts you're sampling from each probe. To sample all prompts, omit this argument. `is_lite` determines whether you're running a "light" version of the harness, which will be cheaper. Set this to `False` if you want to run the full harness.


## View, describe, and summarize evaluations

See our [example](../examples/run-your-first-test.md) for how to do these.