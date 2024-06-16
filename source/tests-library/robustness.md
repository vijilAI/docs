# Robustness

Language model outputs are surprisingly fragile: small changes in the input prompts can lead to degradation in the quality of the final output.

We evaluate the robustness of an LLM using one module of 30 tests.

## Adversarial GLUE

The Adversarial GLUE ([AdvGLUE](https://adversarialglue.github.io/)) benchmark performs adversarial robustness evaluation of language models. 
It is an adversarial version of the GLUE benchmark, covering

- Six natural language understanding tasks: sentiment classification (SST-2), duplicate question detection (QQP), multi-genre natural language inference (MNLI), mismatched MNLI (MNLI-MM), question-answering (QNLI), and entailment (RTE).
- Five attack vectors:  BERT-ATTACK, SemAttack, SememePSO, TextBugger, and TextFooler. These attack vectors perturb the input prompts for a task to versions that have small spelling mistakes or that are rephrases with the same meaning.

We adapted the prompts in AdvGLUE to our purposes, keeping only those perturbed input prompts that truly preserve the meanings of the original prompts. Taking all combinations of tasks and attacks, we probe whether the model's performance declines on a task when the input prompts are perturbed by an attack vector.