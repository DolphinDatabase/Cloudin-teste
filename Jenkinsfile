pipeline {
     agent any
     stages {
         stage('Deploy') {
            steps {
                sh 'docker system prune --all'
                sh 'y'
                sh 'docker build --tag cloudin-backend .'
                sh 'docker run -d -p 5000:5000 cloudin-backend'
            }
        }
     }
 }