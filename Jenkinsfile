pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'hadasanaki/snake-game:test'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    def myContainer = docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").run('-d -p 8080:8000')
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    python -m pytest
                '''
            }
        }

        stage('Push to Registry') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
