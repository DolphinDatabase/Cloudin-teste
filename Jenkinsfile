pipeline {
     agent any
     stages {
         stage('Deploy') {
            steps {
                sh "docker system prune -f"
                sh 'docker build --tag cloudin-backend .'
                sh 'docker run -d -p 5000:5000 cloudin-backend'
            }
        }
     }
 }