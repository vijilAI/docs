<!-- .. Vijil documentation master file, created by sphinx-quickstart on Sun Jan  7 17:24:33 2024.
.. You can adapt this file completely to your liking, but it should at least
.. contain the root `toctree` directive. -->

# Vijil Documentation

Welcome to Vijil! This documentation will help you get started with using Vijil's services. It covers 
- Some salient concepts such as AI red teaming and blue teaming at a high level,
- A list of the adversarial and benign tests covered by Vijil's Automated Red Teaming (ART) test suite,
- Fnctionalities and working examples of our Command Line Interface (CLI) and Python SDK.

## Features

- blah
- blah2
- blah3


```{eval-rst}
.. toctree::
   :hidden:

   getting-started
```

```{eval-rst}
.. toctree::
   :hidden:
   :caption: Concepts

   concepts/agents
   concepts/red-teaming
   concepts/blue-teaming
```

```{eval-rst}
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Library of Tests
   :glob:

   tests-library/security/*
   tests-library/toxicity/*
```

```{eval-rst}
.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Perturbations

   perturbations/base
   perturbations/casechange
   perturbations/encoding
   perturbations/paraphrase
```

```{eval-rst}
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Python SDK

   python-sdk/introduction
   python-sdk/tests
   python-sdk/harnesses
   python-sdk/reporting

```

```{eval-rst}
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: CLI

   cli/commands
```

## About Vijil

Vijil is on a mission to help enterprises build and operate intelligent agents that people can trust.

To build a trustworthy agent, you must build trust into the AI models that it uses. For that, you must be able to inspect, modify, and control the models. This is easier to do when the models are open-source.

Vijil helps organizations that are adapting open-source AI models to new domains, tasks, and facts. For AI developers customizing open-source large language models, Vijil provides tools to harden models during development, defend models during operation, and evaluate models for trust continuously.

## Indices and tables

```{eval-rst}
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```
