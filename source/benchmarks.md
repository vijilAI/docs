# Benchmarks

Beside the Vijil trust score, Vijil also offers the option of testing your models on open-source benchmarks. The scores for these benchmarks are not validated by Vijil. They merely aim to reproduce the logic of the original open-source benchmarks.

To run benchmarks from the UI, select the **Benchmarks** tab when creating an evaluation.

## List of Benchmarks

### Reliability

These benchmarks test whether models are good at tasks involving knowledge and robust reasoning.

- MMLU
- ARC
- HellaSwag
- Adversarial GLUE
- ARC
- GSM8k

## Security

These benchmarks test elements of cybersecurity.

- garak
- CyberSecEval 3
- JailbreakBench

## Safety

These benchmarks test whether models will produce harmful, biased, or inappropriate content.

- Winobias
- [ETHICS]((https://github.com/hendrycks/ethics))
- SocialStigmaQA
- Winogrande
- Safe Eval
- RealToxicityPrompts
- BBQ
- [JiminyCricket](https://github.com/hendrycks/jiminy-cricket)
- TruthfulQA
- HarmBench
- Do Not Answer
- Semi-automatic Attack Prompts