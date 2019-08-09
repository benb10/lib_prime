pipeline {
    agent { docker { image 'python:3.6.5' } }
    stages {
        stage('build') {
            steps {
                bat 'echo AAA'
                bat 'python --version'
                bat 'echo BBB'
            }
        }
    }
}
