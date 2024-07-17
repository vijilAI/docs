# Harnesses

While Vijil has a variety of pre-configured [harnesses](../../components/harnesses.md) that you can select from, you can also create your own harnesses in order to obtain a trust score from your preferred collection of [probes](../../components/tests.md).

The following examples assume that you have already initialized a Vijil [client](agents.md).

## Create harness

Use the `harnesses.create` function in the Python [client](agents.md) to specify the list of probes you want to include in the harness:

```python
client.harnesses.create(name="my custom harness", probes=["probe1", "probe2"])
# If successful, returns dictionary with the following format:
# {'name': "my custom harness", 'status': 'CREATED'}
```

## View harnesses

You can view all available harnesses (include [pre-configured](../../components/harnesses.md) ones) with ``harnesses.list``:

```python
client.harnesses.list()
# Returns list of dictionaries:
# [
#   {'name': 'custom1','probes': ['probe1', 'probe2', probe3']},
#   {'name': 'custom2', 'probes': ['probe4', 'probe5']},
#   {'name': 'fairness', 'probes': ['vijil.probes.adultdata.CounterfactualGender', 'vijil.probes.winobias.ProfessionalBias']}, 
# ...
# ]
```

## Delete harness

```python
client.harnesses.delete(name="my custom harness")
# If successful, returns dictionary with the following format:
# {'name': "my custom harness", 'status': 'DELETED'}
```