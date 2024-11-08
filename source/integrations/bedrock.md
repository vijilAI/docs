# AWS Bedrock

You can evaluate LLMs, accessed as RESTful APIs on Amazon Bedrock, using Vijil Evaluate. To do so, first
set up a [Bedrock Access Gateway](https://github.com/aws-samples/bedrock-access-gateway).

You can then [add an API key](../python-sdk/examples/api-keys.md#add-an-api-key) using the UI or the python client.

## Run an Evaluation

To run an evaluation from the UI, simply select *Bedrock* as the Model Hub, then paste your custom endpoint as the *Model URL*,
and select a *Model Name from the dropdown.

To [run an evaluation using the Python client](../python-sdk/examples/evaluations.md), use the following code pattern, with your custom endpoint as `model_url`, model name as `model_name`, and a harness of your choice.

````{tab} Python
```python
client.evaluations.create(
    model_hub="bedrock",
    model_url="https://your_model_url",
    model_name="anthropic.claude-v2",
    model_params={"temperature": 0},
    harnesses=["hallucination"],
)
```
````

