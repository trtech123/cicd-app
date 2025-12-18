pipeline {
    agent any

    environment {
        IMAGE = "tcohen123/simple-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE:latest .'
            }
        }

        stage('Test App') {
            steps {
                sh '''
                docker run -d --name test_app -p 5000:5000 $IMAGE:latest
                sleep 5
                curl -f http://localhost:5000/health
                docker rm -f test_app
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cd /opt/ansible
                ansible-playbook -i inventory.ini docker.yml
                '''
            }
        }
    }
}
