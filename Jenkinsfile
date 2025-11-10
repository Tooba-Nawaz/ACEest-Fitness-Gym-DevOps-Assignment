pipeline {
  agent any
  environment {
    DOCKER_IMAGE = "toobanawaz/aceest_fitness"
  }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Install & Test') {
      steps {
        sh 'python -m pip install -r requirements.txt'
        sh 'pytest -q'
      }
    }
    stage('Static Analysis') {
      steps {
        withSonarQubeEnv('MySonar') {
    sh 'sonar-scanner'
      }
        echo 'Run SonarQube analysis here (configure Sonar scanner)'
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE:${GIT_COMMIT::8} .'
      }
    }
    stage('Push Image') {
      steps {
        echo 'Push to Docker Hub (configure credentials in Jenkins)'
      }
    }
    stage('Deploy to K8s') {
      steps {
        echo 'Use kubectl to apply manifests (example in repo)'
      }
    }
  }
  post {
    always { archiveArtifacts artifacts: '**/test-reports/*.xml', allowEmptyArchive: true }
  }
}
