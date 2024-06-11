# Privacy

| Harness                     | Probe                                         | Detector                                        |
| --------------------------- | --------------------------------------------- | ----------------------------------------------- |
| vijil.harnesses.privacy     | All probes below                              |                                                 |
| [vijil.harnesses.leakreplay](#copyrighted-data-leakage)  | vijil.probes.leakreplay.LiteratureComplete80  | garak.detectors.leakreplay.StartsWith           |
|                             | vijil.probes.leakreplay.LiteratureCloze80     | garak.detectors.base.TriggerListDetector        |
|                             | vijil.probes.leakreplay.GuardianComplete      | garak.detectors.leakreplay.StartsWith           |
|                             | vijil.probes.leakreplay.GuardianCloze         | garak.detectors.base.TriggerListDetector        |
|                             | vijil.probes.leakreplay.NYTComplete           | garak.detectors.leakreplay.StartsWith           |
|                             | vijil.probes.leakreplay.NYTCloze              | garak.detectors.base.TriggerListDetector        |
| [vijil.harnesses.privateinfo](#private-data-leakage) | [vijil.probes.privateinfo.EnronLeakEmail](#private-training-data)       | garak.detectors.base.TriggerListDetector        |
|                             | [vijil.probes.privateinfo.LeakPII](#inference-stage-private-data)              | garak.detectors.base.TriggerListDetector        |
|                             | [vijil.probes.privateinfo.PrivacyUnderstanding](#privacy-understanding) | autoredteam.detectors.privateinfo.DontAnswerYes |


LLM outputs can accidentally disseminate confidential information. Such sensitive data leakage poses substantial privacy (and security) risks in terms of reputational harm and potential legal consequences.

We test if an LLM is prone to leaking confidential data from both training data and inference-stage data.

## Copyrighted data leakage

[Chang _et al_, 2023](https://arxiv.org/abs/2305.00118) found that LLMs are prone to memorizing text from sources
available on the internet. Our tests are intended to probe for such memorization capabilities. For this, we supply an agent
with
- a sentence with one missing word and ask it to fill in the masked word (cloze completion)
- an incomplete sentence and ask it to complete it (sentence completion)

We perform two such evaluations for each of the following three sources of text:

1. Book passages from English literature,
2. Articles from New York Times,
3. Articles from The Guardian.

## Private data leakage

These probes test for whether models will reveal private data from either their training data or their inference-time data.

### Private training data

We use [Decoding Trust's](https://github.com/AI-secure/DecodingTrust/tree/main) Enron dataset to test whether models will leak private data from the Enron emails.

### Inference-stage private data

We use [Decoding Trust's](https://github.com/AI-secure/DecodingTrust/tree/main) synthetic prompts to test whether models will leak private data like social security numbers and SSH keys if these are provided at the inference stage. For example, if a user enters a query to a chatbot that contains private data, will this data be easily extractable later in the same conversation?

### Privacy understanding

The privacy understanding probe, adapted from [Decoding Trust](https://github.com/AI-secure/DecodingTrust/tree/main), measures whether the model understands when not to reveal private information. The prompts ask the model whether it is appropriate to reveal private information in various settings.
