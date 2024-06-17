# Harnesses, probes, and detectors

Vijil's evaluation service consists of harnesses, probes, and detectors.

At the lowest level, [detectors](detectors.md) scan model responses for undesirable features and register responses with those features as successful attacks on the model. For example, a detector may be designed to look for fake Python packages.

At the next level, each [probe](tests.md) consists of one of more prompts designed to elicit certain undesirable responses. For example, a probe could contain prompts to look for malware.

At the topmost level, [harnesses](harnesses.md) are collections of probes that you run to generate an overall trust score/report from. Each of the [dimensions of trustworthiness](../tests-library/index.md) is a harness. In addition, Vijil has other pre-configured harnesses that consist of related groups of probes.


```{eval-rst}
.. toctree::
   :maxdepth: 1

   harnesses
   tests
   detectors

```