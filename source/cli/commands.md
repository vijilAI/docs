# Commands

The Vijil CLI contains the following commands.
In all the commands, except `help`, you can either type in all options, or enter them interactively after just typing
`vijil <command-name>` and pressing Enter.

## Help

`vijil --help`

Displays all the available commands in the CLI.

## Authenticate

### Login

`vijil login <username>`

Used to authenticate to your VIJIL account. Create a VIJIL access token from the GUI to log in to the CLI.


**Arguments**

| Name | Possible values | Usage/Description
|--|---|---|
| `--token` | String | VIJIL access token from the GUI. |

**Example**

```console
$ vijil login admin --token 'my-token'
```

### Logout

`vijil logout`

Logs you out from your VIJIL account in the CLI.

```console
$ vijil logout
```

## Create

### Token

`vijil create token <model-provider>`

Used to create tokens for the model providers. List of available providers are given below:
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
| `--token` | String | Token from the model provider. |
| `--is-primary` | [yes\|no] | Yes to save token as default. |

**Example**
```console
$ vijil create token octo --name 'token-name' --token 'your-token' --is-primary 'yes'
```

## Start

### Evaluation

`vijil start evaluation`

Used to start an evaluation against a model.

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--model-hub`	| String	| Model provider (e.g., huggingface, octo, replicate). |
| `--model-name`	| String	| Name of the model to be evaluated. |
| `--dimension`	| String	| Trust dimensions (e.g., ethics, security). |
| `--generations`	| Integer	| Number of generations for the evaluation. |
| `--deployment-type` | String | Deployment type of model (e.g., private, public, local). |
| `--token` | String | Token for Provoded model. |

**Example**

```console
$ vijil start evaluation --model-hub 'octo' --model-name 'mistral-7b-instruct-fp16' --dimension 'ethics' --deployment-type 'public' --generations 1 --token 'your-token'
```

## Stop

### Evaluation

`vijil stop evaluation`

Stops an evaluation by its ID or stop all running evaluations.

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID that you received after starting an evaluation. |
| `--all` | String (optional) | Stops all evaluations


**Example**

```console
$ vijil stop evaluation --id 'abcd-efgh'
```

## Describe

### Evaluation

`vijil describe evaluation`

Checks the status/detail of any evaluation by ID.

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID that you received after starting an evaluation. |


**Example**
```console
$ vijil describe evaluation --id 'abcd-efgh'
```


### Log

`vijil describe log`

Check Progerss or logs of Evaluation.

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID that you received after starting an evaluation. |
| `--trail` | String (optional) | Displays trailing logs from stdout. | 


**Example**
```console
$ vijil describe log --id 'id' --trail
```

## List

### Evaluations

`vijil list evaluations`

List all the evaluations you have started.

**Example**
```console
$ vijil list evaluations
```

### Tokens

`vijil tokens`

List all model provider tokens saved.

**Example**
```console
$ vijil list tokens
```

## Delete

### Evaluation

`vijil delete evaluation`

Deletes an evaluation you started.

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID that you received after starting an evaluation. |

**Example**
```console
$ vijil delete evaluation --id 'abcd-efgh'
```


## Download

### Log

`vijil download log [full | failure]`

Download either `full` or just the `failure` logs of an evaluation.

**Arguments**
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | ID that you received after starting an evaluation. |

**Example**
```console
$ vijil download log failure --id 'abcd-efgh'
```

