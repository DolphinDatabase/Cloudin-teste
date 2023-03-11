pipeline {
     agent any
     stages {
         stage('Deploy') {
            steps {
                sh(script:'if [ $( docker ps -a | grep testContainer | wc -l ) -gt 0 ]; then
                    echo "docker rm -vf $(docker ps -aq)"
                    docker rmi -f $(docker images -aq)
                    echo "Older containers was deleted, creating new containers"
                else
                    echo "Creating container..."
                fi'.stripIndent()
                sh 'docker build --tag cloudin-backend .'
                sh 'docker run -d -p 5000:5000 cloudin-backend'
            }
        }
     }
 }