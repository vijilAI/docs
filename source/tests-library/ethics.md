# Ethics

As intelligent agents designed to automate human-grade tasks, it is important for an LLM to have knowledge of basic concepts of morality that goes beyond toxicity, bias, or stereotypes— such as justice, well-being, duties, and virtues.

We evaluate the propensity of an LLM to generate content that is ethically questionable. We use modified versions of the [ETHICS](https://github.com/hendrycks/ethics) and [Jiminy Cricket](https://github.com/hendrycks/jiminy-cricket) datasets for this.

## Probe and scenario list

| Harness/scenario | Probe                            | Probe Description                                                                                                                                                               | Detector        |
| --------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Ethics                |                                  |                                                                                                                                                                           |                 |
| [Ethical theories](#ethical-theories)      | Deontological Ethics             | Evaluates the model's understanding of whether actions are required, permitted, or forbidden according to a set of rules or constraints                             | Trigger absence |
|                       | Adversarial Deontological Ethics | Evaluates the model's understanding of whether actions are required, permitted, or forbidden according to a set of rules or constraints under adversarial prompting | Trigger absence |
|                       | Justice-based Ethics             | Evaluates whether the model understands principles of desert or impartiality                                                                                              | Trigger absence |
|                       | Adversarial Justice-based Ethics | Evaluates whether the model understands principles of desert or impartiality under adversarial prompting                                                                  | Trigger absence |
|                       | Commonsense Morality             | Evaluates whether the model's moral judgments align with common moral intuitions                                                                                          | Trigger absence |
|                       | Adversarial Commonsense Morality | Evaluates, under adversarial prompting, whether the model's moral judgments align with common moral intuitions                                                            | Trigger absence |
|                       | Utilitarianism                   | Evaluates whether the model can identify which of two scenarios has higher utility                                                                                        | Trigger absence |
|                       | Adversarial Utilitarianism       | Evaluates, under adversarial prompting, whether the model can identify which of two scenarios has higher utility                                                          | Trigger absence |
|                       | Virtue Ethics                    | Evaluates whether the model can identify moral virtues correctly                                                                                                          | Trigger absence |
|                       | Adversarial Virtue Ethics        | Evaluates, under adversarial prompting, whether the model can identify moral virtues correctly                                                                            | Trigger absence |
| [Ethics: simulation](#ethics-simulation)    | Simulation                       | Evaluates the model's ability to identify the moral valence of a simulated scenario                                                                                       | Trigger absence |
|                       | Adversarial Simulation           | Evaluates, under adversarial prompting, the model's ability to identify the moral valence of a simulated scenario                                                         | Trigger absence |



## Ethical theories

These probes determine whether the model makes judgments that are consistent with a few major ethical theories. Specifically, they test whether the model's responses are consistent with deontological ethics, virtue ethics, utilitarianism, justice, and commonsense morality.

We also include jailbreaking versions of these probes adapted from [Decoding Trust](https://github.com/AI-secure/DecodingTrust/tree/main). These versions insert adversarial phrases into the system and user prompts that aim to increase the probability of the model providing unethical responses.

## Ethics: Simulation

We use the Jiminy Cricket probes in the way described in [Decoding Trust](https://github.com/AI-secure/DecodingTrust/tree/main), i.e. to evaluate whether models can accurately judge the moral valence of a scenario. Each scenario consists of an action and an observation in a text-based computer game.

Similarly to Decoding Trust, we also include jailbreaking versions of the same scenarios. These contain adversarial phrases that aim to disrupt the model's ability to accurately determine moral valence.