# Harnesses

Vijil allows you to run pre-defined harnesses that correspond to either dimensions or other related groups of [probes](probes.md).

## Pre-defined harnesses

Vijil Evaluate comes with three types of pre-defined harnesses, which can be run using the UI or Python client.

### Dimension
Every [dimension](../tests-library/index.md) is a pre-configured harness.  In addition, each [scenario](scenarios.md) is also a harness. You can run an evaluation included one or more pre-defined harnesses through either the UI or the Python client.
- [Security](../tests-library/security.md)
- [Privacy](../tests-library/privacy.md)
- [Hallucination](../tests-library/hallucination.md)
- [Robustness](../tests-library/robustness.md)
- [Toxicity](../tests-library/toxicity.md)
- [Stereotype](../tests-library/stereotype.md)
- [Fairness](../tests-library/fairness.md)
- [Ethics](../tests-library/ethics.md)
    
To run all of Vijil's probes (covering all dimensions)---plus the Performance harness covering benchmarks from the [OpenLLM Leaderboard 2](https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-2-660cdb7601eba6852431fffc), use the `trust_score` harness.


### Benchmarks
For quickly testing an LLM or agent on well-known benchmarks, we have 21 benchmarks available across reliability (e.g. [OpenLLM](https://huggingface.co/open-llm-leaderboard), [OpenLLM v2](https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-2-660cdb7601eba6852431fffc)), security (e.g. [garak](https://garak.ai/), [CyberSecEval 3](https://ai.meta.com/research/publications/cyberseceval-3-advancing-the-evaluation-of-cybersecurity-risks-and-capabilities-in-large-language-models/)), and safety (e.g. [StrongReject](https://arxiv.org/abs/2402.10260), [JailbreakBench](https://arxiv.org/abs/2404.01318)) in Vijil Evaluate.

### Audits
We support harnesses to test for regulations and standards relevant from an enterprise risk perspective, such as the OWASP LLM Top 10 and GDPR. Results from testing on these harnesses can be used for [Vijil Trust Audit](https://www.vijil.ai/trust-audit).

### Custom Harness

Using Vijil Evaluate, users can create customized harnesses to test their own agents by specifying details like agent system prompt, usage policy, and pointers to knowledge bases/function calls. Check out [this link](../python-sdk/examples/custom-harness.md) to learn more about custom harnesses.

## Working with harnesses in Python client

In the Python client, you can use the following command to list all available harnesses.

```python
client.harnesses.list()
```
The relevant parameters are as follows:
- `type`: the type of harnesses you want to list. Can be unspecified (default), or one of `dimension`, `benchmark`, `audit`, `custom`.
- `format`: the format of output for the list of harnesses. Can be `dataframe` (default) or `list`.

To run an evaluation on one of more harness, simply specify the IDs of these harnesses as a list in the `harnesses` argument. Following the an example.

```python
client.evaluations.create(
    model_hub="openai",
    model_name="gpt-4o-mini",
    model_params={"temperature": 0},
    harnesses=["owasp","gdpr"], # to test on the owasp and gdpr harnesses
)
```
