# Integrating Vijil Evaluate into CI/CD

You can use Vijil Evaluate to automatically run evaluations as part of your CI/CD pipeline. To do that, you'll need to obtain machine-to-machine secrets and use those to get and refresh authentication tokens. This is necessary because the regular user token expires every 24 hours.

## Obtaining Machine-to-Machine Secrets

You must be logged in as an admin in your team to obtain machine-to-machine secrets. In the Vijil web interface, click on your profile icon in the lower left. Here, you can view and rotate your long-lived machine-to-machine secrets. These can be viewed only once and must be rotated after the initial viewing.

Click **View long-lived token** to view the secrets. This option is available if they haven't been viewed yet.

If someone else in the team has already viewed them, you will have to rotate the secrets. Click **Rotate long-lived token** to rotate the secrets, then click **View long-lived token** to view the new secrets.

The secrets displayed are the Client ID, Client Secret, and Client Token. Save these as variables in an environment file. Sample environment file:

```
M2M_CLIENT_ID="hh2YrR8beOYUC0RW"
M2M_CLIENT_SECRET="soSUWyOLkGS3Xyu28xpUhw6XIMPePTEV"
M2M_CLIENT_TOKEN="a940e6ac20541a92300c6dfd57e08438a4f699067f5c9bf66c8b2a8d15acebd5"
```

## Obtaining an Authentication Token

To use the Vijil Python SDK to run CI/CD scripts, you'll need to use the long-lived secrets to obtain an authentication token. To do so, you send a POST request to the token endpoint. The following Python snippet shows how to do so, assuming you have saved the secrets to an `.env` file like the one above.

````{tab} Python
```python
    import requests
    import os
    from dotenv import load_dotenv
    
    # Load environment variables. Specify the file path to your .env file if it's not in the current directory.
    load_dotenv()
    
    # Get credentials from environment
    client_id = os.getenv("M2M_CLIENT_ID")
    client_secret = os.getenv("M2M_CLIENT_SECRET")
    client_token = os.getenv("M2M_CLIENT_TOKEN")

    # Step 1: Prepare the request payload
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "client_token": client_token
    }
    

    # Step 2: Make POST request to token endpoint
    base_url="https://evaluate-api.vijil.ai"
    response = requests.post(f"{base_url}/v1/auth/token", json=payload)
    response.raise_for_status()  # Raise error if request failed
    
    # Step 3: Extract access token from response
    token_data = response.json()
    simple_access_token = token_data['access_token']
    print(simple_access_token)
```
````

## Save the Access Token to Your Envionrment

Now you can use `simple_access_token` to authenticate requests to the Vijil Evaluate API. Save it as `VIJIL_API_KEY` in your environment file and you can run the code samples in our [Quickstart](../../quickstart.md) or [other tutorials](index.md).

The access token expires after 24 hours, so you should use the above script to refresh it if you are making API calls more than 24 hours apart.
