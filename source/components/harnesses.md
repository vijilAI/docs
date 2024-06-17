# Harnesses

Harnesses allow you to run relevant groups of tests all together. You can use pre-configured Vijil harnesses or configure your own custom harnesses.

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

Besides the dimensions listed above, you can also specify other harnesses in the Python client. Here we summarize which probes each of these other harnesses contains.

### Ethical theories

This harness includes both vanilla and jailbreaking probes for prompts that test the model's understanding of ethical theories.

| Harness name     | Harness name for Python client | Probe name                       | Probe module                                          |
| ---------------- | ------------------------------ | -------------------------------- | ----------------------------------------------------- |
| Ethical theories | normative_ethics               | Deontological Ethics             | vijil.probes.normative_ethics.Deontology              |
|                  |                                | Adversarial Deontological Ethics | vijil.probes.normative_ethics.DeontologyJailbreak     |
|                  |                                | Justice-based Ethics             | vijil.probes.normative_ethics.Justice                 |
|                  |                                | Adversarial Justice-based Ethics | vijil.probes.normative_ethics.JusticeJailbreak        |
|                  |                                | Commonsense Morality             | vijil.probes.normative_ethics.Morality                |
|                  |                                | Adversarial Commonsense Morality | vijil.probes.normative_ethics.MoralityJailbreak       |
|                  |                                | Utilitarianism                   | vijil.probes.normative_ethics.Utilitarianism          |
|                  |                                | Adversarial Utilitarianism       | vijil.probes.normative_ethics.UtilitarianismJailbreak |
|                  |                                | Virtue Ethics                    | vijil.probes.normative_ethics.Virtue                  |
|                  |                                | Adversarial Virtue Ethics        | vijil.probes.normative_ethics.VirtueJailbreak         |

### Ethics: simulation

This harness contains vanilla and jailbreaking prompts that ask about the moral valence of a simulated scenario.


| Harness name       | Harness name for Python client | Probe name             | Probe module                               |
| ------------------ | ------------------------------ | ---------------------- | ------------------------------------------ |
| Ethics: simulation | jiminycricket                  | Simulation             | vijil.probes.jiminycricket.Jiminy          |
|                    |                                | Adversarial Simulation | vijil.probes.jiminycricket.JiminyJailbreak |