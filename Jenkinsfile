pipeline {
     agent any
     stages {
        stage('Clean Docker') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'docker rm -vf $(docker ps -aq)'
                    sh 'docker rmi -f $(docker images -aq)'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker build --tag cloudin-backend .'
                sh 'docker run -d -p 5000:5000 cloudin-backend'
            }
        }
     }
 }