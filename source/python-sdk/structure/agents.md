# Client

The `Vijil` class is intended to wrap around generic AI agents such as conversational chatbots and RAG applications.
We currently support LLMs hosted on a number of model providers. Integrations for agent frameworks such as LangChain are coming soon!

Based on the provider, deployments may be available through a public inference API or a dedicated private endpoint.

## Usage

Instantiate the Vijil client with your Vijil API key as follows:

```python
from vijil import Vijil
client = Vijil(api_key=YOUR_API_KEY)
```

Once you've instantiated a client, you can [create an evaluation or list all evaluations](evaluations.md).