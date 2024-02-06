# Allocated Memory for Each Task

Currently, we have the following instance types and allowed RAM for each container:

| Env   | EC2 Type     | Total vCPUs | Total RAM (GB) | Celery RAM (GB) | API RAM (GB) | Redis RAM (GB) |
|-------|--------------|-------------|----------------|-----------------|--------------|----------------|
| Dev   | t3.xlarge    | 2           | 16             | 4               | 2            | 2              |
| Stage | t3.xlarge    | 4           | 16             | 4               | 2            | 2              |
| Prod  | t3.2xlarge   | 8           | 32             | 10              | 3            | 3              |

Above memory allocation is the maximum that can be assigned. During deployment, if there's low memory availability, the latest containers will not be able to start. If you want to increase the memory, you will have to upgrade the EC2 type, resulting in a higher cost.