pipeline {
    agent any
    environment {
        GCR_REPO = "gcr.io/YOUR_PROJECT_ID/survey-app"
        GITHUB_TOKEN = credentials('github-token')
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
        stage('Push to GCR') {
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