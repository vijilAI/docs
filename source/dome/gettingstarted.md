# Getting Started

## Installation

To install Dome, follow these steps:

### To install only the Dome package:
```sh
# downloads and installs dome package
make dome '<PRE-SIGNED URL>'
```

### OR

### To install the Dome package along with the models:
_Note: The download is around 2GB and it may take a few minutes or longer to complete_
```sh
# downloads and installs dome package along with the models
make dome_with_models '<PRE-SIGNED URL>'
```

## Basic Usage
Initialize Dome with the provided default config

```python
from vijil_dome import Dome, get_default_config

dome = Dome(get_default_config())

query = "How can I rob a bank?"
input_scan = dome.guard_input(query)
print(input_scan.is_safe(), input_scan.guarded_response())

response = "Here's how to rob a bank!"
output_scan = dome.guard_output(response)
print(output_scan.is_safe(), output_scan.guarded_response())
```
To create your custom guard config, refer to [Dome Configuration](url) 