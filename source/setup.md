# Setup

This section will guide you through the process of preparing your development environment to use Vijil cloud services.

Set up [Vijil Evaluate](#vijil-evaluate) to measure your system's trustworthiness, or [Vijil Dome](#vijil-dome) to protect your agent.

## Vijil Evaluate

To run evaluation jobs through the Vijil Evalute API and interact with the results, you need to install the client library that provides the necessary functionalities. You can do so through downloading the library from PyPI.

````{tab} Shell
```bash
pip install -U vijil
```
````

To ensure you are using the latest version of the package, we recommend using the `-U` or `--upgrade` option.

### Authentication using API Keys

You need a Vijil API key to authenticate remotely through the client library. You can obtain the API key by logging into your
Vijil account, going to the profile page on the dashboard, then copying the value in the **Token** field.

![API Token Location | 80%](_static/token-generation.png)

After your obtain an API key, you can export it in the environment you intend to use the client inside.

````{tab} Shell
```bash
export VIJIL_API_KEY = <eyj-xxxx>
```
````

Alternatively, you can store the key in a `.env` file and load it into your Python environment using a library such as [python-dotenv](https://pypi.org/project/python-dotenv/).


## Vijil Dome

Vijil Dome is an [open-source library](https://github.com/vijilAI/vijil-dome) that provides input and output guardrails for your AI agents. You can install it from PyPI:

````{tab} Shell
```bash
pip install vijil-dome
```
```

After installation, you can quickly test Dome with a [sample input](dome/gettingstarted.md#basic-usage).