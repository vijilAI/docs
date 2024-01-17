<!-- TODO: add notebook to docs repo -->

# Writing Custom Tests

You can also create custom tests with AutoRedTeam. This allows for more flexibility if some AutoRedTeam tests
used by default do not suit your needs. While this is a bit more advanced than the previous example,
it is still pretty straightforward and can be done with a handful lines of code.

Below, we are going craft a simple test of factuality. We'll start with a basic factual question "Who was the first president of USA?",
generate a few paraphrases of this question, and write a test suite that checks whether the paraphrased questions still output the intended answer.

Let's start by importing a few classes from `autoredteam`.

```python
from autoredteam.tests.base import Test
from autoredteam.perturbations.paraphrase import PegasusT5
from autoredteam.detectors.base import StringAbsenceDetector
```

The base `Test` class allows you to write custom tests, the `PegasusT5` class is a wrapper around a paraphrase generation model, and `StringAbsenceDetector` checks for absence of a specified string in the output when it's called on an 'attempt', essentially an LLM input-output pair.

Let's start by generating a few paraphrases.

```python
prompt = "Who was the first president of USA?"
pp_class = PegasusT5()
pp_prompts = pp_class.perturb_prompt(prompt)
pp_prompts
# ['Who was the first president of the USA?',
#  'Who was the first president of the United States?',
#  'Who was the first president of the US?',
#  'Who was the first President of the USA?',
#  'Who was the first American president?',
#  'The first president of the USA?']
```

We then instantiate the detector with the correct answer, and define our test that wraps around the paraphrased prompts and the detector instance.

```python
custom_detector = StringAbsenceDetector(substrings = ["George Washington"])
custom_test = Test(
    name = 'FirstPresident',
    prompts = pp_prompts,
    detectors = [custom_detector]
)
```

That's it, we're now ready to run our test! To do this, we use a Mistral-7B model off OctoAI as before.

```python
from autoredteam.agents.octo import OctoAPI
agent = OctoAPI(name = "mistral-7b-instruct-fp16", generations=2)
custom_test.run(agent)
# FirstPresident                    base.StringAbsenceDetector:   12/  12 ( 100.0%) passed
```

As we see above, our test `FirstPresident` has a 100% success rate on the Mistral 7B model. This indicates the model generated the correct answer in all the attempts.

To double check, let's finish by printing out the outputs from all attempts.

```python
custom_test.eval_outputs
# [' The first president of the United States was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the American Revolution and was unanimously chosen as the first president under the new Constitution. His leadership and vision helped establish the foundations of the American government.',
#  ' The first president of the United States was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the American Revolution and was unanimously chosen as the first president under the new Constitution. His leadership and vision helped establish the foundations of American democracy.',
#  ' The first President of the United States was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the founding of the country and was unanimously chosen by the Electoral College to lead the new nation. His leadership and vision helped establish the foundations of American democracy.',
#  ' The first President of the United States was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the founding of the country and was unanimously chosen by the Electoral College to lead the new nation. His leadership and vision helped establish the foundations of American democracy.',
#  ' The first President of the United States was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the founding of the country and was unanimously chosen by the Electoral College to lead the new nation. His leadership and vision set the foundation for the presidency and American democracy.',
#  ' The first President of the United States was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the founding of the country and was unanimously chosen by the Electoral College to lead the new nation. His leadership and vision set the foundation for the presidency and American democracy.',
#  ' The first President of the United States was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the founding of the country and was unanimously chosen by the Electoral College to lead the new nation. His leadership and vision helped establish many of the foundational institutions and policies that continue to shape American government.',
#  ' The first President of the United States was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the founding of the country and was unanimously chosen by the Electoral College to lead the new nation. His leadership and vision set the foundation for the presidency and American democracy.',
#  ' The first American president was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the founding of the United States and was unanimously chosen by the Electoral College to lead the new nation. His presidency set many precedents and helped establish the framework for the executive branch of government.',
#  ' The first American president was George Washington. He served two terms from April 30, 1789, to March 4, 1797. Washington played a crucial role in the founding of the United States and was unanimously chosen by the Electoral College to lead the new nation. His presidency set many precedents and helped establish the foundations of American democracy.',
#  " George Washington was the first President of the United States, serving two terms from April 30, 1789, to March 4, 1797. He played a crucial role in the American Revolution and was unanimously elected as the President by the Electoral College. Washington's leadership and vision helped establish the foundations of the American government and set the precedent for the peaceful transfer of power.",
#  " George Washington was the first President of the United States, serving two terms from April 30, 1789, to March 4, 1797. He played a crucial role in the American Revolution and was unanimously elected as the President by the Electoral College. Washington's leadership and vision helped establish the foundations of the American government and set the precedent for the peaceful transfer of power."]
 ```