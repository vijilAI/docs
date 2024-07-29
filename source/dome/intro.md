# Introduction

<!-- ## Blue Teaming -->

AI blue teaming covers defense mechanisms to proactively defend the agent or model against failure modes found through red teaming tests. Blue teaming methods that are popular currently include LLM firewalls, prompt augmentation, and safety guardrails. However, such methods are sometimes overly defensive, and can be bypassed [^1].

In the longer term, deeper defense strategies such as adversarial finetuning and Constitutional AI[^2] may be more robust. However, technical challenges related to computational stability and tradeoffs need to be overcome to make such techniques mainstream.

Using **Vijil Dome**, an enterprise AI engineer or developer can protect a generative AI system by
- Applying guardrails on system prompts
- Routing the input to and output from my app through scanners to block or redact harmful and malicious content
- Applying scanners through policies that map to internal usage restrictions, local/national/international regulations, and standards such as OWASP Top 10 for LLMs.
- Creating new policies or modify existing policy components to adapt to changing threat landscapes.

**(Coming Soon!)** Input and outputs from real-world usage passing through a Dome deployment are logged and stored for post-hoc analysis and improvement. Over time, Vijil Dome adapts to usage patterns of the specific enterprise and application context it is deployed in by retraining its detection models on these datasets.



[^1]: [The Art of Defending: A Systematic Evaluation and Analysis of LLM Defense Strategies on Safety and Over-Defensiveness](https://arxiv.org/abs/2401.00287)
[^2]: [Constitutional AI: Harmlessness from AI Feedback](https://www.anthropic.com/index/constitutional-ai-harmlessness-from-ai-feedback)

