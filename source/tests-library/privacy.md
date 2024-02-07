# Privacy

LLM outputs can accidentally disseminate confidential information. Such sensitive data leakage poses substantial privacy (and security) risks in terms of reputational harm and potential legal consequences.

We test if an LLM is prone to leaking confidential data—either in a benign or adversarial setting—using 7 tests, divided into 2 modules. 

## Data leakage

[Chang _et al_, 2023](https://arxiv.org/abs/2305.00118) found that LLMs are prone to memorizing text from sources
available on the internet. Our tests are intended to probe for such memorization capabilities. For this, we supply an agent
with
- a sentence with one missing word and ask it to fill in the masked word (cloze completion)
- an incomplete sentence and ask it to complete it (sentence completion)

We perform two such evaluations for each of the following three sources of text:

1. Book passages from English literature,
2. Articles from New York Times,
3. Articles from The Guardian.

```{eval-rst}
.. note::
    In our Python SDK, these tests are covered by the module ``autoredteam.tests.leakreplay``.
```
## Poem Attack
AI security researchers from Google recently [pointed out](https://www.vice.com/en/article/88xe75/chatgpt-can-reveal-personal-information-from-real-people-google-researchers-show)
that when repeatedly asked to repeat the word ‘poem’ or ‘book’ indefinitely, 
in some cases ChatGPT diverged to copy outputs directly from training data.

```{eval-rst}
.. note::
    In our Python SDK, these tests are covered by the module ``autoredteam.tests.replay``.
    
    This test is also part of our suite of Security tests.
```