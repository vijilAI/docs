# Perturbations

LLM evaluations are surprisingly brittle: small changes in input prompts can positively or negatively affect the quality of
responses they generate. Such perturbations may be as simple as adding a prefix or suffix to a prompt,
or changing the case, or more complex, such as generating a paraphrase or performing adversarial attacks.

In `autoredteam` we use the `Perturbation` class to implement such changes that you can apply to the prompts
inside a test and run the same tests on the perturbed prompts. Other perturbations inherit from it.

## Case changes

The three perturbations inside `autoredteam.perturbations.casechange` make small changes to prompts 
in a test that change case of a prompt/prompts to 

- `LowerCase`: all lowercase
- `UpperCase`: all UPPERCASE
- `CaseSwitch` all uppercase but randomly make some letters lowercase with some probability (default 0.1)

## Encoding

These two perturbations in `autoredteam.perturbations.encoding` are designed to return encoded versions of any input prompts.

- `Base64`: Base64 encoding
- `CharCode`: CharCode encoding

## Paraphrases

These two perturbations in `autoredteam.perturbations.paraphrase` generate realistic paraphrases of a
base prompt that can be used to test for consistency of outputs.

- `PegasusT5`: uses the [Pegasus](https://huggingface.co/tuner007/pegasus_paraphrase) paraphrasing model
- `Fast`: uses a [lightwright paraphraser](https://huggingface.co/humarin/chatgpt_paraphraser_on_T5_base) trained on a
ChatGPT paraphrase dataset (coming soon!)

All of the classes offer a function `perturb_prompt` that you an use to perturb an input prompt.
[Later](../examples/custom-tests) we show how to write a custom test that checks for factuality on multiple paraphrases
generated on a base prompt.