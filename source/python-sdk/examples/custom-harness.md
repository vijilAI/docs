# Create a custom harness

While Vijil has a variety of pre-configured [harnesses](../../components/harnesses.md) that you can select from, you can also create your own harnesses in order to obtain a trust score specific to your organization.

The following example assumes that you have already initialized a Vijil [client](run-your-first-test.md) named `client`.

<!-- ## Create harness

Use the `harnesses.create` function in the Python [client](agents.md) to specify the list of probes you want to include in the harness:

```python
client.harnesses.create(name="my custom harness", probes=["probe1", "probe2"])
# If successful, returns dictionary with the following format:
# {'name': "my custom harness", 'status': 'CREATED'}
```
 -->
## Create harness from file(s)

You can create a custom policy adherence harness that checks whether your model adheres to its system prompt or an organizational policy. To do this, you need a system prompt specified as a string, and an optional organizational policy provided as a `.txt` or `.pdf` file. If you don't provide a policy file, we will create a harness based only the provided system prompt.

Use the `harnesses.create` function to create your harness:

```python
harness_creation_job = client.harnesses.create(harness_name=your_harness_name, system_prompt=your_system_prompt, policy_file_path=your_policy_file_path)
```

Once the harness is created, you can [run an evaluation](evaluations.md#create-an-evaluation) with it:

```python
client.evaluations.create(
    harnesses=[harness_creation_job['harness_config_id']],
    model_hub=your_model_hub,
    model_name=your_model,
    harness_version="1.0.0" #if this is the first version of the harness.
)
```

The `harness_version` starts at 1.0.0 for any harness of the given `harness_name`. If you create another harness with the same name, vijil automatically increments the harness version, e.g. from 1.0.0 to 1.0.1. In the above example, we assume that `your_harness_name` is a new harness name, so we set the version to 1.0.0.