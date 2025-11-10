# Short Report (2 pages approx)

## CI/CD Architecture Overview
- GitHub: source code hosting, branching and tags for versions.
- Jenkins: orchestrates CI pipeline: checkout -> test -> static analysis -> build -> push -> deploy.
- SonarQube: static code quality checks + quality gates enforced in pipeline.
- Docker Hub: registry for versioned images.
- Kubernetes (Minikube or cloud): runtime for containerized app with multiple deployment strategies.

## Challenges & Mitigation
- Networking complexities in Kubernetes -> use Minikube for local demo and document required kubectl commands.
- Managing secrets (DockerHub credentials) in Jenkins -> use Jenkins Credentials plugin.
- Ensuring tests run inside pipeline -> run pytest inside build agent and confirm artifacts preserved.

## Key Automation Outcomes
- Automated test execution and quality checks reduce human error.
- Versioned Docker images provide reproducible releases.
- Multiple deployment strategies (canary, blue-green, rolling) demonstrated via manifests.

