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
