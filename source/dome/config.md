# Configuring Dome

Vijil Dome provides a number of input and output guards to protect against a variety of attacks and harms. Guided by internal acceptable use policies and compliance guidelines, an enterprise developer can combine one or more guards into a configuration via either a dictionary or a TOML file. Dome provides a wide range of guard methods, featuring various categories such as Security, Moderation and Privacy that can be combined and customized to enhance the security of your applications.


## Default Configuration

By default, Dome provides a default configuration that checks for Jailbreak attempts and Prompt Injection attacks while blocking toxic queries and outputs and obfuscating PII. This default configuration is available via the `get_default_config` method:

```python
from vijil_dome import Dome, get_default_config

default_dome = Dome(get_default_config())
```

## Configuring Dome 

You can configure Dome with a dictionary or a TOML file. In both structures, you configure Dome by specifying the following types of fields: input guards, output guards, execution order, and details about how each guard should work.


## Input and output guards

At the top level, specify a list of input guards and output guards you want to use, in the `input-guards` and `output-guards` fields. You can name these guards according to your own preferences. Later on in the config file, you will specify for each guard (identified by the name you chose for it) details about how the guard should work.

In our example below, we specified one input guard with the name `prompt-injection`, and one output guard with the name `output-toxicity`.


````python
example_config = {
            "input-guards": ["prompt-injection"],
            "output-guards": ["output-toxicity"],
            "prompt-injection": {
                "type": "security",
                "methods" : ["prompt-injection-deberta-v3-base", "security-llm"],
            },
            "output-toxicity":{
                "type":"moderation",
                "methods":["moderation-llamaguard"]
            },
        }
````

The next section describes how to configure the details of how the `prompt-injection` and `output-toxicity` guards work.

## Details of each guard

Once you have specified your input and output guards with names for each guard, you then specify for each guard the methods and parameters you want to use for it.

In the example above, we specified that the guard named `prompt-injection` is a guard of type `security`. Among the detection [methods available](guards/security.md) under `security`, we then specify that it should use `prompt-injection-deberta-v3-base` and `security-llm`, which are both detection methods available under [security](guards/security.md).

You can also configure further details about what parameters each detection method should use. In the example below, we configure the `security-llm` [method](guards/security.md#llm-based-detector-security-llm) to use GPT-4o instead of the default GPT-4-Turbo. 

````python
    "prompt-injection": {
                "type": "security",
                "methods" : ["prompt-injection-deberta-v3-base", "security-llm"],
                "security-llm": {
                    "model_name": "gpt-4o"
                }
            },
````

Besides parameters for specific methods, you can also configure the [order](#per-guard-execution-order) in which the methods should execute.

For a full list of methods available and their corresponding settings, please see [this list of guard methods](guards/index.md).

## Execution settings

You can also specify the order in which the individual guards should run. This can be specified both at the global level (i.e. for all input guards or all output guards) or at a per-guard level (e.g. only for `prompt-injection`). We currently support parallel guard execution, where multiple guards run in parallel, and early termination, where guardrail scanning terminates as soon as one guard flags the query string.

### Global execution settings

You can enable these settings via `input-run-parallel` and `input-early-exit` for the input guardrail, and `output-run-parallel` and `output-early-exit` for the output guardrail. In the example below, the input guardrails (`prompt-injection` and `input-toxicity`) run in parallel, and will stop as soon as one of them flags the query string.

````python
example_config = {
            "input-guards": ["prompt-injection", "input-toxicity"],
            "output-guards": ["output-toxicity"],
            "input-early-exit": True,
            "input-run-parallel": True,
            "prompt-injection": {
                "type": "security",
                "methods" : ["prompt-injection-deberta-v3-base", "security-llm"],
            },
            "input_toxicity":{
                "type":"moderation",
                "methods":["moderations-oai-api"]
            },
            "output_toxicity":{
                "type":"moderation",
                "methods":["moderation-llamaguard"]
            },
        }
````

### Per-guard execution settings

You can even configure parallelism and early termination at the guard level using the `run-parallel` and `early-exit` fields within each guard field. For example, the `prompt-injection` configuration below will run the Deberta model and the Security LLM method in parallel, but will wait till both methods have finished executing

````python
    "prompt-injection": {
            "type": "security",
            "early-exit": False,
            "run-parallel": True,
            "methods" : ["prompt-injection-deberta-v3-base", "security-llm"],
        },
````
By default, guardrails and guards have early termination enabled, and parallel execution disabled. 

## Configuring Dome via a TOML file

Dome configurations can also be described via .toml files. This enables users to easily save and edit conifgurations. Instantiating Dome from a TOML file is identical to instantiating it from a dictionary.
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