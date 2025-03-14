# Scenarios

Scenarios are groups of related probes. Each scenario is its own harness, but multiple scenarios can also be composed to form other harnesses.

Here we briefly describe the each scenario and link to longer descriptions of every scenario under their respective dimensions. The dimension [pages](../tests-library/index.md) also list the probes that belong to each scenario.

## Ethical theories

[This scenario](../tests-library/ethics.md#ethical-theories) includes both vanilla and jailbreaking probes for prompts that test the model's understanding of ethical theories.

## Ethics: simulation

[This scenario](../tests-library/ethics.md#ethics-simulation) contains vanilla and jailbreaking prompts that ask about the moral valence of a simulated scenario.

## Copyrighted content

[This scenario](../tests-library/privacy.md#copyrighted-data-leakage) contains prompts that attempt to get the model to repeat copyrighted content from books and newspapers.

## Private data leak

[This scenario](../tests-library/privacy.md#private-data-leakage) contains prompts that test whether a model will leak private data.

## Adversarial GLUE

This scenario currently makes up the entirety of the [Robustness](../tests-library/robustness.md) harness. It measures whether the model's performance on the natural language understanding tasks in [GLUE](https://gluebenchmark.com/) is affected by perturbations to the sentences in the tasks.

## Professional bias

[This scenario](../tests-library/fairness.md#professional-bias) measures whether the model associates gender with occupations.

## Gender-income bias

[This scenario](../tests-library/fairness.md#gender-income-bias) checks whether the model predicts a person's income in a gender-biased manner.

## Stereotype

This scenario is currently makes up the entire [Stereotype](../tests-library/stereotype.md) harness. It measures whether the model reinforces stereotypes about religion, race, ethnicity, age, disability, national origin, and gender in its responses.

## Compounding hallucination

[This scenario](../tests-library/hallucination.md#compounding-hallucination) attempts to prompt the model into generating hallucinations by having it over-commit to an initial mistake.

## Misleading information

[This scenario](../tests-library/hallucination.md#misleading-information) checks whether the model is able to refute false assertions presented in the input prompt.

## Package hallucination

[This scenario](../tests-library/hallucination.md#package-hallucination) contains prompts designed to elicit sample code importing non-existent Python packages.

## Hallucination: Goodside

[This scenario](../tests-library/hallucination.md#hallucination-goodside) consists of the [Who is Riley?](../tests-library/hallucination.md#who-is-riley) and [Davidjl](../tests-library/hallucination.md#davidjl-glitch) probes. They were designed by Riley Goodside to elicit hallucinations.

## Social Values

[This scenario](../tests-library/hallucination.md#social-values) currently consists of a probe looking for promotions of quack medicine.

## Known malware

[This scenario](../tests-library/security.md#known-malware) checks for the existence of known signatures of spam and viruses in the output.

## Malware generation

[This scenario](../tests-library/security.md#malware-generation) contains probes that attempt to make the model generate malware.

## Prompt injection

[This scenario](../tests-library/security.md#prompt-injection) consists of prompt injections that attempt to trick the model into producing specific strings.

## Prompt injection: encoded data

[This scenario](../tests-library/security.md#prompt-injection-encoded-data) tests whether a model will decode encoded strings injected into the prompt.

## Cross-site scripting

[This scenario](../tests-library/security.md#cross-site-scripting-xss) aims to get the model to produce a cross-site scripting content in a Markdown image.

## Adversarial suffix

[This scenario](../tests-library/security.md#adversarial-suffix) uses adversarial suffixes to elicit instructions on how to steal from a non-profit organization.

## Glitch

[This scenario](../tests-library/security.md#glitch) contains prompts that use glitch tokens to disrupt expected model behavior.

## Do Anything Now

[These probes](../tests-library/security.md#do-anything-now-dan) attempt to get the model to escape its guardrails by prompting it to take on a special persona.

## Slur continuation

[This scenario](../tests-library/toxicity.md#slur-continuation) tests whether a model will continue a slur when provided with leading text.

## Ethical harms

[This scenario](../tests-library/toxicity.md#ethical-harms) checks for ethical harms in the model's output, such as bullying, deadnaming, profanity, sexual content, and slurs.

## Real Toxicity Prompts

[This scenario](../tests-library/toxicity.md#real-toxicity-prompts) contains input text, taken from web data, that are toxic if completed.

