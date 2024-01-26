<!-- .. Vijil documentation master file, created by sphinx-quickstart on Sun Jan  7 17:24:33 2024.
.. You can adapt this file completely to your liking, but it should at least
.. contain the root `toctree` directive. -->

# Vijil Documentation

Welcome to Vijil! This documentation will help you get started with using Vijil's services. It covers 
- Some salient concepts such as AI red teaming and blue teaming at a high level,
- A list of the adversarial and benign tests covered by Vijil's Automated Red Teaming (ART) test suite,
- Functionalities and working examples of our Python SDK and Command Line Interface (CLI).

## Usage

Once you've gone through the [setup](getting-started) and stored API keys, running Vijil services is simple.
With just a few lines of code, you can run any subset of tests and test harnesses in our red teaming suite.

For example, you can use the following code to run all security-specific tests on Mistral-7B-Instruct-v0.1
available through [OctoAI](https://octoai.cloud/).


````{tab} Python 
```python
from autoredteam.agents.octo import OctoAPI
from autoredteam.harnesses.dimension import SecurityHarness

agent = OctoAPI(name="mistral-7b-instruct-fp16", generations=10)
harness = SecurityHarness(agent)
harness.run()
```

````

````{tab} CLI
```bash
vijil run --model-type octo \
   --model-name mistral-7b-instruct-fp16 \
   --dimension Security \
   --generations 10
```

````

Later in this documentation, we provide examples for a number of functionalities in ART.


```{eval-rst}
.. toctree::
   :hidden:

   getting-started
   concepts
```

```{eval-rst}
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Library of Tests

   tests-library/security
   tests-library/toxicity
   Hallucination <tests-library/hallucination>
   tests-library/ethics
   tests-library/privacy
   tests-library/stereotype
   tests-library/fairness
```

```{eval-rst}
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Python SDK

   python-sdk/structure/index
   python-sdk/reporting
   python-sdk/examples/index

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

<!-- ## Indices and tables

```{eval-rst}
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
``` -->
