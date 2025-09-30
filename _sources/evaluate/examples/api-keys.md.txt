# Managing API keys

To query a model for responses, you need to have one or more model hub API keys stored in Vijil. Currently, we support OpenAI and Together as model hubs. You can also add [custom hubs](../../integrations/custom.md), including [Google Vertex AI](../../integrations/vertex.md) and [DigitalOcean](../../integrations/digitalocean.md). You can create an API key while [adding an agent](agents.md), or create it separately.

## Create, Delete, or Update API Keys in Vijil Web Interface

In the left sidebar, click on **Keys**. You'll see a list of all the model hub API keys you've added to Vijil, along with their metadata like rate limits. Click **Add new key** to create a new API key. 

Any keys you create can later be specified as the key for an [agent](agents.md) you create.

## Create, Delete, or Update API Keys in the Python Client

Before doing any of this, you'll need to [instantiate](../../quickstart.md) your Vijil client. In this topic we'll assume you've instantiated a Vijil client called `client`.

### List available API keys

This lists all the model hub API keys you've added to Vijil, along with their metadata like rate limits:

```python
client.api_keys.list()
```

### Add an API key

When adding an API key, you must specify the model hub it's for, the name you want to give it, and the API key value.

You can also specify a rate limit for the API key, which defines the maximum number of requests to send to model endpoint per unit of time. The `rate_limit_interval` is the number of seconds in the interval, and `rate_limit_per_interval` is the number of requests you can make in that interval. In the example below, we are specifying a limit of 600 requests per 60 seconds, i.e. 600 requests per minute.

```python
client.api_keys.create(
    name="openAI20240630-2", 
    model_hub="openai", 
    api_key="sk+++", 
    rate_limit_per_interval=600, # optional, defaults to lowest requests-per-minute
    rate_limit_interval=60, # optional, defaults to 60 seconds
)
```
If you don't define a rate limit, Vijil defaults to the lowest tier rate limit offered by the model provider.

### Delete an API key

```python
client.api_keys.delete(name="openAI20240630-2")
```

### Modify an API key

You can use this to update any property of an API key except for its name. To update its name, use the `rename` function instead.

The following example updates the API key value and rate limit properties for the key with name `openAI20240630-2`:

```python
client.api_keys.modify(name="openAI20240630-2", api_key="sk---", rate_limit_interval=1, rate_limit_per_interval=5)
```

### Rename an API key

Use this to update the name of an API key.

```python
client.api_keys.rename(name="openAI20240630-2", new_name="openAI20240630-3")
```

