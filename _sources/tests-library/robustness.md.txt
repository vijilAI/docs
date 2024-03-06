# Robustness

Language model outputs are surprisingly fragile: small changes in the input prompts can lead to degradation in the quality of the final output.

We evaluate the robustness of an LLM using one module of 30 tests.

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