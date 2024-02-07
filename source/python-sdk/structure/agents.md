# Agents

The `Agent` class is intended to wrap around generic AI agents such as conversational chatbots and RAG applications.
We currently support LLMs hosted on a number of model providers. Integrations for agent frameworks such as LangChain are coming soon!

Based on the provider, deployments may be available through a public API or a dedicated private endpoint.

## Usage

To use a model hosted on a particular provider, simply load the respective module and class, then pass the model identifier
(stub or full URL) as the `name` argument. Optionally, you can specify how many times responses for each prompt in an AutoRedTeam test
needs to be generated using the `generations` parameter (default is 10).

Here are examples of how you can instantiate the agents we support.

### Public APIs

````{tab} Anyscale
```python
from autoredteam.agents.anyscale import AnyscaleAPI
agent = AnyscaleAPI(name="meta-llama/Llama-2-7b-chat-hf")
```

````

````{tab} Mistral
```python
from autoredteam.agents.mistral import MistralAPI
agent = MistralAPI(name="mistral-tiny")
```
````

````{tab} OpenAI
```python
from autoredteam.agents.openai import OpenaiAgent
agent = OpenaiAgent(name="gpt-4")
```
````

````{tab} Together
```python
from autoredteam.agents.together import TogetherAPI
agent = TogetherAPI(name="togethercomputer/falcon-40b-instruct")
```
````


```{eval-rst}
.. note::
    For public APIs we recommend using your own API token to avoid rate limits.
```

### Hugging Face

````{tab} Public
```python
from autoredteam.agents.huggingface import InferenceAPI
agent = InferenceAPI(name="gpt2")
```

````

````{tab} Private
```python
from autoredteam.agents.huggingface import InferenceEndpoint
agent = InferenceEndpoint(name="https://xxx.us-east-1.aws.endpoints.huggingface.cloud")
```

````

### OctoAI

````{tab} Public
```python
from autoredteam.agents.octo import OctoAPI
agent = OctoAPI(name="mistral-7b-instruct-fp16")
```

````

````{tab} Private 
```python
from autoredteam.agents.octo import OctoEndpoint
agent = OctoEndpoint(name="https://llama-2-70b-chat-xxx.octoai.run/v1/chat/completions")
```

````

### Replicate

````{tab} Public
```python
from autoredteam.agents.replicate import ReplicateAPI
agent = ReplicateAPI(name="meta/llama-2-70b-chat")
```

````

````{tab} Private
```python
from autoredteam.agents.replicate import ReplicateEndpoint
agent = ReplicateEndpoint(name="username/your-llama2-70b")
```

````