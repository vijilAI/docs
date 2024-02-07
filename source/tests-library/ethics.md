# Ethics

## Virtue Alignment

We adapt the [ETHICS](https://github.com/hendrycks/ethics) dataset to test how much an LLM aligns with notions of human virtues. Each input prompt consists of a scenario, e.g. Martha hired a new babysitter and was totally at ease with her, a human trait, e.g. trustful, and a 0/1 label of whether the trait is exhibited in this scenario. The LLM is tasked with making this inference. We use adversarial system prompts and evasion strings from DecodingTrust to make this test aggressive in nature.

```{eval-rst}
.. note::
    In our Python SDK, these tests are covered by the module ``autoredteam.tests.hendrycksethics``.
```

## Language Model Risk Cards

This group of tests implement the Language Model Risk Cards (LMRC) [framework](https://arxiv.org/abs/2303.18190).
LMRC specifies a large set of risks that might present in LLM deployment.

We use 8 vectors to test a model for unethical behavior, such as misrepresenting itself as a human,
disrespecting the preferences of the human users, or reinforcing restrictive stereotypes.

- Anthropomorphization
- Bullying
- Deadnaming
- Profanity
- Quack Medicine
- Sexual Content
- Sexualization
- Slur Usage

```{eval-rst}
.. note::
    In our Python SDK, these tests are covered by the module ``autoredteam.tests.lmrc``.
```