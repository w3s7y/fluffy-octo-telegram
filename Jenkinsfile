pipeline {
    agent any

    stages {
        stage('Lint') {
            steps {
                sh 'echo "TODO"'
            }
        }
        stage('Test') {
            steps {
		sh 'python manage.py test'
            }
        }
        stage('Tag') {
            steps {
		sh 'git tag ${BUILD_NUMBER}_$(date)'
		sh 'git push --tags'
            }
        }
    }
}
