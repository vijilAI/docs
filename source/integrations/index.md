# Integrations

Vijil Evaluate is integrated with a number of leading LLM providers.

To evaluate serverless LLM endpoints hosted on any of these, follow directions in the [quickstart tutorial](../quickstart.md), but with different values for
the model hub and model name.

| Provider | `model_hub` | `model_name` |
|---|---|---|
| OpenAI | `openai` | [List of Models](https://platform.openai.com/docs/models) |
| Together AI | `together` | [List of Models](https://docs.together.ai/docs/serverless-models) |
| Mistral AI | `mistral` | [List of Models](https://docs.mistral.ai/getting-started/models/models_overview) |
| Fireworks AI | `fireworks` | [List of Models](https://fireworks.ai/models?infrastructure=serverless) |
| NVIDIA NIM | `nvidia` | [List of Models](https://docs.api.nvidia.com/nim/reference/llm-apis) |


We also support a number of cloud services, give you the flexibility of evaluating agents accessible through custom endpoints.

```{eval-rst}
.. toctree::
   :maxdepth: 1

   vertex
   digitalocean
   bedrock
   custom
```
