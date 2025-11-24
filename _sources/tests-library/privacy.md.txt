# Privacy

LLM outputs can accidentally disseminate confidential information. Such sensitive data leakage poses substantial privacy (and security) risks in terms of reputational harm and potential legal consequences.

We test if an LLM is prone to leaking confidential data from both training data and inference-stage data.

## Probe and scenario list

| Harness/scenario | Probe | Probe Description                                                                                                        | Detector |
| --------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| Privacy               |                                                                            |                                                                                                                    |                          |
| [Copyrighted content](#copyrighted-content)   | Book excerpt completion                                                    | Tests whether the model will complete a book excerpt when prompted with the beginning                              | Starts with trigger      |
|                       | Book excerpt insertion                                                     | Tests whether the model will fill in the middle of a book excerpt                                                  | Trigger presence         |
|                       | Media excerpt completion - Guardian                                        | Tests whether the model will complete an excerpt from The Guardian when prompted with the beginning                | Starts with trigger      |
|                       | Media excerpt insertion - Guardian                                         | Tests whether the model will fill in the middle of an excerpt from The Guardian                                    | Trigger presence         |
|                       | Media excerpt completion - NYT                                             | Tests whether the model will complete an excerpt from the New York Times when prompted with the beginning          | Starts with trigger      |
|                       | Media excerpt insertion - NYT                                              | Tests whether the model will fill in the middle of an excerpt from the New York Times                              | Trigger presence         |
| [Private data leak](#private-data-leak)     | Emails leakage - Enron                                                     | Tests whether the model will reveal email addresses obtained from the discovery process of the Enron investigation | Trigger presence         |
|                       | PII Leakage                                                                | Tests whether PII provided to the model during a conversation can be leaked                                        | Trigger presence         |
|                       | Confidentiality comprehension                                              | Tests whether the model understands privacy-related phrases that flag when certain information is confidential     | Don't answer yes         |




## Copyrighted content

[Chang _et al_, 2023](https://arxiv.org/abs/2305.00118) found that LLMs are prone to memorizing text from sources
available on the internet. Our tests are intended to probe for such memorization capabilities. For this, we supply an agent
with
- a sentence with one missing word and ask it to fill in the masked word (cloze completion)
- an incomplete sentence and ask it to complete it (sentence completion)

We perform two such evaluations for each of the following three sources of text:

1. Book passages from English literature,
2. Articles from New York Times,
3. Articles from The Guardian.

## Private data leak

These probes test for whether models will reveal private data from either their training data or their inference-time data.

### Private training data

We use [Decoding Trust's](https://github.com/AI-secure/DecodingTrust/tree/main) Enron dataset to test whether models will leak private data from the Enron emails.

### Inference-stage private data

We use [Decoding Trust's](https://github.com/AI-secure/DecodingTrust/tree/main) synthetic prompts to test whether models will leak private data like social security numbers and SSH keys if these are provided at the inference stage. For example, if a user enters a query to a chatbot that contains private data, will this data be easily extractable later in the same conversation?

### Privacy understanding

The privacy understanding probe, adapted from [Decoding Trust](https://github.com/AI-secure/DecodingTrust/tree/main), measures whether the model understands when not to reveal private information. The prompts ask the model whether it is appropriate to reveal private information in various settings.
