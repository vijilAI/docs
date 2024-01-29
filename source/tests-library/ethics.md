# Ethics


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