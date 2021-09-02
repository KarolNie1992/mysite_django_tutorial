pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                //test Python version 
                sh 'python3.9 --version'

                //upgrade pip
                sh 'pip3.9 install --upgrade pip'

                //install requirements
                sh "pip3.9 install -r ${env.WORKSPACE}/requirements.txt"

                //test variables
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}, WORKSPACE: ${env.WORKSPACE}"
            }
        }
        stage('Test') {
            steps {
                //echo 'Testing'

                //run Test in django project
                sh "python3.9 ${env.WORKSPACE}/manage.py test"
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