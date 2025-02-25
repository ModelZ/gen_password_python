pipeline {
    agent { label 'docker-agent-bookworm-jdk21' }

    stages {
        stage('init') {
            steps {
                echo "Welcome to Password Genarator"
                echo "Triggering... pipeline"
                sleep 5
                echo "Done!"
            }
        }

        stage('update apt') {
            steps {
                sh 'apt update' 
            }
        }

        stage('install python') {
            steps {
                sh 'apt install python3' 
            }
        }

        stage('test run') {
            steps {
                sh 'python3 genpass.py'
            }
        }

    }

    post {
        always {

        }
        success {
            echo 'Build and deployment successful.'
        }
        failure {
            echo 'Build or deployment failed.'
        }
    }
}
