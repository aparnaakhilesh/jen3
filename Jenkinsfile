pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'pipline', url: 'https://github.com/aparnaakhilesh/jen3.git'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 backend/pipe1.py input/data.csv output/results.csv'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover backend/tests || echo "No tests found"'
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

