# Updating Secrets in AWS Secret Manager

To update secrets in AWS Secret Manager, follow these steps:

1. Sign in to the AWS Management Console and open Secret Manager.

2. Open the `vijilai/codebuild_secrets` secret.

3. Click on "Retrieve Secrets."

4. Update the value of the key you want.

5. For the Env file, use the string with `\n` escape characters.

6. The `DEV_ENV` key has a development environment file content.

7. The `STAGE_ENV` key has a staging environment file content.

8. The `PROD_ENV` key has a production environment file content.
