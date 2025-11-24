# List of Detection Methods

Vijil Dome has a number of detection methods to protect against a variety of attacks and harms.

Detection methods are grouped into categories depending on what type of attack they aim to protect against. While any method can be used in an input or output guard, certain categories of guards only make sense in one location (for example, prompt injection guards would usually only be useful in an input guard)

Dome currently supports the following detection methods. Our library of detection methods is composed of a mix of heuristics/match based detectors, classifiers, embedding-based methods, and LLM calls with custom system prompts. Based on latency and deployment constraints, combinations of these methods can be specified in a configuration file to deploy a customized version of Dome specific to a specific LLM, agent, or application.



```{eval-rst}
.. toctree::
   :maxdepth: 2
   
   security
   moderation
   privacy
   integrity
```