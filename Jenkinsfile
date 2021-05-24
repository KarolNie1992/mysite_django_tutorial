pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.9.5-alpine3.12' 
                }
            }
            steps {          
                sh """
                    python --version
                    set +e
                """
            }
        }
    }
}