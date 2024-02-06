# Removing Old Images from AWS ECR

To avoid extra costs in AWS ECR, which costs $1/GB, follow these steps to remove old builds that are no longer required:

1. Sign in to the AWS Management Console and open AWS ECR.

2. Open a repository. There are three repositories, one for each environment:
   - vijilai-prod-repo
   - vijilai-stage-repo
   - vijilai-dev-repo

3. Select the image you want to remove and choose "Delete."
