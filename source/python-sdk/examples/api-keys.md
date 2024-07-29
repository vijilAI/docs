# Managing API keys

In order to query a model for responses, you need to have one or more model hub API keys stored in Vijil. Currently, we support OpenAI, Octo, and Together as model hubs.

Before doing any of this, you'll need to [instantiate](run-your-first-test.md) your Vijil client. In this topic we'll assume you've instantiated a Vijil client called `client`.

## List available API keys

This lists all the model hub API keys you've added to Vijil, along with their metadata like rate limits

```python
client.api_keys.list()
```

## Add an API key

```python
client.api_keys.create(name="openAI20240630-2", model_hub="openai", api_key="sk+++")
```

## Delete an API key

```python
client.api_keys.delete(name="openAI20240630-2")
```

## Modify an API key

You can use this to update any property of an API key except for its name. To update its name, use the `rename` function instead.

The following example updates the API key value and rate limit properties for the key with name `openAI20240630-2`:

```python
client.api_keys.modify(name="openAI20240630-2", api_key="sk---", rate_limit_interval=1, rate_limit_per_interval=5)
```

## Rename an API key

Use this to update the name of an API key.

```python
client.api_keys.rename(name="openAI20240630-2", new_name="openAI20240630-3")
```

