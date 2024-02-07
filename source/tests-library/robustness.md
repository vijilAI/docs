# Robustness

LLMs can generate content that perpetuate harmful stereotypes against historically marginalized communities.
These tests checks if an LLM-based agent is prone to generate such stereotypical content when asked to do so.

## AdvGLUE

The Adversarial GLUE ([AdvGLUE](https://adversarialglue.github.io/)) benchmark performs adversarial robustness evaluation of language models. 
It is an adversarial version of GLUE benchmark, covering

- Six natural language understanding tasks: sentiment classification (SST-2), duplicate question detection (QQP), multi-genre natural language inference (MNLI), mismatched MNLI (MNLI-MM), question-answering (QNLI), and entailment (RTE).
- Five attack vectors:  BERT-ATTACK, SemAttack, SememePSO, TextBugger, and TextFooler.

Taking all combinations of tasks and attacks, we designed a total of 30 tests that probe a LLM for robustness.

```{eval-rst}
.. note::
    In our Python SDK, these tests are covered by the module ``autoredteam.tests.advglue``.
```