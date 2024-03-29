# Tests

The `autoredteam.tests.base.Test` class encapsulate the prompts and evaluation logic of a test.
All tests in `autoredteam` inherit from this class, and are divided into modules.

## List of Tests

Below is a mapping from our group of tests described earlier to modules inside `autoredteam.tests`.
Each of them contain one or more inherited `Test` classes. 

| Tests | `autoredteam.tests` module |
|---|---|
| Adversarial suffix | `gcg` |
| DAN | `dan` |
| Encoding | `encoding` |
| Glitch | `glitch` |
| Goodside | `goodside` |
| Known bad signatures | `knownbadsignatures` |
| Malware generation | `malwaregen` |
| Package hallucination | `packagehallucination` |
| Prompt injection | `promptinject` |
| Poem attack | `replay` |
| Cross-site scripting | `xss` |
| Misleading claims | `misleading` |
| Snowball | `snowball` |
| AdvGLUE | `advglue` |
| Attack generation | `atkgen` |
| Continuation | `continuation` |
| Real Toxicity Prompts | `realtoxicityprompts` |
| Data leakage  | `leakreplay` |
| Adversarial Stereotype | `advstereo` |
| Adult dataset | `adultdata` |
| WinoBias | `winobias` |
| Virtue alignment | `hendrycksethics` |
| Risk Cards | `lmrc` |

To list the tests inside one or more module(s), you can adapt
the following example:

```python
import json
from autoredteam.utils import list_all_tests
test_list = list_all_tests(modules=['leakreplay','realtoxicityprompts'])
print(json.dumps(test_list))
# {
#     "leakreplay": [
#         "GuardianCloze", 
#         "GuardianComplete",
#         "NYTCloze",
#         "NYTComplete",
#         "LiteratureCloze80",
#         "LiteratureComplete80"
#     ],
#     "realtoxicityprompts": [
#         "RTPBlank",
#         "RTPFlirtation",
#         "RTPIdentity_Attack",
#         "RTPInsult",
#         "RTPProfanity",
#         "RTPSevere_Toxicity",
#         "RTPSexually_Explicit",
#         "RTPThreat"
#     ]
# }
```

Skipping the `modules` argument returns a dictionary of *all* tests grouped by modules.

## Detectors

After a test is run on an agent, a number of prompts and responses are generated.
The `Detector` class, called from `autoredteam.detectors.base`, codifies the evaluation logic of scoring a response as a pass or fail
based on what that test is intended to do.

Each of the tests are associated with inherited detector classes that are one of the following type.

- **Heuristics-based**: Rule-based detectors that look for presence or absence of a list of strings.
    - `StringDetector`: presence of one of more substrings constitutes a hit. List of substrings passed as arguments when initiating a `Test` class.
    - `StringAbsenceDetector`: absence of one of more strings constitutes a hit.
    - `TriggerListDetector`: A variation of `StringDetector` that utilizes blocklists specific to individual prompts inside a test, instead of the whole test.
    - `TriggerListAbsenceDetector`: prompt-level absence detector, i.e. absence of one of more strings in the trigger list constitutes a hit.

- **Classifiers**: Using the `HFDetector` class, you can use a model off Hugging Face to give a probability score to a response between
0 and 1. Response is deemed pass or fail based on a threshold defined for a `Test` using that detector.

- **Generative**: Uses GPT-4 to determine the pass or fail status of a response. Currently, such a detector is used in the `adultdata.CounterfactualGender` test. 

