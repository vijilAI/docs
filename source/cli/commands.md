# Commands

The Vijil CLI contains the following commands.
In all the commands, except `help`, you can either type in all options, or enter them interactively after just typing
`vijil <command-name>` and pressing Enter.

<!-- | Command | Functionality
|--|---|
| `vijil --help` | Displays all CLI options. |
| `vijil login` | Used for authentication, required to use all other CLI commands. Use your login credentials for the GUI. |
|  `vijil run | Used to submit an evaluation. |
| `vijil status` |Checks the status/detail of any job by job ID. |
| `vijil stop` | Stops a job by job ID. |
| `vijil list` | Lists all in-progress or completed jobs on your account. |
| `vijil delete` | Deletes a job by its job ID. |
| `vijil download` | Gets report/hitlog file given job ID. |
| `vijil replicate` / `vijil huggingface` / `vijil octo` | Sets API tokens for model Replicate , Huggingface , OctoAI, respectively. |
| `vijil logout` | Logs you out of the CLI. | -->


## `vijil --help`

Displays all CLI options.


## `vijil login`

Used for authentication, required to use all other CLI commands. Use your login credentials for the GUI.


### Arguments

| Name | Possible values | Usage/Description
|--|---|---|
| `--username` | String | Registered Username of Vijil. |
| `--token` | String | API Token of Vijil. |

### Example

```console
foo@bar:~$ vijil login --username my_username --token my_token
Token verification successful. Configuration complete.
```


## `vijil logout`

Logs out from CLI.

```console
foo@bar:~$ vijil logout
```

## `vijil run`

Used to submit an evaluation.

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| `--job-name`	| String	| Unique name for Job. |
| `--model-type`	| String	| Model provider (e.g., huggingface, octo, replicate). |
| `--model-name`	| String	| Name of the model to be evaluated. |
| `--dimension`	| String	| Trust dimensions (e.g., ethics, security). |
| `--generations`	| Integer	| Number of generations for the evaluation. |
| `--deployment-type` | String | Deployment type of model (e.g., private, public, local). |
| `--token` | String | Token for Provoded model. |

### Example

```console
foo@bar:~$ vijil run --job-name jobname --model-type octo --model-name mistral-7b-instruct-fp16 --dimension ethics --deployment-type public --generations 1 --token 'your-token'
Running evaluation for model type: octo, model name: mistral-7b-instruct-fp16
Successfully Create Evaluation, Check Job Status by ID: 81f05220-27be-4a84-b707-354a71b7359e
```

## `vijil list`

List jobs details.

### Example
```console
foo@bar:~$ vijil list
```

## `vijil status`

Checks the status/detail of any job by ID.

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | Id that is recieved while submit evaulation. |
| `--all` | String (optional) | List full details (default is truncated)


### Example
```console
foo@bar:~$ vijil status --id id
Getting Job status for ID: id
Job Status: .....
Job Result: .....
```

## `vijil stop`

Stops a job by job ID or stop all running jobs.

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | Id that is recieved while submit evaulation. |
| `--all` | String (optional) | Stops all jobs


### Example

```console
foo@bar:~$ vijil stop --id id
Stopping Evaluation of ID: id
Job Status: Stopped
```

## `vijil logs`

Check Progerss or logs of Evaluation.

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | Id that is recieved while submit evaulation. |
| `--trail` | String (optional) | Displays trailing logs from stdout. | 


### Example
```console
foo@bar:~$ vijil logs --id id
foo@bar:~$ vijil logs --id id --trail
```


## `vijil delete`

Deletes a job.

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| `--id` | String | Id that is recieved while submit evaulation. |

### Example
```console
foo@bar:~$ vijil delete --id id
```

## `vijil download`

Download report/hitlog file or report PDF by job ID.

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| `--file-id` | String | Id that is recieved while job detail or list. |

### Example
```console
foo@bar:~$ vijil download --file-id fileid
```

## `vijil tokens`

List all saved integration tokens of model.

### Example
```console
foo@bar:~$ vijil tokens
```

## `vijil integrations`

Save integration tokens of model to Vijil 

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| `--source` | String | Model provider (e.g., huggingface, octo, replicate). |
| `--name` | String | Name of token. |
| `--token` | String | Token of integration platform. |
| `--is-primary` | String | Yes to save token as default. |

### Example
```console
foo@bar:~$ vijil integrations --source octo --name newone --token token --is-primary yes/no
```