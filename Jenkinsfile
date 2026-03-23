pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from your repository branch
                git branch: 'pipline', url: 'https://github.com/aparnaakhilesh/jen3.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run') {
            steps {
                sh 'python3 pipe1.py'
            }
        }

        stage('Test') {
            steps {
                // If you add pytest-based tests later
                sh 'pytest || echo "No tests found"'
            }
        }
    }

    post {
        success {
            echo 'Python  pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}
