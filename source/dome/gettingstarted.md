# Getting Started

## Installation 

### To install only the Dome package:
```sh
# downloads and installs dome package
make dome PRESIGNED_URL='<YOUR-PRESIGNED URL>'
```

### To install the Dome package along with the models::
```sh
# downloads and installs dome package
make dome_with_models PRESIGNED_URL='<YOUR-PRESIGNED URL>'
```

Notes: 
- Use quotes around the pre-signed URL since it contains special characters
- The models are rather large (>2GB). Installation for `dome_with_models` may take a few minutes


## Basic Usage
Initialize Dome with the provided default config

```python
from vijil_dome import Dome, get_default_config

# If you're running your code in a notebook, add these lines
# import nest_asyncio
# nest_asyncio.apply()

dome = Dome(get_default_config())

query = "How can I rob a bank?"
input_scan = dome.guard_input(query)
print(input_scan.is_safe(), input_scan.guarded_response())

response = "Here's how to rob a bank!"
output_scan = dome.guard_output(response)
print(output_scan.is_safe(), output_scan.guarded_response())
```

To further customize Dome, refer to [Dome Configuration](./config.md) 