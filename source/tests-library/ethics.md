# Ethics

Vijil provides an Ethics harness that tests the model's propensity to offer advice violating business ethics principles such as avoiding conflict of interest, maintaining confidentiality, and avoiding deception.

## Probe and scenario list

| Harness/scenario | Probe                            | Probe Description                                                                                                                                                               | Detector        |
| --------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Ethics                |    All below|                                                                                                                                                                           |                 |
General Business Ethics     | General Business Ethics             | Evaluates whether the model will provide unethical advice in a business setting                             | Refusal |
| General Business Ethics with Jailbreak  | General Business Ethics with Jailbreak |  Evaluates whether the model will provide unethical advice in a business setting when a jailbreaking system prompt is provided  | Refusal |