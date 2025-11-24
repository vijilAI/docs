# Getting Started

## Installation 

To install the Dome package:
```bash
# install Dome
pip install vijil-dome
```

Dome has the following additional extras that can be installed 
- opentelemetry (`pip install vijil-dome[opentelemetry]`) for opentelemetry support
- google (`pip install vijil-dome[google]`) to enable observability on GCP via cloud traces, metrics and logs
- langchain (`pip install vijil-dome[langchain]`) to use Dome as a langchain runnable
- embeddings (`pip install vijil-dome[embeddings]`) for fast embeddings support (not supported on GCP)


## Basic Usage
Initialize Dome with the provided default config:

```python
from vijil_dome import Dome

# If you're running your code in a notebook, add these lines
# import nest_asyncio
# nest_asyncio.apply()

dome = Dome()

query = "How can I rob a bank?"
input_scan = dome.guard_input(query)
print(input_scan.is_safe(), input_scan.guarded_response())

response = "Here's how to rob a bank!"
output_scan = dome.guard_output(response)
print(output_scan.is_safe(), output_scan.guarded_response())
```

To further customize Dome, refer to [Dome Configuration](./config.md) 