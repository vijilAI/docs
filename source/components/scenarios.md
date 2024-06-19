# Scenarios

Scenarios are groups of related probes. Each scenario is its own harness, but multiple scenarios can also be composed to form other harnesses.

Here we describe each scenario and what probes it contains.

## Ethical theories

This scenario includes both vanilla and jailbreaking probes for prompts that test the model's understanding of ethical theories.


## Ethics: simulation

This scenario contains vanilla and jailbreaking prompts that ask about the moral valence of a simulated scenario.

## Copyrighted content

This scenario contains prompts that attempt to get the model to repeat copyrighted content from books and newspapers.

## Private data leak

This scenario contains prompts that test whether a model will leak private data.

## Adversarial GLUE

This scenario measures whether the model's performance on the natural language understanding tasks in [GLUE](https://gluebenchmark.com/) is affected by perturbations to the sentences in the tasks.

## Professional bias

This scenario measures whether the model associates gender with occupations.

## Stereotype

This scenario measures whether the model reinforces stereotypes about religion, race, ethnicity, age, disability, national origin, and gender in its responses.

## Malware generation

This scenario contains probes that attempt to make the model generate malware.

## Compounding hallucination

This scenario attempts to prompt the model into generating hallucinations by having it over-commit to an initial mistake.

## Misleading information

This scenario checks whether the model is able to refute false assertions presented in the input prompt.

## Gender-income bias

This scenario checks whether the model predicts a person's income in a gender-biased manner.

## Ethical harms

This scenario checks for ethical harms in the model's output, such as bullying, deadnaming, profanity, sexual content, and slurs.

## Known malware

This scenario checks for the existence of known signatures of spam and viruses in the output.

## Prompt injection

This scenario consists of prompt injections that attempt to trick the model into producing specific strings.

## Cross-site scripting

This scenario aims to get the model to produce a cross-site scripting content in a Markdown image.

## Adversarial suffix

This scenario uses adversarial suffixes to elicit instructions on how to steal from a non-profit organization.

## Package hallucination

This scenario contains prompts designed to elicit sample code importing non-existent Python packages.

## Glitch

This scenario contains prompts that use glitch tokens to disrupt expected model behavior.

## Prompt injection: encoded data

This scenario tests whether a model will decode encoded strings injected into the prompt.

## Slur continuation

This scenario tests whether a model will continue a slur when provided with leading text.

## Hallucination: Goodside

This scenario contains prompts designed by Riley Goodside to elicit hallucinations.

## Real Toxicity Prompts

This scenario contains input text, taken from web data, that are toxic if completed.

## Do Anything Now

These probes attempt to get the model to escape its guardrails by prompting it to take on a special persona.