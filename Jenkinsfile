pipeline {
    agent any 
    environment {
        HEROKU_API_KEY = credentials('heroku-api-key')  // Your Heroku API key
    }
    stages {
        stage('Initial'){
        steps {
            script {
                bat 'git config --global user.email "thinhtruongkhangnguyen1404@gmail.com"'
                bat 'git config --global user.name "Truong Khang Thinh Nguyen"'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                echo 'Building the application...'
                bat 'docker build -t jimmythinh1404/blur-detect .'
              
                // For example, if you have a requirements.txt, you can use:
                // sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Testing the Python Test File'
                    // Run pytest inside the Docker container for test_helpers.py
                    bat 'docker run --rm jimmythinh1404/blur-detect python -m unittest discover -s . -p "test_*.py"'
                }
            }
        }
        // stage('Code Quality Checkk')
          //  {
          //      environment{
           //         scannerHome = tool 'sonar'
            //        SONAR_SCANNER = 'SonarScanner'
            //    }
             //   steps {
                //    withSonarQubeEnv('sonar') {
                //        bat "${env.scannerHome}\\bin\\sonar-scanner.bat"
                 //   }
               // }
           // }
           stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                script{
                bat 'heroku git:remote -a flaskcalc'
                bat 'git checkout -b main'  // Create and switch to 'main' branch if it doesn't exist
                bat 'git add .'
               // bat 'git commit -am "make it better"'
                bat 'git push heroku main --force'
                }
            }
        }

        stage('Release') {
            steps {
                echo 'Releasing the application...'
                bat """
                heroku git:remote -a flaskcalc-prod
                git add .
                git commit -am "make it better"
                git push heroku main --force
                """
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Clean up actions, if necessary
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
