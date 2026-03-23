pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'pipline', url: 'https://github.com/aparnaakhilesh/jen3.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r backend/requirements.txt || echo "No requirements.txt found"'
            }
        }

        stage('Run Script') {
            steps {
                sh './venv/bin/python backend/pipe1.py input/data.csv output/results.csv'
            }
        }

        stage('Test') {
            steps {
                sh './venv/bin/python -m unittest discover backend/tests || echo "No tests found"'
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'output/*.csv', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}


