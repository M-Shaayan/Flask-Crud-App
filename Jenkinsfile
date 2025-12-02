//Shaayan
//alisudfcow

pipeline {
    agent any
    environment {
        NEW_VERSION = '1.3.0'
    }
    parameters {
        choice(name: 'DEPLOY_VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: 'Select version')
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Run tests?')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building Flask CRUD App'
                echo "Building version ${NEW_VERSION}"
            }
        }
        stage('Test') {
            when {
                expression { params.executeTests }
            }
            steps {
                echo 'Testing Flask CRUD App'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying Flask CRUD App'
                echo "Deploying version ${params.DEPLOY_VERSION}"
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}
