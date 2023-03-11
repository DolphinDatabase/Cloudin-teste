pipeline {
     agent any
     stages {
        stage('Clean Docker') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'docker rm -v $(docker ps -aq -f status=exited)'
                    sh 'docker rmi -f $(docker images -aq -f status=exited)'
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