# Harnesses

Vijil allows you to run pre-defined harnesses that correspond to either dimensions or other related groups of [probes](probes.md).

## Pre-defined harnesses

Every [dimension](../tests-library/index.md) is a pre-configured harness.  In addition, each [scenario](scenarios.md) is also a harness. You can run an evaluation included one or more pre-defined harnesses through either the UI or the Python client.

### Dimension harnesses

- [Security](../tests-library/security.md)
- [Privacy](../tests-library/privacy.md)
- [Hallucination](../tests-library/hallucination.md)
- [Robustness](../tests-library/robustness.md)
- [Toxicity](../tests-library/toxicity.md)
- [Stereotype](../tests-library/stereotype.md)
- [Fairness](../tests-library/fairness.md)
- [Ethics](../tests-library/ethics.md)

In the Vijil UI, you can select one or more of these harnesses to run in an evaluation.

### Performance harness

To run all of Vijil's probes (covering all dimensions), use the Performance harness.

### Other pre-defined harnesses

Every [scenario](scenarios.md) can also be run as a harness.

### Specify  harnesses in Python client

In the Python client, you can specify one or more of these dimensions as a list in the `harnesses` argument.

Example usage is as follows. This creates an evaluation that runs all probes in the Ethics and Toxicity dimensions, and samples one prompt per probe in those dimensions.

```python
client.evaluations.create(
    model_hub="openai",
    model_name="gpt-4o-mini",
    model_params={"temperature": 0},
    harnesses=["ethics", "toxicity"],
    harness_params={"sample_size": 1, "is_lite": False}
)
```
