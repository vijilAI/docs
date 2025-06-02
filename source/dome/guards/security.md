# Security

Security guards block against malicious prompts that attempt to cause the LLM to break its intended behaviour and guidelines. We currently support methods that aim to detect prompt injections, and jailbreak attacks. Security methods should typically be used in input guardrails.

The table below lists the security methods we currently support. The `ID` column should be used to use the detection method in a config. 

| Name    | ID | Description |
| -------- | ------- | ------- |
| [Vijil Prompt Injection MBert Classifier](#vijil-prompt-injection-classifier-prompt-injection-mbert) | `prompt-injection-mbert` | Vijil's Finetuned Modern-BERT classifier for prompt injections and jailbreaks |
| [ProtectAI Prompt Injection Classifier](#prompt-injection-classifier-prompt-injection-deberta-v3-base) | `prompt-injection-deberta-v3-base` | Finetuned Deberta model to detect prompt injections and jailbreaks |
| [Meta LLama PromptGuard](#meta-promptguard-security-promptguard) | `security-promptguard` | Meta-Llama PromptGuard model to detect malicious jailbreaks and prompt injection attacks |
| [Security Prompt Engineering](#security-prompt-engineering-security-llm)| `security-llm` |  Detect jailbreaks and prompt injection attacks via LLM prompt engineering |
| [Length-Per-Perplexity Heuristic](#length-per-perplexity-heuristic-jb-length-per-perplexity) | `jb-length-per-perplexity` | Heuristic-driven jailbreak detection algorithm |
| [Prefix-Suffix-Perplexity Heuristic](#prefix-suffix-perplexity-heuristic-jb-prefix-suffix-perplexity) | `jb-prefix-suffix-perplexity` | Another heuristic-driven jailbreak detection algorithm |
| [Security Embeddings](#security-embeddings-security-embeddings)| `security-embeddings` | Embeddings-based jailbreak and prompt injection detector |


---

### Vijil Prompt Injection Classifier (`prompt-injection-mbert`)

This is a [finetuned modern-BERT model](https://huggingface.co/vijil/mbert-prompt-injection), developed by Vijil that detects jailbreaks and prompt injection attacks. This model is enabled by default for security and in our internal testing, is the best performing low-latency model we've found for prompt injection attacks. Enabled in Dome's default configuration.

**Parameters**

- **truncation** (optional boolean): Determines if the model input should be truncated. Default value is true.
- **max_length** (optional int): Maximum length of input string. Default value is 512.


### Prompt Injection Classifier (`prompt-injection-deberta-v3-base`)

This is a [finetuned deberta-v3-base model](https://huggingface.co/protectai/deberta-v3-base-prompt-injection) developed by Protect AI, intended to be a classifier for detecting jailbreaks and prompt injection attacks.

**Parameters**

- **truncation** (optional boolean): Determines if the model input should be truncated. Default value is true.
- **max_length** (optional int): Maximum length of input string. Default value is 512.

### Meta PromptGuard (`security-promptguard`)

[Meta's PromptGuard 86M model](https://huggingface.co/meta-llama/Prompt-Guard-86M). This is a multiligual DeBERTa model finetuned to detect malicious jailbreaks and prompt injections.
````{Note}
PromptGuard is a gated model and requires access. Request access here: https://huggingface.co/meta-llama/Prompt-Guard-86M
Once you request access, you will need to set your HuggingFace token in your environment, or sign in via HF's CLI to be able to download and use the model.
````

**Parameters**

- **score_threshold** (optional float): The threshold for a prompt injection. Default value is 0.5. Values greater than or equal to this threshold will be flagged.
- **truncation** (optional boolean): Determines if the model input should be truncated. Default value is true.
- **max_length** (optional int): Maximum length of input string. Default value is 512.

### Security Prompt Engineering (`security-llm`)

A detector that uses custom prompt engineering to determine if the query string is a prompt-injection or jailbreak attempt.

**Parameters**

- **hub_name** (optional str): The hub that hosts the model you want to use. Currently supports OpenAI (`openai`) and Together (`together`). Default value is `openai`.
- **model_name** (optional str): The model that you want to use. Default value is `gpt-4o`. Please ensure that the model you wish to use is compatible with the hub you selected. When using models from Together, ensure the model starts with `together_ai` as per LiteLLM's documentation.
- **api_key** (optional str): Specify the API key you want to use. By default, this is None, and the API key is pulled directly from the environment variables. The environment variables used are `OPENAI_API_KEY`, and `TOGETHERAI_API_KEY`.

### Length-Per-Perplexity Heuristic (`jb-length-per-perplexity`)

This method uses a heuristic based on perplexity outputs of GPT-2 and the length of a query string to determine if a prompt is a possible jailbreak attack. See [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/user_guides/guardrails-library.html#jailbreak-detection-heuristics) for additional details.

**Parameters**

- **stride_length** (optional int): Stride of the LLM. Default value is 512.
- **threshold** (optional float): the threshold of the heuristic. A string with a score higher than the threshold is classified as a jailbreak. Default value is 89.79.

### Prefix-Suffix-Perplexity Heuristic (`jb-prefix-suffix-perplexity`)

Similar to the previous method, this method uses a hueristic based on the perplexity of the first and last 20 words of a query. See [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/user_guides/guardrails-library.html#jailbreak-detection-heuristics) for additional details.

**Parameters**

- **stride_length** (optional int): Stride of the LLM. Default value is 512.
- **prefix_threshold** (optional float): The threshold for prefix perplexity. Any query string with a prefix threshold higher than this is flagged as a jailbreak attempt. Default value is 1845.65.
- **suffix_threshold** (optional float): The threshold for suffix perplexity. Any query string with a suffix threshold higher than this is flagged as a jailbreak attempt. Default value is 1845.65.
- **prefix_length** (optional int): The number of words to consider in the prefix. If this is larger than the number of words in the query string, the max length of the query string is used. Default value is 20.
- **suffix_length** (optional int): The number of words to consider in the suffix. If this is larger than the number of words in the query string, the max length of the query string is used. Default value is 20.

### Security Embeddings (`security-embeddings`)
Creates an embeddings index using the garak-in-the-wild-jailbreaks dataset.

**Parameters**

- **engine** (optional str): The engine to perform the embeddings. We currently support `SentenceTransformer` and `FastEmbed`. Default value is `SentenceTransformer`.
- **model** (optional str): The embedding model to use. Default value is `all-MiniLM-L6-v2`.
- **threshold** (optional float. The default similarity threshold. If the similarity between a query and its nearest neighbour is greater than or equal to this value, the query is flagged. Default value is 0.8.
- **in_mem** (optional boolean): Keep the index in memory via a Pandas dataframe (if true) or via Annoy (if False). (Note: Annoy appears to have some instability on Windows environments, and does not work with agents deployed via Google Cloud Run). Default value is true.
