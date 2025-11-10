pipeline {
  agent any
  environment {
    DOCKER_IMAGE = "tooba-nawaz/aceest_fitness"
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install & Test') {
      steps {
        sh 'python -m pip install -r requirements.txt'
        sh 'pytest -q'
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE:${GIT_COMMIT::8} .'
      }
    }
    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push $DOCKER_IMAGE:${GIT_COMMIT::8}
          '''
        }
      }
    }
    stage('Deploy to K8s') {
      steps {
        sh 'kubectl apply -f k8s/'
      }
    }
  }
}