# Harnesses, probes, and detectors

Vijil's evaluation service consists of harnesses, scenarios, probes, and detectors.

```{image} ../_static/Harness-scenario-probe-detector.png
:alt: Vijil score structure
:class: bg-primary
:width: 800px
:align: center
```

At the lowest level, [detectors](detectors.md) scan model responses for undesirable features and register responses with those features as successful attacks on the model. For example, a detector may be designed to look for fake Python packages.

At the next level, each [probe](tests.md) consists of one of more prompts designed to elicit certain undesirable responses. For example, a probe could contain prompts to look for malware.

The next highest level consists of [scenarios](scenarios.md), which are collections of probes that have similar goals. 

At the topmost level, [harnesses](harnesses.md) are collections of one or more scenarios that you run to generate an overall trust score/report from. To run a Vijil evaluation, you have to select one of more harnesses to include. Each of the [dimensions of trustworthiness](../tests-library/index.md) is a harness. In addition, each scenario is also a harness.


```{eval-rst}
.. toctree::
   :maxdepth: 1

   harnesses
   scenarios
   tests
   detectors

```