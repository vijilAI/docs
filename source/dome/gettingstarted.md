# Getting Started

## Installation 

Dome is available as a `.whl` for private preview as we continue to add additional features and functionality. Please contact us if you're interested in trying out Dome. 

Once you are granted access, you will recieve 
- a pre-signed url to the `vijil-dome` python wheel
- a MAKEFILE for easy installation 

To install simply, copy the makefile to your project directory and run 
```
EXPORT DOME_WHEEL_URL= <YOUR PRE-SIGNED URL>
make install
```
This will install the `vijil-dome` to your current active virtual environment 

You can also run 
```
curl -o vijil_dome-0.1.0-py3-none-any.whl <YOUR PRE-SIGNED URL>
pip install vijil_dome-0.1.0-py3-none-any.whl
```
to install `vijil-dome`

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