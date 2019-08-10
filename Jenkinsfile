pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Other') {
            steps {
                echo 'Other commands'
                echo ''
                bat 'echo AAAAA'
                bat 'python --version'
                bat 'dir'
            }
        }
    }
}
