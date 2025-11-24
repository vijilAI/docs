# Pre-requisites

Before deploying **Vijil Evaluate** in your enterprise environment, ensure you have the following foundational skills and resources:

- **AWS Account**: You must have access to an AWS account with sufficient permissions to create and manage EKS clusters, RDS/Aurora databases, OpenSearch domains, and S3 buckets.
- **AWS CLI**: Install and configure the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) on your local machine.
- **kubectl**: Install [kubectl](https://kubernetes.io/docs/tasks/tools/) to interact with your Kubernetes cluster.
- **IAM Permissions**: Ensure your AWS user/role has permissions to create and manage EKS, RDS/Aurora, OpenSearch, and S3 resources.
- **Basic Kubernetes Knowledge**: Familiarity with Kubernetes concepts and resource management is required.
- **Networking**: Understanding of VPC, subnets, and security groups in AWS.

## Dependencies

The following AWS resources and services are required for a production deployment of Vijil Evaluate:

### Core

- **Amazon EKS Cluster**: The primary compute environment for running Vijil Evaluate services.

### Datastores

- **PostgreSQL Database**: Used for persistent storage of application data. This can be provisioned using:
  - **Amazon Aurora (PostgreSQL-compatible)** – recommended for high availability and scalability.
  - **Amazon RDS for PostgreSQL** – suitable for smaller-scale or non-production deployments.
  - Any other PostgreSQL solution you want that your EKS cluster has permission to access

- **Amazon OpenSearch Service**: Provides search and analytics capabilities (Elasticsearch-compatible). Required for indexing and querying evaluation data.

### Object Storage

- **Amazon S3**: Necessary for storing artifacts and handling data uploads for harness creations and other funcitonality. You will need to create three S3 buckets:
  1. **Evaluation Data Bucket** – for storing evaluation results and related data.
  2. **Configs Bucket** – for storing configuration files required by the vijil-evaluate service.
  3. **File Uploads Bucket** – for handling file uploads, such as files used in harness creation.
    
    For the file uploads bucket you will also need to go to the control panel of this bucket and add CORS configurations, such that it is able to accept signed URL file uploads from your browser. Below is an example of what to add in an AWS S3 bucket's CORS configuration (it will be very similar in the cloud storage equivalents of other cloud providers):
    ```JSON
    [
      {
          "AllowedHeaders": [
              "*"
          ],
          "AllowedMethods": [
              "GET",
              "PUT",
              "POST",
              "HEAD"
          ],
          "AllowedOrigins": [
              "https://*.yourdomain.com"
          ],
          "ExposeHeaders": [
              "ETag",
              "x-amz-request-id",
              "x-amz-id-2"
          ],
          "MaxAgeSeconds": 3000
      }
    ]
    ```

### Authentication

- **Auth0** - You will require an Auth0 account and the ability to create an Auth0 application in your tenant

### Summary Table

| Dependency         | AWS Service                | Purpose                                 |
|--------------------|---------------------------|-----------------------------------------|
| Compute            | EKS                       | Run Vijil Evaluate workloads            |
| Relational DB      | Aurora/RDS (PostgreSQL)   | Persistent application data             |
| Search/Analytics   | OpenSearch                | Indexing and querying evaluation data   |
| Object Storage     | S3                        | Store artifacts, logs, and backups      |

> **Note:** All resources should be provisioned in the same AWS region for optimal performance and cost efficiency.

Once these pre-requisites and dependencies are in place, you can proceed to the deployment steps.
