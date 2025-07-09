# Robustness

Language model outputs are surprisingly fragile: small changes in the input prompts can lead to degradation in the quality of the final output.

We evaluate the robustness of an LLM using one module of 30 tests.

## Probe and scenario list

| Harness/scenario | Probe                        | Probe Description                                         | Detector                       |
| ---------------- | ---------------------------- | --------------------------------------------------------- | ------------------------------ |
| Robustness       | BERT attack on MNLI          | Probes effects of BERT-based perturbation on MNLI task    | Robustness pairwise comparison |
|                  | BERT attack on MNLI-MM       | Probes effects of BERT-based perturbation on MNLI-MM task | Robustness pairwise comparison |
|                  | BERT attack on QNLI          | Probes effects of BERT-based perturbation on QNLI task    | Robustness pairwise comparison |
|                  | BERT attack on QQP           | Probes effects of BERT-based perturbation on QQP task     | Robustness pairwise comparison |
|                  | BERT attack on RTE           | Probes effects of BERT-based perturbation on RTE task     | Robustness pairwise comparison |
|                  | BERT attack on SST2          | Probes effects of BERT-based perturbation on SST2 task    | Robustness pairwise comparison |
|                  | SemAttack on MNLI            | Probes effects of SemAttack perturbation on MNLI task     | Robustness pairwise comparison |
|                  | SemAttack on MNLI-MM         | Probes effects of SemAttack perturbation on MNLI-MM task  | Robustness pairwise comparison |
|                  | SemAttack on QNLI            | Probes effects of SemAttack perturbation on QNLI task     | Robustness pairwise comparison |
|                  | SemAttack on QQP             | Probes effects of SemAttack perturbation on QQP task      | Robustness pairwise comparison |
|                  | SemAttack on RTE             | Probes effects of SemAttack perturbation on RTE task      | Robustness pairwise comparison |
|                  | SemAttack on SST2            | Probes effects of SemAttack perturbation on SST2 task     | Robustness pairwise comparison |
|                  | SememePSO attack on MNLI     | Probes effects of SememePSO perturbation on MNLI task     | Robustness pairwise comparison |
|                  | SememePSO attack on MNLI-MM  | Probes effects of SememePSO perturbation on MNLI-MM task  | Robustness pairwise comparison |
|                  | SememePSO attack on QNLI     | Probes effects of SememePSO perturbation on QNLI task     | Robustness pairwise comparison |
|                  | SememePSO attack on QQP      | Probes effects of SememePSO perturbation on QQP task      | Robustness pairwise comparison |
|                  | SememePSO attack on RTE      | Probes effects of SememePSO perturbation on RTE task      | Robustness pairwise comparison |
|                  | SememePSO attack on SST2     | Probes effects of SememePSO perturbation on SST2 task     | Robustness pairwise comparison |
|                  | TextBugger attack on MNLI    | Probes effects of TextBugger perturbation on MNLI task    | Robustness pairwise comparison |
|                  | TextBugger attack on MNLI-MM | Probes effects of TextBugger perturbation on MNLI-MM task | Robustness pairwise comparison |
|                  | TextBugger attack on QNLI    | Probes effects of TextBugger perturbation on QNLI task    | Robustness pairwise comparison |
|                  | TextBugger attack on QQP     | Probes effects of TextBugger perturbation on QQP task     | Robustness pairwise comparison |
|                  | TextBugger attack on RTE     | Probes effects of TextBugger perturbation on RTE task     | Robustness pairwise comparison |
|                  | TextBugger attack on SST2    | Probes effects of TextBugger perturbation on SST2 task    | Robustness pairwise comparison |
|                  | TextFooler attack on MNLI    | Probes effects of TextFooler perturbation on MNLI task    | Robustness pairwise comparison |
|                  | TextFooler attack on MNLI-MM | Probes effects of TextFooler perturbation on MNLI-MM task | Robustness pairwise comparison |
|                  | TextFooler attack on QNLI    | Probes effects of TextFooler perturbation on QNLI task    | Robustness pairwise comparison |
|                  | TextFooler attack on QQP     | Probes effects of TextFooler perturbation on QQP task     | Robustness pairwise comparison |
|                  | TextFooler attack on RTE     | Probes effects of TextFooler perturbation on RTE task     | Robustness pairwise comparison |
|                  | TextFooler attack on SST2    | Probes effects of TextFooler perturbation on SST2 task    | Robustness pairwise comparison |

## Adversarial GLUE

The Adversarial GLUE ([AdvGLUE](https://adversarialglue.github.io/)) benchmark performs adversarial robustness evaluation of language models. 
It is an adversarial version of the GLUE benchmark, covering

- Six natural language understanding tasks: sentiment classification (SST-2), duplicate question detection (QQP), multi-genre natural language inference (MNLI), mismatched MNLI (MNLI-MM), question-answering (QNLI), and entailment (RTE).
- Five attack vectors:  BERT-ATTACK, SemAttack, SememePSO, TextBugger, and TextFooler. These attack vectors perturb the input prompts for a task to versions that have small spelling mistakes or that are rephrases with the same meaning.

We adapted the prompts in AdvGLUE to our purposes, keeping only those perturbed input prompts that truly preserve the meanings of the original prompts. Taking all combinations of tasks and attacks, we probe whether the model's performance declines on a task when the input prompts are perturbed by an attack vector.