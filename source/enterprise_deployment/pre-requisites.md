# Pre-requisites

Before deploying **Vijil Evaluate** in your enterprise environment, ensure you have the following foundational skills and resources:

- **AWS Account**: You must have access to an AWS account with sufficient permissions to create and manage EKS clusters, RDS/Aurora databases, OpenSearch domains, and S3 buckets.
- **AWS CLI**: Install and configure the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) on your local machine.
- **kubectl**: Install [kubectl](https://kubernetes.io/docs/tasks/tools/) to interact with your Kubernetes cluster.
- **eksctl** (optional but recommended): Install [eksctl](https://eksctl.io/) for simplified EKS cluster management.
- **IAM Permissions**: Ensure your AWS user/role has permissions to create and manage EKS, RDS/Aurora, OpenSearch, and S3 resources.
- **Basic Kubernetes Knowledge**: Familiarity with Kubernetes concepts and resource management is required.
- **Networking**: Understanding of VPC, subnets, and security groups in AWS.

# Dependencies

The following AWS resources and services are required for a production deployment of Vijil Evaluate:

## Core

- **Amazon EKS Cluster**: The primary compute environment for running Vijil Evaluate services.

## Datastores

- **PostgreSQL Database**: Used for persistent storage of application data. This can be provisioned using:
  - **Amazon Aurora (PostgreSQL-compatible)** – recommended for high availability and scalability.
  - **Amazon RDS for PostgreSQL** – suitable for smaller-scale or non-production deployments.

- **Amazon OpenSearch Service**: Provides search and analytics capabilities (Elasticsearch-compatible). Required for indexing and querying evaluation data.

## Object Storage

- **Amazon S3**: Used for storing large objects such as evaluation artifacts, logs, and backups.

## Summary Table

| Dependency         | AWS Service                | Purpose                                 |
|--------------------|---------------------------|-----------------------------------------|
| Compute            | EKS                       | Run Vijil Evaluate workloads            |
| Relational DB      | Aurora/RDS (PostgreSQL)   | Persistent application data             |
| Search/Analytics   | OpenSearch                | Indexing and querying evaluation data   |
| Object Storage     | S3                        | Store artifacts, logs, and backups      |

> **Note:** All resources should be provisioned in the same AWS region for optimal performance and cost efficiency.

Once these pre-requisites and dependencies are in place, you can proceed to the deployment steps.
