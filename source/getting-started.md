# Getting Started

Let's begin by preparing your environment.

## Installation

We first install libraries necessary to run Vijil services.

```bash
pip install vijil
```

## Model Providers

Vijil supports a number of LLM providers. If you want to use our tool on models deployed with them, make sure to create an account and have API keys handy for the respective provider.

* Anyscale
* Hugging Face
* Mistral
* OctoAI
* OpenAI
* Replicate
* Together

## Managing API Keys

We use environment variables for key management. You can export keys into environment variables through either CLI, or set them manually.

```bash
export KEY_NAME="key-string"
```

| Service | `KEY_NAME` |
|---|---|
| Vijil | `VIJIL_AUTH_TOKEN` |
| Anyscale | `ANYSCALE_API_TOKEN` |
| Hugging Face | `HF_INFERENCE_TOKEN` |
| Mistral | `MISTRAL_API_TOKEN` |
| OctoAI | `OCTO_API_TOKEN` |
| OpenAI | `OPENAI_API_TOKEN` |
| Replicate | `REPLICATE_API_TOKEN` |
| Together | `TOGETHER_API_TOKEN` |
| groq | `GROQ_API_TOKEN` |
| AWS | `AWS_API_TOKEN` |
| Microsoft | `MICROSOFT_API_TOKEN` |
| Google | `GOOGLE_API_TOKEN` |


Alternatively, you can store the API keys in a `.env` file that can be picked up by your Python client using [``python-dotenv``](https://pypi.org/project/python-dotenv/).
