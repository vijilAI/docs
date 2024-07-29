# List of Guards

Vijil Dome has a number of input and output guards to protect against a variety of attacks and harms.

Guards are grouped into categories depending on what type of attack they aim to protect against. While any guard method can be used in an input or output guard, certain categories of guards only make sense in one location (for example, prompt injection guards would only make sense as an input guard)

Dome currently supports the following guards. Our library of guards is composed of a mix of heuristics/match based detectors, classifiers, embedding-based methods, and LLM calls with custom system prompts. Based on latency and deployment constraints, combinations of these guards can be specified in a configuration file to deploy a customized version of Dome specific to a specific LLM, agent, or application.



```{eval-rst}
.. toctree::
   :maxdepth: 2
   
   security
   moderation
   privacy
   integrity
```