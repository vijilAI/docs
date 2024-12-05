# Configuring Guardrails

Dome offers a flexible system to secure your applications through configurable guardrails. Here's how to understand and set them up:

### Step 1: Choose and Configure Guardrails

Dome provides [the following types](overview.md#guardrails) of guardrails:
1. Input Guardrails
2. Output Guardrails
2. Retrieval Guardrails (coming soon)
3. Execution Guardrails (coming soon)

The type of guardrail simply indicates where it is supposed to run in an application flow. 

To configure a guardrail :
- provide a list of guards
- specify whether guards should run serially or in parallel (`run-parallel`)
- specify whether all guards should run, or execution should terminate as soon as one guard is a hit (`early-exit`)

### Step 2: Assemble and Configure Guards

Guards are groups of detectors of a particular type that make up a guardrail. Guards can be named as you like, and are completely user defined. 

Each guard must be one of the following types:
1. Security
2. Moderation
3. Privacy
4. Integrity

To configure a guard:
- specify the type of guard
- provide a list of detectors of the same type as the guard
- specify whether detectors should run serially or in parallel (`run-parallel`)
- specify whether all detectors should run, or execution should terminate as soon as one detector is a hit (`early-exit`)

### Step 3: Select and Configure Detectors

Guards are made up of detectors. To set up your guards:
1. Choose specific detectors from Dome's growing library
2. Configure each detector with settings like thresholds or context-length. 

These settings depend on the detector used. Please see the [list of detection methods](guards/index.md) for a comprehensive list of all the detection methods we currently offer and the settings they have. 

### Example

````python
example_config = {

            # The input guardrail has two guards - 'prompt-injection' and 'input-toxicity'
            "input-guards": ["prompt-injection", "input-toxicity"],
            # The output guardrail has one guard - 'output-toxicity'
            "output-guards": ["output-toxicity"],

            # Here, we set the input guardrail's execution settings. Early-exit and parallel execution are enabled
            "input-early-exit": True,
            "input-run-parallel": True,

            # By not specifying the output guardrail's execution settings, the default values are used. It runs serially, and has early-exit enabled.

            # Here, we set up the 'prompt-injection' guard. 
            "prompt-injection": {
                "type": "security", # This type governs what detectors can be used in the guard. Only detectors of the same type can be used

                # Here, we specify guard-level execution settings
                "early-exit": False,    # This guard does not terminate early
                "run-parallel": True,   # This guard runs its detection methods in parallel

                # We specify the detection methods we want to use - "prompt-injection-deberta-v3-base" and "security-llm", both of which are security methods
                "methods" : ["prompt-injection-deberta-v3-base", "security-llm"],

                # Here, we are configuring detector-specific settings. 
                # We are using GPT 4 as the LLM in the security-llm detector instead of the default GPT-4 Turbo
                "security-llm": {
                    "model_name": "gpt-4"
                }
            },

            # This sets up the 'input-toxicity' guard. 
            "input-toxicity":{
                "type":"moderation",
                # Since we do not specify the guard-level execution settings, the default values are used. It runs serially, and has early-exit enabled.

                # We have just one method in this guard, which is the OpenAI moderations API
                "methods":["moderations-oai-api"]
            },

            # This sets up the 'output-toxicity' guard. 
            "output-toxicity":{
                "type":"moderation",
                "methods":["moderation-llamaguard"]
            },
        }
````



## Configuring Dome via a TOML file

Dome configurations can also be described via .toml files. This enables users to easily save and edit configurations. Instantiating Dome from a TOML file is identical to instantiating it from a dictionary.
```python
from vijil_dome import Dome

dome_from_toml = Dome(<PATH_TO_TOML_FILE>)
```

An example of a TOML configuration is shown below, followed by its corresponding dictionary representation. 

````toml
[guardrail]
input-guards = ["prompt-injection", "input-toxicity"] 
output-guards = ["output-toxicity"] 
input-early-exit = false

[prompt-injection] 
type="security"
early-exit = false
methods = ["prompt-injection-deberta-v3-base", "security-llm"]

[prompt-injection.security-llm]
model_name = "gpt-4o"

[input-toxicity]
type="moderation"
methods = ["moderations-oai-api"]

[output-toxicity]
type="moderation"
methods = ["moderation-llamaguard"]
````

````python
{
    "input-guards": ["prompt-injection", "input-toxicity"],
    "output-guards": ["output-toxicity"],
    "input-early-exit": False,
    "prompt-injection": {
        "type": "security",
        "early-exit": False,
        "methods" : ["prompt-injection-deberta-v3-base", "security-llm"],
        "security-llm": {
            "model_name": "gpt-4o"
        }
    },
    "input-toxicity":{
        "type":"moderation",
        "methods":["moderations-oai-api"]
    },
    "output-toxicity":{
        "type":"moderation",
        "methods":["moderation-llamaguard"]
    },
}
````

To create a TOML configuration for Dome, ensure that you have a field named ```guardrail``` that lists out the input and output guards, and the parallel execution/early termination settings you need. To specify settings for a method in a guard, use  ```<GUARD_NAME>.<METHOD_NAME>```. 

````{note}
When specifying booleans in the TOML, please ensure to use **lowercase** values (i.e, 'true' and 'false').
````

### Overall Config Structure


The ```guardrail``` field describes the high level structure of a Dome configuration.
| Attribute | Type | Description |
|---|---|---|
| `input-guards` | List | user-defined list of guard modules used to scan an input |
| `input-early-exit` | Boolean | determines if the input guardrail runs in "early-exit" mode, i.e, stop execution as soon as one of the guards in the input guardrail has flagged the input. (Default is True) |
| `input-run-parallel` | Boolean | determines whether guards in the input guardrail are executed in parallel. (Default is False) |
| `output-guards` | List | user-defined list of guard modules used to scan an output |
| `output-early-exit` | Boolean | determines if the output guardrail runs in "early-exit" mode, i.e, stop execution as soon as one of the guards in the output guardrail has flagged the input. (Default is True) |
| `output-run-parallel` | Boolean | determines whether guards in the output guardrail are executed in parallel. (Default is False) |

Inside a guardrail specification, the configuration of each guard module can be specified by creating a new field with the module name. 

Each ```guard``` module has four attributes.

| Attribute | Type | Description |
|---|---|---|
| `type` | Enum | user-defined type of the guard module, specifying the category of guards that it holds. Every guard module can be exactly one of the four currently supported types: `security`, `moderation`, `privacy`, and `integrity` (experimental) |
| `methods` | List | describes which methods are to be used in the guard module. Possible methods depend on the type selected, and can be chosen from the [list of methods](guards/index.md) under that type. 
| `early-exit` | Boolean | determines if the guard runs in "early-exit" mode, i.e, stop execution as soon as one of the methods in guard has the flagged the query |
| `run-parallel` | Boolean |  determines whether methods in the guard are executed in parallel. (Default is False) |

Finally, to customize a configuration at the method-level, you need to create a new field with the name ```<MODULE-NAME>.<METHOD-NAME>```. In the example above, ```prompt-injection.security-llm``` describes the configuration settings for the ```security-llm``` method of the ```prompt-injection``` guard module. This configuration scheme lets users create custom settings for different groups and use the same method with different settings in a guardrail. See the next section for detailed instructions on the options available for each method.