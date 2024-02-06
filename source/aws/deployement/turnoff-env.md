# Turning Off an Environment

To turn off an environment, follow these steps:

1. Sign in to the AWS Management Console and open AWS CloudFormation.

2. Go to "Stacks" and select the environment ECS stack you want to stop. There are three stacks for ECS:
   - vijilai-prod-ecs
   - vijilai-stage-ecs
   - vijilai-dev-ecs

3. Select "Update," choose "Use current template," and click "Next."

4. Set `ClusterSize` and `TasksDesiredCounter` parameter values to 0 and choose "Next."

5. On the "Configure stack options" step, no update is required, so choose "Next."

6. At the last step, choose the "View change set" to review the changes. After reviewing the changes, choose "Execute change set" or choose "Submit" to run the update.

7. Monitor the execution process in the "Events" tab of the selected stack.

8. In a few minutes, all tasks and the EC2 host will be terminated, and an "UPDATE_COMPLETE" message will appear against the stack name in the "Events" tab.
