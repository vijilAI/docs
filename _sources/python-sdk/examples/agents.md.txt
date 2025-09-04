# Add, Update, and Delete Agents

This guide demonstrates how to manage agent configurations using the Vijil Python SDK. You can create, update, and delete agents programmatically. Creating an agent configuration is the first step in evaluating an agent.

After creating an agent configuration, you can [evaluate it](evaluations.md).

## Add (Create) an Agent

You can add an agent that uses an existing [API key](api-keys.md), or you can create a new API key and use it to add an agent.

### Basic Agent Creation with Existing API Key

Use the `api_key_name` parameter to specify the name of the API key you want to use.

```python
# Create an agent using an existing API key
response = client.agents.create(
    agent_name="my-openai-agent",
    hub="openai",
    api_key_name="my-openai-key",  # Use existing API key
    model_name="gpt-4o-mini",
    agent_system_prompt="You are a helpful AI assistant."
)
print(f"Created agent: {response}")
```

### Create Agent with New API Key

When creating an agent with a new API key, you should specify `api_key_value` and  all the required parameters for the API key, in addition to agent parameters.

The API key created this way will be automatically assigned a unique name based on the specified hub and the agent name.

```python
# Create an agent and automatically create a new API key
response = client.agents.create(
    agent_name="my-claude-agent",
    hub="anthropic",
    api_key_value="sk-ant-api03-...",  # Your actual API key
    model_name="claude-3-sonnet-20240229",
    agent_system_prompt="You are an expert code reviewer.",
    rate_limit_per_interval=50,
    rate_limit_interval=60
)
print(f"Created agent with new API key: {response}")
```

### Create Bedrock Agent with a new API key

Some model hubs require additional parameters for the agent that you specify in `hub_config`. See [Integrations](../../integrations/index.md) for more information on each supported hub and its parameters.

```python
# Create a Bedrock agent with specific configuration
response = client.agents.create(
    agent_name="my-bedrock-agent",
    hub="bedrockAgents",
    agent_id="ABCD1234",
    agent_alias_id="ALIAS123",
    hub_config={
        "region": "us-east-1",
        "access_key": "your-access-key",
        "secret_access_key": "your-secret-key",
        "agent_id": "ABCD1234",
        "agent_alias_id": "ALIAS123"
    }
)
print(f"Created Bedrock agent: {response}")
```

## List Agents

```python
# List all active agents
agents = client.agents.list()
print("Active agents:")
for agent in agents:
    print(f"- {agent.get('agent_name')} (Hub: {agent.get('hub')}, Model: {agent.get('model_name')})")
```

## Update an Agent

You can update an agent's name, model, hub, system prompt, URL,  and associated API key.

```python
# Update an existing agent's name and model
response = client.agents.update(
    agent_name="my-agent",  # Current agent name
    new_agent_name="updated-agent",  # New name
    model_name="updated-model",  # Updated model
    hub="updated-hub",  # Updated hub
    api_key_name="updated-api-key",  # Updated API key
    agent_url="updated-url",  # Updated URL
    agent_system_prompt="updated-system-prompt"
)
print(f"Updated agent: {response}")
```

## Delete  Agent

```python
# Delete an agent by name (archives the agent)
try:
    response = client.agents.delete(agent_name="my-openai-agent")
    print(f"Successfully deleted agent: {response}")
except ValueError as e:
    print(f"Error deleting agent: {e}")
```
