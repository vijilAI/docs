# Hallucination / Confabulation

Language models are said to hallucinate or confabulate when they generate content that does not correspond to our knowledge of the real-world or is inconsistent with facts. We evaluate a LLM by prompting it to generate false outputs in situations where the desired response is a refusal to answer.

Vijil's Hallucination probes evaluate whether an LLM is prone to generating hallucinations. 

## Probe and scenario list

| Harness/scenario          | Probe | Probe Description                                                     | Detector                      |
| ------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------- |
| Hallucination             | All probes below                                                           |                                                                 |                               |
| [Social values](#quack-medicine)             | Quack Medicine                                                             | Evaluates whether the model promotes quack medicine             | Quack medicine                |
| [Hallucination: Goodside](#hallucination-goodside)   | False assertions: Riley Goodside                                           | Evaluates hallucinations about Riley Goodside                   | Riley Goodside misinformation |
|                           | Glitch - Davidjl                                                           | Checks for hallucinations about the glitch token Davidjl        | Glitch                        |
| [Package hallucination](#package-hallucination)     | Hallucinate Python packages                                                | Checks if a model hallucinates Python packages                  | Python package hallucination  |
| [Compounding hallucination](#compounding-hallucination) | False assertions: senators                                                 | Checks for false assertions about US senators                   | Don't start yes               |
|                           | False assertions: general                                                  | Checks for false assertions about general history/science facts | Claim refutation              |
|                           | False assertions: flights                                                  | Checks if the model invents impossible flight routes            | Don't start yes               |
|                           | Hallucinate prime numbers                                                  | Evaluates hallucinations about prime numbers                    | Don't start no                |
## Misleading information

This test checks for a subset of confabulation/hallucination,
where false information is present that the agent is expected to
deny, refute, or contradict.


## Compounding hallucination

Through these tests,  we evaluate an agent by prompting it to generate false outputs and then further prompting
it to over-commit to these false outputs by generating explanations.
The question-answering datasets used for this purpose is due to [Zhang _et al_, 2023](https://arxiv.org/abs/2305.13534), and
consists of complex reasoning questions where ideally it should not give any answer.


## Package hallucination

This vulnerability was discovered [recently](https://www.scmagazine.com/news/ai-package-hallucination-malicious-code-developer-environments).
If an LLM agent ends up hallucinating fake code libraries or packages, attackers can upload packages to respective repositories, so that whoever downloads those
packages gets infected.

Currently, we test whether an LLM hallucinates Python package names.

## Hallucination: Goodside

### Who is Riley?

These prompts attempt to get the model to generate false information about Riley Goodside. Common hallucinations involve claiming that Riley Goodside is in the entertainment industry, Canadian, Australian, or an entrepreneur.

### Davidjl glitch

These prompts attempt to get the model to repeat false information about the glitch token "Davidjl". They were [discovered](https://twitter.com/goodside/status/1666598580319035392) by Riley Goodside.

## Social values

We use [prompts](https://github.com/leondz/lm_risk_cards/blob/main/cards/en/quack_medicine.md) from the Language Model Risk Cards framework to check if a model will promot quack medicine.