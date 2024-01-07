# Getting Started

Let's begin by preparing your environment to run Vijil services.

## Installation

We begin by installing libraries necessary to run our services.

```bash
pip install autoredteam vijil_cli
```

## Model Providers

Vijil supports a number of LLM providers. If you want to use our tool on models deployed with them, make sure to create an account have API keys handy for the respective provider.

* Anyscale
* Cohere
* Hugging Face
* OctoAI
* OpenAI
* Replicate

## Managing API Keys

We use environment variables for key management. You can export keys into environment variables through either CLI, or set them manually.

```
export KEY_NAME="key-string"
```

<table><thead><tr><th width="306">Service</th><th>KEY_NAME</th></tr></thead><tbody><tr><td>Vijil</td><td><code>VIJIL_AUTH_TOKEN</code></td></tr><tr><td>Anyscale</td><td><code>ANYSCALE_API_TOKEN</code></td></tr><tr><td>Cohere</td><td><code>COHERE_API_TOKEN</code></td></tr><tr><td>Hugging Face</td><td><code>HF_INFERENCE_TOKEN</code></td></tr><tr><td>OctoAI</td><td><code>OCTO_API_TOKEN</code></td></tr><tr><td>OpenAI</td><td><code>OPENAI_API_TOKEN</code></td></tr><tr><td>Replicate</td><td><code>REPLICATE_API_TOKEN</code></td></tr></tbody></table>

Alternatively, you can store the API keys in a `.env` file that can be picked up by your Python client using the [`dotenv`](https://pypi.org/project/python-dotenv/) library.
