pipeline {
    agent any
    environment {
        GCR_REPO = "us-central1-docker.pkg.dev/project-8a788ef4-4bf5-45aa-996/survey-repo/survey-app"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token',
                    url: 'https://github.com/SharathReddyKottam/survey-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $GCR_REPO:latest .'
            }
        }
        stage('Push to Artifact Registry') {
            steps {
                sh 'docker push $GCR_REPO:latest'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl set image deployment/survey-app survey-app=$GCR_REPO:latest'
            }
        }
    }
}