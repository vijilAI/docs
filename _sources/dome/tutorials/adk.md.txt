# Using Dome Guardrails with Google ADK Agents

Agents created using Google ADK have `before_model_callback` and `after_model_callback` functions that are executed right before and after the model in the agent is invoked. Following ADK best practices, Dome's input and output guardrails can be added into the agent via these callbacks.

```python
from google.adk.agents import Agent

from vijil_dome import Dome
from vijil_dome.integrations.adk import generate_adk_input_callback, generate_adk_output_callback
# Dome is Async first, however ADK does not yet support async model callbacks
# Nest asyncio is required for compatibility until async callbacks are supported
import nest_asyncio
nest_asyncio.apply()

dome = Dome()
# Now we can generate the callback functions to guard our agents
# You can optionally customize the input or output messages here, and pass along any additional callbacks for your agent. 
guard_input = generate_adk_input_callback(
    dome, 
    blocked_message=None # optional: Customize the block message,
    additional_callback=None # Optional: Additional input callback functions
)
guard_output = generate_adk_output_callback(
    dome, 
    blocked_message=None # optional: Customize the block message,
    additional_callback=None # Optional: Additional output callback functions
)

# Finally, add guardrails to the agent
my_agent = Agent(
    model="gemini-2.0-flash-001",
    name="my_agent",
    description="An Agent built using google ADK, protected by Dome",
    instruction="You are a friendly, question-answering AI agent",
    before_model_callback=guard_input,
    after_model_callback=guard_output,
)
```

To deploy an ADK agent protected with Dome, follow ADK's [Cloud Run deployment guide via the Gcloud CLI](https://google.github.io/adk-docs/deploy/cloud-run/#gcloud-cli), and add `vijil-dome` to your agent's `requirements.txt` file. When deploying, ensure you use a container size that is sufficiently large. We recommend `--cpu=4 --memory=8Gi`

> ⚠️ Deploying directly via the ADK CLI is not supported as there is no way yet to provide explicit requirements or adjust the container image size via the ADK CLI. The default container size of 1 CPU and 512 MB memory is insufficient for Dome's default configuration. We recommend 4 CPUs and 8Gi memory.

> ⚠️ Dome uses the `annoy` package for a fast embeddings store. Unfortunately, `annoy` is not currently compatible with agents built using Google ADK + Cloud Run. Use the default in-memory option if embeddings-based detectors need to be used. `annoy` can be installed via the optional `embeddings` extra, so for most default configurations of Dome, this should not matter.

For a more comprehensive walkthrough of how to guard a multi-agent ADK setup with Dome, and deploy it, check out [this blog post](https://www.vijil.ai/blog/protecting-google-adk-agents-with-vijil-dome). 