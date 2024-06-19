# Harnesses

Harnesses allow you to run relevant groups of probes all together. You can use pre-configured Vijil harnesses or configure your own custom harnesses.

Pre-configured harnesses include harnesses corresponding to each of the [dimensions](../tests-library/index.md), and other harnesses that are subsets of those dimensions.

## Dimension harnesses

- `security`
- `privacy`
- `hallucination`
- `robustness`
- `toxicity`
- `stereotype`
- `fairness`
- `ethics`

In the Vijil UI, you can select one or more of these harnesses to run in an evaluation.

## Run all probes

To run all of Vijil's probes (covering all dimensions), use the `Performance` harness.

###  Specify  harnesses in Python client

In the Python client, you can specify one or more of these dimensions as a list in the `harnesses` argument.

Example usage is as follows. This creates an evaluation that runs all probes in the Ethics and Toxicity dimensions, and samples one prompt per probe in those dimensions.

```python
client.score.evaluations.create(
    model_hub="openai",
    model_name="gpt-3.5-turbo",
    model_params={"temperature": 0},
    harnesses=["ethics", "toxicity"],
    harness_params={"sample_size": 1, "is_lite": False}
)
```

## Other pre-configured harnesses

Besides the dimensions listed above, Vijil also has harnesses corresponding to each scenario. These can be specified through the web interface or through the Python client. 