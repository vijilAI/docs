<!-- .. Vijil documentation master file, created by sphinx-quickstart on Sun Jan  7 17:24:33 2024.
.. You can adapt this file completely to your liking, but it should at least
.. contain the root `toctree` directive. -->

# Vijil Documentation

Welcome to Vijil! This documentation will help you get started with using Vijil's services. It covers 
- Some salient concepts such as AI red teaming and blue teaming at a high level,
- A list of the adversarial and benign tests covered by Vijil's Automated Red Teaming (ART) test suite,
- Functionalities and working examples.

## Usage

Running Vijil services is simple. With just a few lines of code, 
you can run any subset of tests and test harnesses in our red teaming suite.

For example, you can use the following code to run all security-specific tests on Mistral-7B-Instruct
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
```console
$ vijil start evaluation \
    --model-hub octo \
    --model-name mistral-7b-instruct-fp16 \
    --dimension Security \
    --deployment-type public \
    --generations 10
```

````

Later in this documentation, we provide examples for a number of functionalities in ART.


```{eval-rst}
.. toctree::
   :maxdepth: 2

   getting-started
   concepts
   tests-library/index
```

<!-- ```{eval-rst}
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Library of Tests

   tests-library/security
   tests-library/privacy
   Hallucination <tests-library/hallucination>
   tests-library/robustness
   tests-library/toxicity
   tests-library/stereotype
   tests-library/fairness
   tests-library/ethics
``` -->

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

```{eval-rst}
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Integrations

   integrations/index
```

## About Vijil

Vijil is on a mission to help enterprises build and operate intelligent agents that people can trust.

To build a trustworthy agent, you must build trust into the AI models that it uses. For that, you must be able to inspect, modify, and control the models. This is easier to do when the models are open-source.

Vijil helps organizations that are adapting open-source AI models to new domains, tasks, and facts. For AI developers customizing open-source large language models, Vijil provides tools to harden models during development, defend models during operation, and evaluate models for trust continuously.

Vijil ART is currently available as a cloud service accessible through an API, CLI, and web user interface. Please contact us to get a private preview. 

<!-- ## Indices and tables

```{eval-rst}
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
``` -->
