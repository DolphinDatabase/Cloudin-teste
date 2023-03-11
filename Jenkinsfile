pipeline {
     agent any
     stages {
         stage('Install dependencies') {
             steps {
                 sh 'pip install -r requirements.txt'
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