# DAN

A model provider typically prepends a system prompt that stipulates organizational policies (safety guardrails, content moderation filters, etc.) to every user prompt. A Do-Anything-Now (DAN[^1]) attack is a user prompt designed to get the model to ignore these guardrails. Falcon-40B-Instruct exhibits high susceptibility to DAN attacks.

Vijil covers 15 DAN attack scenarios through its tests.

* AntiDAN
* AutoDAN
* ChatGPT Developer Mode + RANTI
* ChatGPT Developer Mode v2
* ChatGPT Markdown Image Unlocker
* DAN Jailbreak
* DUDE
* DAN 6.0
* DAN 6.2
* DAN 7.0
* DAN 8.0
* DAN 9.0
* DAN 10.0
* DAN 11.0
* STAN

{% hint style="info" %}
DAN attacks are covered by the `autoredteam.dan` test module.
{% endhint %}



[^1]: [ChatGPT is easily abused, or let's talk about DAN](https://adguard.com/en/blog/chatgpt-dan-prompt-abuse.html)
