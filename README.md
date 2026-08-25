# Docker + GitHub Actions CI/CD to AWS EC2

A complete CI/CD project that containerizes a Flask web application using Docker and automatically deploys it to an AWS EC2 instance using GitHub Actions.

## Architecture

   text
Developer
    |
    | git push
    ▼
GitHub Repository
    |
    ▼
GitHub Actions CI/CD
    |
    | SSH Deployment
    ▼
AWS EC2
    |
    ▼
Docker Container
    |
    ▼
Flask Web Application


## Technologies Used
Python
Flask
Docker
Git
GitHub
GitHub Actions
AWS EC2
Ubuntu
SSH


## Project Structure
docker-github-actions-cicd/
  
  ─ app/
    ── app.py
    ── requirements.txt

  ─ .github/
   └── workflows/
      └── deploy.yml

 ─ Dockerfile
 ─ .dockerignore
 ─ .gitignore
 ─ README.md


## Application Endpoints
Endpoint	Description
/	Main application page
/health	Health check endpoint
🐳 Run Locally with Docker
Build the Docker image
docker build -t cicd-web-app .
Run the container
docker run -d -p 5000:5000 --name cicd-container cicd-web-app

Open in your browser:

http://localhost:5000

Health check:

http://localhost:5000/health
🔄 CI/CD Workflow

Whenever code is pushed to the main branch:

GitHub Actions is triggered.
The repository is checked out.
A Docker image is built.
GitHub Actions connects to AWS EC2 using SSH.
The latest code is pulled on EC2.
The existing Docker container is stopped and removed.
A new Docker image is built.
A new container is started automatically.
🔐 GitHub Secrets

The following secrets are required for deployment:

Secret	Description
EC2_HOST	Public IP address of the EC2 instance
EC2_USER	EC2 username
EC2_SSH_KEY	Private SSH key used for deployment

⚠️ Never commit private keys, .pem files, passwords, or other sensitive credentials to GitHub.

## Deployment

The application is automatically deployed to AWS EC2 whenever changes are pushed to the main branch.

git add .
git commit -m "Update application"
git push origin main

This automatically triggers the GitHub Actions CI/CD pipeline.

## Author

CHIMALA NIKHITHA

⭐ Future Improvements
Deploy Docker images using Amazon ECR
Add Docker Compose
Add Nginx reverse proxy
Add HTTPS using SSL/TLS
Add automated testing
Add application health checks
Implement blue-green deployment