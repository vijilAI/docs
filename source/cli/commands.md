# Commands

The Vijil CLI contains the following commands.
In all the commands, except `help`, you can either type in all options, or enter them interactively after just typing
`vijil <command-name>` and pressing Enter.

| Command | Functionality
|--|---|
| `vijil --help` | Displays all CLI options. |
| `vijil login --username <username_without_domain> --token <password>` | Used for authentication, required to use all other CLI commands. Use your login credentials for the GUI. |
|  `vijil run --model-type <model_provider> --model-name <model_name> --dimensions <trust_dimension> --generations <no_of_generations>` | Used to submit an evaluation. |
| `vijil status` |Checks the status/detail of any job by job ID. |
| `vijil stop` | Stops a job by job ID. |
| `vijil list` | Lists all in-progress or completed jobs on your account. |
| `vijil delete` | Deletes a job by its job ID. |
| `vijil download` | Gets report/hitlog file given job ID. |
| `vijil replicate` / `vijil huggingface` / `vijil octo` | Sets API tokens for model Replicate , Huggingface , OctoAI, respectively. |
| `vijil logout` | Logs you out of the CLI. |


## `vijil --help`

Displays all CLI options.


## `vijil login`

Used for authentication, required to use all other CLI commands. Use your login credentials for the GUI.

### Example
```bash
vijil login --username my_username --token my_token
```

### Expected Output
```bash
Token verification successful. Configuration complete.
```

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| --username | String | Registered Username of Vijil. |
| --token | String | API Token of Vijil. |


## `vijil logout`

Logs out from CLI.

### Example
```bash
vijil logout
```

## `vijil run`

Used to submit an evaluation.

### Example
```bash
vijil run --job-name jobname --model-type huggingface --model-name gpt2 --dimension ethics --deployment-type local --generations 1 --token ''
```

### Expected Output
```bash
Running evaluation for model type: huggingface, model name: gpt2
Successfully Create Evaluation, Check Job Status by ID: 81f05220-27be-4a84-b707-354a71b7359e
```

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| --job-name	| String	| Unique name for Job. |
| --model-type	| String	| Model provider (e.g., huggingface, octo, replicate). |
| --model-name	| String	| Name of the model to be evaluated. |
| --dimension	| String	| Trust dimensions (e.g., ethics, security). |
| --generations	| Integer	| Number of generations for the evaluation. |
| -deployment-type | String | Deployment type of model (e.g., private, public, local). |
| -token | String | Token for Provoded model. |


## `vijil list` or `vijil list -a`

List all the Jobs details with trucated values and full values.

### Example
```bash
vijil list
```


## `vijil status`

Checks the status/detail of any job by ID.

### Example
```bash
vijil status --id id
```

### Expected Output
```bash
Getting Job status for ID: id
Job Status: .....
Job Result: .....
```

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| --id | String | Id that is recieved while submit evaulation. |


## `vijil stop` or `vijil stop -a`

Stops a job by job ID or stop all running jobs.

### Example
```bash
vijil stop --id id
vijil stop --all
```

### Expected Output
```bash
Stopping Evaluation of ID: id
Job Status: Stopped
```

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| --id | String | Id that is recieved while submit evaulation. |


## `vijil logs` or `vijil logs --trail`

Check Progerss or logs of Evaluation.

### Example
```bash
vijil logs --id id
vijil logs --id id --trail
```

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| --id | String | Id that is recieved while submit evaulation. |


## `vijil delete`

Deletes a job

### Example
```bash
vijil delete --id id
```

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| --id | String | Id that is recieved while submit evaulation. |


## `vijil download`

Download Report/Hitlog file or Report Pdf by it's file id.

### Example
```bash
vijil download --file-id fileid
```

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| --file-id | String | Id that is recieved while job detail or list. |


## `vijil tokens`

List all saved integration tokens of model.

### Example
```bash
vijil tokens
```

## `vijil integrations`

Save integration tokens of model to Vijil 

### Example
```bash
vijil integrations --source octo --name newone --token token --is-primary yes/no
```

### Arguments
| Name | Possible values | Usage/Description
|--|---|---|
| --source | String | Model provider (e.g., huggingface, octo, replicate). |
| --name | String | Name of token. |
| --token | String | Token of integration platform. |
| --is-primary | String | Yes to save token as default. |