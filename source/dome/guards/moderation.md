# Moderation

Moderation methods are aimed to catch offensive, hurtful, toxic or inappropriate content. They also provide support for catching content that might violate other policies such as containing words of phrases that should be banned.  Moderation methods can be used at both the input and output level. 


The table below lists the moderation methods we currently support. The `ID` column should be used to use the detection method in a config. 

| Name    | ID | Description |
| -------- | ------- | ------- |
| [FlashText Banlist](#flashtext-banlist-moderation-flashtext)  | `moderation-flashtext`  | Keyword/Phrase Banlist |
| [Llamaguard](#llamaguard-moderation-llamaguard) | `moderation-llamaguard` | Toxic content detector using Llamaguard 2 |
| [Moderation Prompt Engineering](#moderation-prompt-engineering-moderation-prompt-engineering) | `moderation-prompt-engineering` | Detect toxic content via LLM prompt engineering |
| [OpenAI Moderations API](#openai-moderations-api-moderations-oai-api) | `moderations-oai-api` | Detect toxic content using OpenAI's Moderation API |
| [Perspective API](#perspective-api-moderation-perspective-api) | `moderation-perspective-api` | Detect toxic content using the Perspective API |
| [Toxicity Classifier](#toxicity-classifier-moderation-deberta) | `moderation-deberta` | Finetuned Deberta model to detect toxicity |


---

### FlashText Banlist (`moderation-flashtext`)

Uses the [FlashText](https://github.com/vi3k6i5/flashtext) algorithm for fast keyword matching to block any string that contains a phrase or word that is present in a banlist.

**Parameters**

- **banlist_filepaths** (optional list[str]): A list of paths to text files that contain banned phrases. If not provided, a [default banlist](https://github.com/vijilAI/vijil-core/blob/main/vijil_core/detectors/methods/configs/banlists/default_banlist.txt) is used. 

### Llamaguard (`moderation-llamaguard`)

Meta’s Llamaguard 2 model for content moderation. Currently supported via an API call to the hosted LLM on OctoAI. Please ensure the `OCTO_API_KEY` is set before using this detection method.

**Parameters** (we _do not_ recommend changing them)

- **hub_name** (optional str): Default value is `octo`.
- **model_name** (optional str): Default value is `llamaguard-2-8b`.

### Moderation Prompt Engineering (`moderation-prompt-engineering`)

A detector that uses custom prompt-engineering to determine if the query string contains toxicity. Please ensure the `OPENAI_API_KEY` is set before using this method.

**Parameters**

- **hub_name** (optional str): The hub that hosts the model you want to use. Currently supports OpenAI (`openai`), Together (`together`) and Octo (`octo`). Default value is `openai`.
- **model_name** (optional str): The model that you want to use. Default: `gpt-4o`. Please ensure that the model you wish to use is compatible with the hub you selected. 
- **api_key** (optional str): Specify the API key you want to use. By default this is not specified and the API key is pulled directly from the environment variables. The environment variables used are `OPENAI_API_KEY`, `OCTO_API_KEY`, and `TOGETHER_API_KEY` for the corresponding hubs. 

### OpenAI Moderations API (`moderations-oai-api`)

Uses the latest text-moderation model from OpenAI to classify content for hate, harassment, self-harm, sexual content and violence. 

**Parameters**

- **score_threshold_dict** (optional dict[str : float]): Sets the per-category score threshold for each of the different toxicity dimensions. Scores above the threshold will be flagged as toxic. If unspecified, uses 0.5 as the default threshold for each category. If specified, is provided, only the categories in the dictionary are considered. For example, setting this to `{"violence" : 0.8, "self-harm" : 0.3}` will cause the method to ignore every category except violence and self-harm, setting their thresholds to 0.8 and 0.3 respectively. For a full list of the categories available, see [here](https://platform.openai.com/docs/guides/moderation/overview).

### Perspective API (`moderation-perspective-api`)

Uses Google Jigsaw's [Perspective API](https://www.perspectiveapi.com/) to detect toxicity.

**Parameters**

- **api_key** (optional str): Specify the API key you want to use. By default this is not specified and the API key is pulled directly from the environment variables. The environment variable used is `PERSPECTIVE_API_KEY`
- **attributes** (optional dict): We do not recommend changing this since it is required by the API. Default value is `{'TOXICITY':{}}`.
- **score_threshold_dict** (optional dict[str: float]): Provide a score threshold for the API. Values that cross the threshold are flagged by the detector. Default value is `{"TOXICITY": 0.5}`.

### Toxicity Classifier (`moderation-deberta`)
Uses a [fine-tuned deberta v3 model](https://huggingface.co/cooperleong00/deberta-v3-large_toxicity-scorer) to detect the presence of toxicity in text.

**Parameters** 

- **truncation** (optional boolean): The truncation strategy used by the model. Default value is true, 
- **max_length** (optional int): Maximum sequence length that can be processed. Default value is 208.
- **device** (optional str): The device to run on (`cuda` or `cpu`). By default uses CUDA if available, else CPU.
