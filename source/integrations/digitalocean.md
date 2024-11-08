# DigitalOcean

If you are building an agent on the [DigitalOcean GenAI platform](https://www.digitalocean.com/products/gen-ai), Vijil Evaluate can help you evaluate it before going to production.

To set up an agent on DigitalOcean, follow the instructions [here](https://docs.digitalocean.com/products/genai-platform/getting-started/quickstart/).


## Store Credentials

Once you have an agent set up, follow the instructions [here](https://docs.digitalocean.com/products/genai-platform/how-to/manage-ai-agent/use-agent/) to fetch the credentials `data-agent-id` and `data-chatbot-id` to access that agent through an API, as well as the agent endpoint.

Now log into Vijil Evaluate, and navigate to **Keys > Add new key**. From the Model Hub dropdown, select *DigitalOcean* as your chosen hub, and add the above information in the respective fields.

![DigitalOcean Hub Config | 60%](../_static/image-do.png)


Give the API key configuration a name, save it, and you're ready to go!

To add the credentials using the python client, you need to supply the fields inside the `hub_config` argument.
````{tab} Python
```python
client.api_keys.create(
    name="digitalocean-test",
    model_hub="digitalocean",
    hub_config={
        "agent_id": "abc-xyz",
        "agent_key": "xyz-123"
    }
    rate_limit_per_interval=60, # optional
    rate_limit_interval=60 # optional
)
```

## Run an Evaluation

To run an evaluation from the UI, simply select *DigitalOcean* as the Model Hub, then paste the agent endpoint as the *Model URL*.

To run an evaluation using the Python client, use the following code pattern, with the agent API as `model_url` and a harness of your choice.

````{tab} Python
```python
client.evaluations.create(
    model_hub="digitalocean",
    model_url="https://agent-xxx.ondigitalocean.app/api/v1",
    model_params={"temperature": 0},
    harnesses=["hallucination"]
)
```
````