<!-- .. Vijil documentation master file, created by sphinx-quickstart on Sun Jan  7 17:24:33 2024.
.. You can adapt this file completely to your liking, but it should at least
.. contain the root `toctree` directive. -->

# Vijil Documentation

Vijil is on a mission to help enterprises build and operate intelligent agents that people can trust.

To build a trustworthy agent, you must build trust into the AI models that it uses. For that, you must be able to inspect, modify, and control the models. This is easier to do when the models are open-source.

Vijil helps organizations that are adapting open-source and API-only AI models to new domains, tasks, and facts. For AI developers customizing open-source large language models, Vijil provides red-team and blue-team cloud services to harden models during development, defend models during operation, and evaluate models for reliability, security, and safety continuously.

**Vijil Evaluate** is Vijil's flagship evaluation service that enables AI developers evaluate the trustworthiness of an LLM, generative AI application, or agent. Using the Evaluate API, developers can test an AI system under benign and hostile conditions in minutes along 9 dimensions of trust. Evaluations are based on a combination of Vijil-provided test harnesses informed by latest research, and dynamically generated adeversarial tests based on user-provided seed prompts.

**Vijil Dome** is the guardrailing service by Vijil that provides a defensive layer around an agent against malicious or harmful inputs and prevents it from providing outputs that suffer from these issues. While we retain the core elements of current firewall approaches---a combination of string matching, ML and NLP classifiers, and embedding/LLM-based approaches, we put a premium on configurability, latency, and reusability.


## Contents

```{eval-rst}
.. toctree::
   :maxdepth: 2

   setup
   quickstart
```

```{eval-rst}
.. toctree::
   :maxdepth: 1
   :caption: Evaluating Agents

   concepts
   tests-library/index
   components/index
   python-sdk/examples/index
   integrations/index
   glossary/index
   api
```

```{eval-rst}
.. toctree::
   :maxdepth: 1
   :caption: Protecting Agents

   dome/intro
   dome/gettingstarted
   dome/overview
   dome/config
   dome/guards/index
   dome/tutorials/index
   dome/integrations
```

<!-- ## About Vijil


Vijil ART is currently available as a cloud service accessible through an API, CLI, and web user interface. Please contact us to get a private preview.  -->

<!-- ## Indices and tables

```{eval-rst}
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
``` -->
