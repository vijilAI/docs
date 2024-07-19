# Getting Started

## Installation 

Once you have access to the `vijil-dome` github repository, you can install the Dome by running the command \
`pip install git+https://github.com/vijilAI/vijil-dome.git@domelibrary`

## Basic Usage
Dome's basic usage pattern is very straightforward - simply initialize Dome with a config, and scan strings

```python
from vijil_dome import Dome, get_default_config

my_dome = Dome(get_default_config())

query = "How can I rob a bank?"
input_scan = my_dome.guard_input(query)
print(input_scan.is_safe(), input_scan.guarded_response())

response = "Here's how to rob a bank!"
output_scan = my_dome.guard_output(response)
print(output_scan.is_safe(), output_scan.guarded_response())
```

A dome config is a dictionary or TOML file that specifies a list of Guards that should be applied to an LLM input or LLM response. Each Guard is made up of mutiple detection methods, whose details can be found in [this list of detection methods](guards/index.md)