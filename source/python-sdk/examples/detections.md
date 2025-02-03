# Working with Detections

Evaluations tightly couple detectors with probes, using a detector only to evaluate responses from
the prompts in probes that use that detector. We offer a detection endpoint to run the detectors in a more atomic manner.
Using this functionality, a user can evaluate their preferred payload using our detectors, as long as the payload has the
fields required fields to run a detector.

You can create, view, and summarize detections with the Vijil Python client.

## List Detectors

List all supported detectors with the `detections.list_detectors` method:

```python
client.detections.list_detectors()
```

## Create Detections

You can use the `detections.create` method to run a detector on a list of inputs.


```python
client.detections.create(
    detector_id = "llm.AnswerRelevancy",
    detector_inputs = [
        {"question": "How do I tie my shoes?", "response": "To tie your shoes you should first use your laces."},
        {"question": "How do I tie my shoes?", "response": "George washington was the first president of the USA."}
    ]
)
# If successful, returns dictionary with the following format:
# {'id': YOUR_GUID, 'status': 'CREATED'}
```

The relevant parameters are as follows:

- `detector_ids`: Identifier for the detector to be called. A full list of detectors is available [here](../../glossary/detectors.md).
- `detector_inputs`: List of dicts supplying structured payload to the detector. Keys to the dicts should map to [permitted input fields](#supported-fields-for-detectors) for that detector.
- `detector_params`: You can use LLM-based detectors with non-default LLMs by supplying a dictionarity with (1) a hub name, (2) model name, and (3) the name of an API key for that hub you have saved in Evaluate.

Below is an example for the use of `detector_params`. Suppose you want to use Llama 3.3 70B Instruct on Together as an evaluator LLM for the answer relevancy metric (it uses gpt-4o on OpenAI by default). Given you have a Together API key saved, you can use the following code

```python
client.detections.create(
    detector_id = "llm.AnswerRelevancy",
    detector_inputs = [
        {"question": "How do I tie my shoes?", "response": "To tie your shoes you should first use your laces."},
        {"question": "How do I tie my shoes?", "response": "George washington was the first president of the USA."}
    ],
    detector_params = {
        "hub": "together",
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo"
    }
)
```


## Summarize Detections

Get summary scores for a completed detection, including status and related metadata with the `detections.describe` method:

```python
client.detections.describe(detection_id='22df0c08-4fcd-4e3d-9285-3a5e66c93f54')
```

Takes the optional argument `format`. Permitted values are `dataframe` (default), and `list`, which return a pandas data frame and list of dicts, respectively.

## Supported fields for Detectors

The table below gives the required set of input fields for each detector.

| Detector ID | Required fields: format |
|---|---|
| `goodside.Glitch` | `response`: str,`triggers`: list[str] |
| `base.TriggerListDetector` | `response`: str,`triggers`: list[str] |
| `base.TriggerListAbsenceDetector` | `response`: str,`triggers`: list[str] |
| `privateinfo.LeakPII` | `response`: str,`triggers`: list[str] |
| `encoding.DecodeMatch` | `response`: str,`triggers`: list[str] |
| `winobias.TriggerPlusAmbiguity` | `response`: str,`triggers`: list[str] |
| `mitigation.TriggerAbsenceWithRefusal` | `response`: str,`triggers`: list[str] |
| `mitigation.mathLatexSympy.MathLatexSympy` | `response`: str,`triggers`: list[str] |
| `instructionFollowing.InstructionFollowing` | `response`: str,`instructions`: list[str], `kwargs`: list[dict] |
| `toolcalling.ToolCorrectness` | `response`: str,`expected_tools`: list[str] |
| `nlp.BLEU` | `response`: str,`ground_truth`: str |
| `nlp.METROR` | `response`: str,`ground_truth`: str |
| `nlp.BERTScore` | `response`: str,`ground_truth`: str |
| `llm.AnswerRelevancy` | `response`: str,`question`: str |
| `llm.ContextualPrecision` | `question`: str,`ground_truth`: str,`contexts`: list[str] |
| `llm.ContextualRecall` | `ground_truth`: str,`contexts`: list[str] |
| `llm.Faithfulness` | `response`: str,`question`: str,`contexts`: list[str] |
| `llm.StrongReject` | `response`: str,`forbidden_prompt`: str |
| `llm.ConversationRoleAdherence` | `response`: str,`role`: str |
| `llm.PolicyViolation` | `response`: str,`input`: str,`policy`: str |
| All other detectors | `response`: str |
