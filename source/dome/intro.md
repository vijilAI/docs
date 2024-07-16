# Introduction

## Blue Teaming

AI blue teaming covers defense mechanisms to proactively defend the agent or model against failure modes found through red teaming tests. Blue teaming methods that are popular currently include LLM firewalls, prompt augmentation, and safety guardrails. However, such methods are sometimes overly defensive, and can be bypassed [^1].

In the longer term, deeper defense strategies such as adversarial finetuning and Constitutional AI[^2] may be more robust. However, technical challenges related to computational stability and tradeoffs need to be overcome to make such techniques mailstream.

[^1]: [The Art of Defending: A Systematic Evaluation and Analysis of LLM Defense Strategies on Safety and Over-Defensiveness](https://arxiv.org/abs/2401.00287)
[^2]: [Constitutional AI: Harmlessness from AI Feedback](https://www.anthropic.com/index/constitutional-ai-harmlessness-from-ai-feedback)
