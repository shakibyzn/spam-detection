# Spam Classification Project

This project serves as a template to learn how to integrate **GitHub Actions** and GitHub API using **ghapi**, along with the **Weights & Biases (WandB) API**, to create a **CI/CD workflow** for machine learning projects.


## Project Overview
The project focuses on creating a streamlined process for running experiments and tracking results using GitHub Actions and WandB. This setup automates the workflow by enabling experiment tracking directly from pull requests, simplifying collaboration and monitoring for machine learning models.

This project is the final submission for the **CI/CD for Machine Learning (GitOps)** course by [Weights & Biases](https://www.wandb.courses/courses/ci-cd-for-machine-learning).

## Features

- **ChatOps Integration:** Listens for the comment `"/wandb <run id>"` on a pull request to trigger a comparison workflow.
- **Baseline Fetching:** Fetches the run tagged as “baseline” from your WandB project using the WandB API.
- **Comparison Report:** Automatically generates a report comparing the baseline run with the provided run ID.
- **PR Commenting:** Posts a comment on the pull request with the URL to the comparison report, making it easy to access.


## Setup Instructions

### 1. Install Dependencies
First, install the required dependencies by running the following command:
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables
You need to set the following WandB environment variables to integrate the WandB API:

- WANDB_ENTITY
- WANDB_PROJECT
- WANDB_API_KEY

### 3. Run the Project
```
python main.py
```

## GitHub Action & WandB Integration
### 1. Set Up Repository Secrets
To integrate the workflow with GitHub Actions, first, create the following repository secrets on GitHub for your project:

- WANDB_ENTITY
- WANDB_PROJECT
- WANDB_API_KEY

These secrets will be used to communicate with WandB during the workflow execution.

### 2. Pull Request Workflow
When you create a pull request, you can trigger an experiment run on WandB by commenting on the PR with the following command:

```
/wandb experiment-run-id
```
This will trigger the workflow, and you’ll see a workspace on your WandB dashboard where you can monitor the experiment's progress.

## License
This project is licensed under the MIT License.