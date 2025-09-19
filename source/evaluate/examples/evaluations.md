# Working with Evaluations

You can create, view, summarize, export, cancel, and delete evaluations with the Vijil Python client.

Before doing any of this, you'll need to [instantiate](run-your-first-test.md) your Vijil client. In this topic we'll assume you've instantiated a Vijil client called `client`.

## Create an evaluation

You can use the `evaluations.create` method to create an evaluation:


```python
client.evaluations.create(
    model_hub="openai",
    model_name="gpt-4o-mini",
    model_params={"temperature": 0},
    harnesses=["security"],
    harness_params={"is_lite": False}
)
# If successful, returns dictionary with the following format:
# {'id': YOUR_GUID, 'status': 'CREATED'}
```

The relevant parameters are as follows:

- `model_hub`: The model hub your model is on. Currently we support `openai`, `octo`, and `together` as model hubs. Make sure you have an API key [stored](api-keys.md) for the hub you want to use.
- `model_name`: The name of the model you want to use on the hub. You can get this from the relevant hub's documentation.
- `model_params`: Inference parameters like temperature and top_p.
- `harnesses`: [Harnesses](../../components/harnesses.md) determine which probes you want to run, which determines what makes up your trust score.
- `harness_params`: `is_lite` determines whether you're running a "light" version of the harness, which will be cheaper and faster. Set this to `False` if you want to run the full harness.


## View, describe, and summarize evaluations

### List evaluations

List all evaluations with the `evaluations.list` method:

```python
client.evaluations.list(limit=20)
```
If you do not specify `limit`, it will return only the 10 most recent evaluations.

If you do not know an evaluation ID, the `list` method lets you find out the ID, which you need in order to get more details about that evaluation.

### Get evaluation status

You can view the status of an evaluation with the `evaluations.get_status` method:

```python
client.evaluations.get_status(evaluation_id='96f925f6-a7a7-05dd-5f2a-665734d181ee')
```

### Summarize a completed evaluation

Get summary scores for a completed evaluation, including scores at the overall, harness, scenario, and probe levels, with the `evaluations.summarize` method:

```python
client.evaluations.summarize(evaluation_id='22df0c08-4fcd-4e3d-9285-3a5e66c93f54')
```


### Get prompt-level details

Get prompt-level details for a completed evaluation with the `evaluations.describe` method:

```python
client.evaluations.describe(evaluation_id='22df0c08-4fcd-4e3d-9285-3a5e66c93f54', format='dataframe', limit=1000)
```

This returns all prompts and detector scores for each probe. By default, it will return only 1000 results, but you can change this with the `limit` argument.

By default, the output is a pandas dataframe, but if you prefer a list of dictionaries, specify `list` as the `format`.

#### Get a list of hits only

If you want a list of only the prompts/responses that led to hits (responses deemed undesirable), you can use the `hits_only` argument. By default, all prompts and responses will be returned.

```python
client.evaluations.describe(evaluation_id='22df0c08-4fcd-4e3d-9285-3a5e66c93f54', format='dataframe', hits_only=True)
```

## Export evaluations

You can export both the [summary](#summarize-a-completed-evaluation)- and [prompt-level](#get-prompt-level-details) evaluation results.

### Export summary

Export the summary of an evaluation with the `evaluations.export_summary` method:

```python
client.evaluations.export_summary(evaluation_id='96f925f6-a7a7-05dd-5f2a-665734d181ee', format='pdf', output_dir='./output')
```

The format can be either `pdf` or `html`. `output_dir` defaults to the current directory unless otherwise specified.

### Export prompt-level details

Export the prompt-level details of an evaluation with the `evaluations.export_report` method:

```python
client.evaluations.export_report('33a886cd-2183-4a61-9ede-241cbbb10ec6', format='parquet', output_dir='./output')
```

The format can be `csv`, `parquet`, `json` or `jsonl`. `output_dir` defaults to the current directory unless otherwise specified.

See the [glossary](../../glossary/index.md) to understand what the probe or detector modules in the report do.

#### Export hits only

To export only the prompts/responses that led to hits (responses deemed undesirable), you can use the `hits_only` argument. By default, all prompts and responses will be returned.

```python
client.evaluations.export_report(evaluation_id='22df0c08-4fcd-4e3d-9285-3a5e66c93f54', format='csv', hits_only=True)
```

## Cancel or delete evaluations

You can cancel an in-progress evaluation or delete evaluations to unclutter your dashboard.

### Cancel an evaluation

Cancel an in-progress evaluation with the `evaluations.cancel` method:

```python
client.evaluations.cancel(evaluation_id='ecc4139a-bb07-4e04-8f0f-b402c1e5cb65')
# {'type': 'CANCEL_EVALUATION',
#  'id': 'dc3d4e6c-041d-41a6-8115-674cf2496718',
#  'created_at': 1721163830.4333143,
#  'created_by': '',
#  'data': {'evaluation_id': 'ecc4139a-bb07-4e04-8f0f-b402c1e5cb65'},
#  'metadata': None}
```

### Delete an evaluation

Delete an evaluation with the `evaluations.delete` method:

```python
client.evaluations.delete(evaluation_id='bb8ad49b-4d49-462f-8abb-cbdbc0b1998d')
# {'type': 'DELETE_EVALUATION',
#  'id': 'a67e1b5e-83fb-4aa5-9cbb-bd057fb4db4f',
#  'created_at': 1721163723.7307427,
#  'created_by': '',
#  'data': {'evaluation_id': 'bb8ad49b-4d49-462f-8abb-cbdbc0b1998d'},
#  'metadata': None}
```

