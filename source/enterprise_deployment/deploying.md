# Deploying Vijil Evaluate with Helm

Now that you have provisioned an EKS cluster and ensured connectivity to the required AWS resources—**PostgreSQL** (Aurora or RDS), **OpenSearch/Elasticsearch**, and **S3**—you are ready to deploy **Vijil Evaluate** using our Helm chart.

## Prerequisites

- An **EKS cluster** with the necessary IAM permissions and networking configuration.
- Access to a PostgreSQL-compatible database (**Aurora or RDS**).
- Access to an **OpenSearch or Elasticsearch** domain.
- **S3** buckets for object storage.
- An **Auth0** application for authenticating with all APIs
- Access to the private **`vijil-eks`** GitHub repository. If you do not have access, please contact the Vijil team.

## Deploying the Helm Chart

The deployment of Vijil Evaluate is managed via a Helm chart provided in the `vijil-eks` GitHub repository that you will need to contact us in order to gain access to. The repository contains a `README.md` with instructions for configuring and deploying the chart.

### Steps Overview

1. **Clone the Repository**

```bash
git clone git@github.com:vijil-ai/vijil-eks.git
cd vijil-eks
```

2. **Review the README**

The `README.md` in the repository contains the most up-to-date and detailed deployment instructions, including required values, configuration options, and example commands.

3. **Configure Your Values**

Prepare a `values.yaml` and `secrets.yaml` file with the necessary configuration for your environment. This includes database connection strings, OpenSearch endpoints, S3 bucket names, and any other required secrets or settings. There are examples in the `vijil-eks` repository for you to follow.

4. **Install the Helm Chart**

Follow the instructions in the `README.md` to install the chart, for example:

```bash
helm upgrade --install  eval . -f values/dev.yaml -f values/secrets/dev.yaml
```

It should take around 10-15m to deploy.

> **Note:** The actual command and chart path may vary; always refer to the repository's `README.md` for the latest instructions.

5. **Verify the Deployment**

After installation, monitor the pods and services in your EKS cluster to ensure that all components are running as expected.

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

When you fetch the ingress defintions, you should see 2 Load Balancers with DNS. You will want to add those DNS entries under the Route53 entries you desire in your AWS account, so that you can access the API and Web UI through the domain names that you want.
You should be able to verify that the API is up and running by hitting the `/healthz` endpoint

## Next Steps

- For advanced configuration, troubleshooting, and upgrade instructions, consult the `vijil-eks` repository documentation.
- If you encounter issues or need support, please reach out to the Vijil team.

> **Reminder:** The Helm chart and deployment scripts are actively maintained. Always refer to the `vijil-eks` repository for the latest best practices and updates.
