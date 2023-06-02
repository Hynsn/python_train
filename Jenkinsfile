pipeline{
    agent any
    stages{
        stage("Start"){
            steps {
                echo 'hello world'
            }
        }
        stage("Run"){
            steps {
                echo 'run python'
                script {
                    sh 'python --version'
                    sh 'python main.py'
              }
            }
        }
    }
    post{
        always{
            echo 'always say goodbay'
        }
    }
}