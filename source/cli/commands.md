# Commands

Below are the commands available in the Vijil CLI. In all commands except `help`, you can either input all options at once or enter them interactively after typing `vijil <command-name>` and pressing Enter.

## Help

To display all available commands in the CLI, use:

`vijil --help`

## Authenticate

### Login

To authenticate the CLI to your Vijil account, use:

`vijil login <username>`

> This command requires a Vijil access token created from the GUI.


**Arguments**

| Name | Possible values | Usage/Description
|--|---|---|
| `--token` | String | VIJIL access token from the GUI. |

**Example**

```console
$ vijil login admin --token my-token
```

### Logout

To log out from your Vijil account in the CLI, use:

`vijil logout`

**Example**

```console
$ vijil logout
```

## Create

### Token

To create tokens for interacting with the model hubs, use:

`vijil create token <model-hub>`

You can choose from the following hubs:
- `huggingface`
- `octo`
- `replicate`
- `openai`
- `together`
- `anyscale`
- `mistral`

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--name` | String | Name of token. |
| `--token` | String | Token from the model hub. |
| `--is-primary` | [yes\|no] | Save token as default (yes or no). |

**Example**
```console
$ vijil create token octo --name token-name \
    --token your-token \
    --is-primary yes
```

## Start

### Evaluation

Start an evaluation against a model using:

`vijil start evaluation`

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--model-hub`	| String	| Model hub (e.g., huggingface, octo, replicate). |
| `--model-name`	| String	| Name of the model to be evaluated. |
| `--dimension`	| String	| Trust dimensions (e.g., ethics, security). |
| `--generations`	| Integer	| Number of generations for the evaluation. |
| `--deployment-type` | String | Deployment type of model (e.g., private, public, local). |
| `--token` | String | Token for accessing the provided model. |

**Example**

```console
$ vijil start evaluation \
    --model-hub octo \
    --model-name mistral-7b-instruct-fp16 \
    --dimension security \
    --deployment-type public \
    --generations 1 \
    --token your-token
```

## Stop

### Evaluation

Stop an evaluation by its ID or stop all running evaluations using:

`vijil stop evaluation`

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID received after starting an evaluation. |
| `--all` | String (optional) | Stop all evaluations.


**Example**

```console
$ vijil stop evaluation --id abcd-efgh
```

## Describe

### Evaluation

Check the status/detail of an evaluation by ID using:

`vijil describe evaluation`

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID received after starting an evaluation. |


**Example**
```console
$ vijil describe evaluation --id abcd-efgh
```


### Log

Check the progress or logs of an evaluation using:

`vijil describe log`

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID received after starting an evaluation. |
| `--trail` | String (optional) | Display trailing logs from stdout. | 


**Example**
```console
$ vijil describe log --id abcd-efgh --trail
```

## List

### Evaluations

List all evaluations created in the past using:

`vijil list evaluations`

**Example**
```console
$ vijil list evaluations
```

### Tokens

List all model hub tokens saved using:

`vijil list tokens`

**Example**
```console
$ vijil list tokens
```

## Delete

### Evaluation

Delete an evaluation you started using:

`vijil delete evaluation`

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID received after starting an evaluation. |

**Example**
```console
$ vijil delete evaluation --id abcd-efgh
```


## Download

### Log

Download either `full` or only the `failure` logs of an evaluation using:

`vijil download log [full | failure]`

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID received after starting an evaluation. |

**Example**
```console
$ vijil download log failure --id abcd-efgh
```

