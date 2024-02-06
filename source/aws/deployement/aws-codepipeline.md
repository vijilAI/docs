# Pipeline Execution in Different Environments

In the development environment, the pipeline will be triggered automatically when any commit is pushed to the develop branch. However, staging and production pipelines require manual triggering.

## Manual Pipeline Execution:

To run a pipeline manually, follow these steps:

1. Sign in to the AWS Management Console and open AWS CodePipeline.

2. Select the pipeline from the following options:
   - **Vijilai-dev-codepipeline** (Branch: develop)
   - **Vijilai-stage-codepipeline** (Branch: staging)
   - **Vijilai-prod-codepipeline** (Branch: production)

3. Click on the "Release Change" button to start the pipeline manually.

4. To view the logs, open the pipeline, click on "Details" in the Build stage, and select the "Logs" tab.
