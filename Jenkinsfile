pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/saaadhyaaa/agile-jenkins-3.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                /* 
                   Pipes Subject 1 marks (75), Subject 2 marks (82), 
                   and Subject 3 marks (90) straight into the python inputs.
                */
                bat "(echo 75 && echo 82 && echo 90) | python marks.py"
            }
        }
    }
}
