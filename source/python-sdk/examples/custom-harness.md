# Create a Custom Harness

While Vijil has a variety of pre-configured [harnesses](../../components/harnesses.md) that you can select from, you can also create your own harnesses in order to obtain a trust score specific to your organization.

The following example assumes that you have already initialized a Vijil [client](run-your-first-test.md) named `client`.

## Policy Document(s)

You can create a custom policy adherence harness that checks whether your model adheres to its system prompt or an organizational policy. To do this, you need a system prompt specified as a string, and an optional organizational policy provided as a `.txt` or `.pdf` file. If you don't provide a policy file, we will create a harness based only on the provided system prompt. To specify that you want a policy adherence harness, you need to specify the `category` argument as `["AGENT_POLICY"]`.

The following examples uses the `harnesses.create` function to create a harness to test adherence against the NIST [AI Risk Management](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) framework.

```python
harness_creation_job = client.harnesses.create(
    harness_name="NIST AI RMF harness",
    system_prompt="You are a helpful assistant.", 
    policy_file_path="nist.ai.100-1.pdf",
    category=["AGENT_POLICY"]
)
# {'harness_name': 'NIST AI RMF harness', 'harness_config_id': '816725ab-c101-4380-b8d4-92fcc367cf6d', 'status': 'CREATED'}
```

You can use the `get_status` command to know the status of a harness creation job.

```python
client.harnesses.get_status(harness_id=harness['harness_config_id'])
# {'created_by': 'f6e0b128-c075-4bc3-91da-34d03fa6c67e',
#  'created_at': 1741819347,
#  'id': '654289d2-d4c4-40fb-b893-120ab3978a69',
#  'harness_config_id': '85482e8b-a8b4-4cac-a4a2-92b4f4f6e56e',
#  'harness_name': 'NIST AI RMF harness',
#  'team_id': '00ccc042-1b41-4f02-ae5f-6a09b5e6e844',
#  'status': 'COMPLETED',
#  'status_message': 'Harness NIST AI RMF harness updated successfully!',
#  'agent_system_prompt': 'you are a helpful assistant',
#  'started_at': None,
#  'completed_at': None,
#  'harness_config_version': '1.0.0'}
```

The `harness_config_version` starts at 1.0.0 for any harness of the given harness name. If you create another harness with the same name, vijil automatically increments the harness version, e.g. from 1.0.0 to 1.0.1. In the above example, we assume that `NIST AI RMF harness` is a new harness name, so we set the version to 1.0.0.

Once the harness is created, you can [run an evaluation](evaluations.md#create-an-evaluation) with it:

```python
client.evaluations.create(
    harnesses=[harness_creation_job['harness_config_id']],
    model_hub=your_model_hub,
    model_name=your_model
)
```

## Knowledge Base
If you are developing a RAG agent and would like to generate a custom test harness to evaluate generation and retrieval capabilities based on a set of document chunks, upload the documents that you'd like to base the evaluation on into a GCP storage bucket and use the following command. To specify that you want a RAG harness, set the `category` parameter to `["KNOWLEDGE_BASE"]`.

```python
harness_creation_job = client.harnesses.create(
    harness_name="Your KB harness",
    system_prompt="You are a RAG agent that answers questions based on a knowledge base.", 
    kb_bucket="your_bucket_name",
    category=["KNOWLEDGE_BASE"]
)
```

## Tool Calling Agent
To evaluate a tool calling agent, you need to supply input and output schemas for a function that you want to generate test prompts based on, as well as an endpoint to call that function. To specify that you want a tool calling harness, set the `category` parameter to `["FUNCTION_ROUTE"]`.

```python
harness_creation_job = client.harnesses.create(
    harness_name="Your tool calling harness",
    system_prompt="You are a calculator agent that calls a function to calculate the sum of two numbers.", 
    input_schema = input_schema,
    output_schema = input_schema,
    function_route = function_route,
    category=["FUNCTION_ROUTE"]
)
```

## Custom Harness with Multple Components

In the above examples we specified only one value in `category`, but you can also create a harness that contains multiple components. For example, you can create a harness that contains a knowledge base component and a tool calling agent component, or any of those components together with a policy adherence component. To do this, specify multiple values in `category`. For example, to create a harness with all three components, use `category=["KNOWLEDGE_BASE", "FUNCTION_ROUTE", "POLICY_ADHERENCE"]`.