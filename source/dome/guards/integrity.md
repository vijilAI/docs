# Integrity

Integrity methods evaluate query strings based on some available context to check for possible hallucinations and ungrounded or incorrect conclusions. Integrity methods will typically only apply to output guards in RAG-based applications.

All integrity models support **context** as a parameter where the context for the detector can be initialized. 

````{warning}
Integrity methods are currently experimental! 
````

The table below lists the integrity methods we currently support. The `ID` column should be used to use the detection method in a config. 

| Name    | ID | Description |
| -------- | ------- | ------- |
| [HHEM](#hhem-hhem-hallucination)  | `hhem-hallucination`    | Classifier to detect hallucinations |
| [Hallucination Prompt Engineering](#hallucination-prompt-engineering-hallucination-llm) | `hallucination-llm` | Detect hallucinations via LLM prompt engineering |
| [Fact-Check Classifier](#fact-check-classifier-fact-check-roberta) | `fact-check-roberta` | Roberta Model for fact-checking | 
| [Fact-Check Prompt Engineering](#fact-check-prompt-engineering-fact-check-llm) | `fact-check-llm` | Fact-checking via LLM prompt engineering |


---


### HHEM (`hhem-hallucination`)
Uses the [HHEM Model](https://huggingface.co/vectara/hallucination_evaluation_model) to determine if there might be possible model hallucinations where the provided context does not support the query claim or hypothesis.

**Parameters**

- **context** (optional str): Sets the initial context.
- **factual_consistency_score_threshold**   (optional float): The factual consistency score threshold.
**Important**: any input where the factual consistency score is _lower_ than the threshold is classified as a possible hallucination. Default value is 0.5.
- **trust_remote_code** (optional bool): Whether remote code should be trusted. This must be set to true in order to use HHEM. Defaults to true. 

### Hallucination Prompt Engineering (`hallucination-llm`)
Uses a prompt template outlined in [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/user_guides/guardrails-library.html#hallucination-detection) to detect hallucinations given a context and hypothesis.

**Parameters**

- **context**  (optional str): Sets the initial context.
- **hub_name** (optional str): The hub that hosts the model you want to use. Currently supports OpenAI (`openai`) and Together (`together`). Default value is `openai`.
- **model_name** (optional str): The model that you want to use. Default value is `gpt-4o`. Please ensure that the model you wish to use is compatible with the hub you selected. When using models from Together, ensure the model starts with `together_ai` as per LiteLLM's documentation.
- **api_key** (optional str): Specify the API key you want to use. By default, this is None, and the API key is pulled directly from the environment variables. The environment variables used are `OPENAI_API_KEY`, and `TOGETHERAI_API_KEY`.

### Fact-Check Classifier (`fact-check-roberta`)
Uses a [fine-tuned RoBERTa model](https://huggingface.co/Dzeniks/roberta-fact-check) to detect possible factual inconsistencies by examining the joint encoding of a context string and a query string and classifying if the context supports or refutes the claim. 

**Parameters**


- **context**  (optional str): Sets the initial context.

### Fact-Check Prompt Engineering (`fact-check-llm`)
Uses a prompt template outlined in [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/user_guides/guardrails-library.html#fact-checking) to detect if a claim is grounded in some context. 

**Parameters**

- **context**  (optional str): Sets the initial context.
- **hub_name** (optional str): The hub that hosts the model you want to use. Currently supports OpenAI (`openai`) and Together (`together`). Default value is `openai`.
- **model_name** (optional str): The model that you want to use. Default value is `gpt-4o`. Please ensure that the model you wish to use is compatible with the hub you selected. When using models from Together, ensure the model starts with `together_ai` as per LiteLLM's documentation.
- **api_key** (optional str): Specify the API key you want to use. By default, this is None, and the API key is pulled directly from the environment variables. The environment variables used are `OPENAI_API_KEY`, and `TOGETHERAI_API_KEY`.
