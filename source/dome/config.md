# Configurations

Vijil Dome provides a number of input and output guards to protect against a variety of attacks and harms. Guided by internal acceptable use policies and compliance guidelines, and enterprise developer can combine one or more guards into a configuration via either a dictionary or a TOML file.

An example of a TOML configuration is shown below.

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

The same configuration as a dictionary is shown below.

````python
example_config = {
            "input-guards": ["prompt-injection", "input-toxicity"],
            "output-guards": ["output-toxicity"],
            "input-early-exit": False,
            "prompt-injection": {
                "type": "security",
                "early-exit":False,
                "methods" : ["prompt-injection-deberta-v3-base", "security-llm"],
                "security-llm": {
                    "model_name": "gpt-4o"
                }
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

## Structure


The ```guardrail``` field describes the high level structure of a Dome configuration. Each guardrail has two components, `input` and `output` guards. For each component, there are three possible options.

| Attribute | Type | Description |
|---|---|---|
| `guards` | List | user-defined list of guard modules used to scan an input or output |
| `early-exit` | Boolean | determines if a guard module runs in "early-exit" mode, i.e, stop execution as soon as one of the groups has flagged the input. (Default is True) |
| `run-parallel` | Boolean | determines whether guards in a module are executed in parallel. (Default is False) |

Inside a guardrail specification, the configuration of each guard module can be specified by creating a new field with the module name. In the example above, we have three guard modules: ```prompt-injection```,  ```input-toxicity``` and  ```output-toxicity```. ```prompt-injection``` and  ```input-toxicity``` apply to the input, and ```output-toxicity``` is applied only to the output. 

## Guard Modules

Each guard module has four attributes.

| Attribute | Type | Description |
|---|---|---|
| `type` | Enum | user-defined type of the guard module, specifying the category of guards that it holds. Every guard module can be exactly one of the four currently supported types: `security`, `moderation`, `privacy`, and `integrity` (experimental) |
| `methods` | List | describes which methods are to be used in the guard module. Possible methods depend on the type selected, and can be chosen from the [list of Guards](guards/index.md)) under that type. 
| `early-exit` | Boolean | Same as above |
| `run-parallel` | Boolean | Same as above |

Finally, to customize a configuration at the method-level, you need to create a new field with the name ```<MODULE-NAME>.<METHOD-NAME>```. In the example above, ```prompt-injection.security-llm``` describes the configuration settings for the ```security-llm``` method of the ```prompt-injection``` guard module. This configuration scheme lets users create custom settings for different groups and use the same method with different settings in a guardrail. See the next section for detailed instructions on the options available for each method.