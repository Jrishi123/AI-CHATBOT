pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Jrishi123/AI-Chatbot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t chatbot-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop chatbot || true'
                sh 'docker rm chatbot || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5003:5000 --name chatbot chatbot-app'
            }
        }
    }
}