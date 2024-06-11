# Ethics

| Harness                          | Probe                                                 | Detector                                              |
| -------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| vijil.harnesses.ethics           | All probes named below                                | autoredteam.detectors.base.TriggerListAbsenceDetector |
| [vijil.harnesses.normative_ethics](#probes-from-the-ethics-dataset) | vijil.probes.normative_ethics.Deontology              | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.normative_ethics.DeontologyJailbreak     | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.normative_ethics.Justice                 | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.normative_ethics.JusticeJailbreak        | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.normative_ethics.Morality                | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.normative_ethics.MoralityJailbreak       | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.normative_ethics.Utilitarianism          | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.normative_ethics.UtilitarianismJailbreak | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.normative_ethics.Virtue                  | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.normative_ethics.VirtueJailbreak         | autoredteam.detectors.base.TriggerListAbsenceDetector |
| [vijil.harnesses.jiminycricket](#jiminy-cricket)    | vijil.probes.jiminycricket.Jiminy                     | autoredteam.detectors.base.TriggerListAbsenceDetector |
|                                  | vijil.probes.jiminycricket.JiminyJailbreak            | autoredteam.detectors.base.TriggerListAbsenceDetector |

As intelligent agents designed to automate human-grade tasks, it is important for an LLM to have knowledge of basic concepts of morality that goes beyond toxicity, bias, or stereotypes— such as justice, well-being, duties, and virtues.

We evaluate the propensity of an LLM to generate content that is ethically questionable. We use modified versions of the [ETHICS](https://github.com/hendrycks/ethics) and [Jiminy Cricket](https://github.com/hendrycks/jiminy-cricket) datasets for this.

## Probes from the ETHICS dataset

These probes determine whether the model makes judgments that are consistent with a few major ethical theories. Specifically, they test whether the model's responses are consistent with deontological ethics, virtue ethics, utilitarianism, justice, and commonsense morality.

We also include jailbreaking versions of these probes adapted from [Decoding Trust](https://github.com/AI-secure/DecodingTrust/tree/main). These versions insert adversarial phrases into the system and user prompts that aim to increase the probability of the model providing unethical responses.

## Jiminy Cricket

We use the Jiminy Cricket probes in the way described in [Decoding Trust](https://github.com/AI-secure/DecodingTrust/tree/main), i.e. to evaluate whether models can accurately judge the moral valence of a scenario. Each scenario consists of an action and an observation in a text-based computer game.

Similarly to Decoding Trust, we also include jailbreaking versions of the same scenarios. These contain adversarial phrases that aim to disrupt the model's ability to accurately determine moral valence.