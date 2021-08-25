pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                //test Python version 
                sh 'python --version'

                //upgrade pip
                sh 'pip3.9 install --upgrade pip'

                //install requirements
                sh "pip3.9 install -r ${env.WORKSPACE}/requirements.txt"

                //test
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}, WORKSPACE: ${env.WORKSPACE}"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}