# ACEest_Fitness CI/CD Project (Prepared)

This project skeleton fulfills the Assignment 2 requirements for the DevOps course.
It includes a simple Flask application, tests, Dockerfile, Jenkinsfile, and Kubernetes manifests for various deployment strategies.

**What is included (summary):**
- Flask app under `app/` with REST API endpoints under `/api`
- Pytest tests under `tests/`
- Dockerfile to build the application image
- Jenkinsfile (Declarative pipeline) with stages for test, static analysis, build, push and deploy (placeholders)
- Kubernetes manifests for RollingUpdate, Canary, Blue-Green, and A/B test setups
- SonarQube config placeholder
- This README with run instructions

## Quick local run (without Docker)
1. Create a Python 3.11 venv
2. pip install -r requirements.txt
3. python run.py
4. Open http://127.0.0.1:5000/api/health

## Run tests
    pytest -q

## Build Docker image (example)
    docker build -t your-dockerhub-username/aceest_fitness:latest .

## Notes for submission
- Replace `your-dockerhub-username` in manifests/Jenkinsfile with your Docker Hub user.
- Configure Jenkins credentials and SonarQube plugin to enable full CI.
- For Kubernetes, Minikube is recommended for a local demo. Use `kubectl apply -f k8s/` to deploy manifests.
# ACEest-Fitness-Gym-DevOps-Assignment
