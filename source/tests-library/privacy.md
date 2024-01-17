# Privacy

## Data leakage

[Chang _et al_, 2023](https://arxiv.org/abs/2305.00118) found that LLMs are prone to memorizing text from a number of books
available on the internet. Our tests are intended to probe for such memorization capabilities. For this, we supply an agent
with
- a sentence with one missing word and ask it to fill in the masked word (cloze completion)
- an incomplete sentence and ask it to complete it (sentence completion)

```{eval-rst}
.. note::
    In our Python SDK, these tests are covered by the module ``autoredteam.tests.leakreplay``.
```
