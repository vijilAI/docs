# ECS Update

To upscale and increase the memory:

1. Sign in to the AWS Management Console and open AWS CloudFormation.

2. Go to "Stacks" and select the environment ECS stack you want to update. There are three stacks for ECS:
   - vijilai-prod-ecs
   - vijilai-stage-ecs
   - vijilai-dev-ecs

3. Select "Update" and choose "Use current template," then click "Next."

4. Set `ClusterSize` and `TasksDesiredCounter` parameter values to 0. Select the new EC2 type from the `Ec2Type` parameter.

5. Update the RAM for Celery, Redis, and API in respective parameters. RAM can be divided using the following formula. Memory is assumed in MBs:
   - CeleryRAM = ((totalRam - 1024) / 100) * 33
   - RedisRAM = ((totalRam - 1024) / 100) * 10
   - VijilapiRAM = ((totalRam - 1024) / 100) * 10

6. Make sure the `VijilImage` param has the latest image name and choose "Next."

7. On the "Configure stack options" step, no update is required, so choose "Next."

8. At the last step, choose the "View change set" to review the changes, and after reviewing the changes, choose "Execute change set" or choose "Submit" to run the update.

9. Monitor the execution process in the "Events" tab of the selected stack.

10. In a few minutes, all tasks and the EC2 host will be terminated, and an "UPDATE_COMPLETE" message will appear against the stack name in the "Events" tab.

11. After the update completes, again choose "Update," "Use current template," and click "Next."

12. This time, set `ClusterSize` and `TasksDesiredCounter` parameter values to 1.

13. Complete the update steps, and resources will be up in a few minutes.

**Note:** To update any other parameter, don't set `ClusterSize` and `TasksDesiredCounter` parameter values to 0.