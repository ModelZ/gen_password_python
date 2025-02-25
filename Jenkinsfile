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
                sh 'apt install python3 python3-pip python3.11-venv -y' 
            }
        }

        stage('install dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('test run') {
            steps {
                sh '''
                ls -la
                source venv/bin/activate
                python3 gen_pass.py
                '''
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
