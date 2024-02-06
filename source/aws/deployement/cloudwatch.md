# Cloudwatch

## Accessing Logs and Health Metrics for ECS Service

To access the logs and health metrics of an ECS service, follow the steps below:

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and open AWS Elastic Container Service.

2. Open the required cluster. Currently, we have the following clusters for each environment (prod, dev, stage):
   - Vijilai-dev-cluster
   - Vijilai-stage-cluster
   - Vijilai-prod-cluster

3. Select the required service from the Services tab. In each cluster, we have the following services:
   - Vijilai-{Env}-vijilapi
   - Vijilai-{Env}-redis (logs are not enabled for redis)
   - Vijilai-{Env}-celery

4. Click on the "Logs" tab to view the logs. You can specify the time to view logs for a specific time period.

5. Click on "Health and Metrics" to view the resource consumption of the container.