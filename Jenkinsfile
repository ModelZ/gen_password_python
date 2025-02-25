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
                sh 'apt install python3 -y' 
            }
        }

        stage('test run') {
            steps {
                sh 'ls -la'
                sh 'python3 gen_pass.py'
            }
        }

    }

    post {
        always {
            echo 'This is Post Stages'
        }
        success {
            echo 'Build and deployment successful.'
        }
        failure {
            echo 'Build or deployment failed.'
        }
    }
}
