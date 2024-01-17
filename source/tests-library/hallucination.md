# Hallucination / Confabulation

Language models are said to "hallucinate", or more accurately, confabulate,
when they generate content that does not correspond to our knowledge of the real-world or is inconsistent with facts.
Our test suite checks an LLM-based agent for multiple such vulnerabilities.

## Misleading claims

This test checks for a subset of confabulation/hallucination,
where false information is present that the agent is expected to
deny, refute, or contradict.

```{eval-rst}
.. note::
    In our Python SDK, this test is by the module ``autoredteam.tests.misleading``.
```

## Package hallucination

This vulnerability was discovered [recently](https://www.scmagazine.com/news/ai-package-hallucination-malicious-code-developer-environments).
If an LLM agent ends up hallucinating fake code libraries or packages, attackers can upload packages to respective repositories, so that whoever downloads those
packages gets infected.

Currently, we test whether an LLM hallucinates Python package names.

```{eval-rst}
.. note::
    In our Python SDK, this test is covered by the module ``autoredteam.tests.packagehallucination``.

    This test is also part of our suite of security tests.
```

## Snowball

Through these tests,  we evaluate an agent by prompting it to generate false outputs and then further prompting
it to over-commit to these false outputs by generating explanations.
The question-answering datasets used for this purpose is due to [Zhang _et al_, 2023](https://arxiv.org/abs/2305.13534), and
consists of complex reasoning questions where ideally it should not give any answer.

```{eval-rst}
.. note::
    In our Python SDK, these tests are covered by the module ``autoredteam.tests.snowball``.
```