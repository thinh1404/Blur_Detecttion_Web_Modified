pipeline {
    agent any 

    stages {
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
                    // Run pytest inside the Docker container
                    // bat 'docker run --rm jimmythinh1404/tic-tac-toe python -m pytest test.py --junitxml= Tic_Tac_Toe_Game.py'
                }
                 
            }
           
        }
        stage('Code Quality Checkk')
        { 
            // environment{
            //     scannerHome = tool 'sonar'
            //     SONAR_SCANNER = 'SonarScanner'
            // }
            // steps {
            //     withSonarQubeEnv('sonar') {
            //         bat "${env.scannerHome}\\bin\\sonar-scanner.bat"
            //     }
            // }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Here you would add your deployment commands
                // This might include copying files to a server or starting a service
                // Example:
                // sh 'scp -r ./* user@yourserver:/path/to/deploy/'
            }
        }

        stage('Release') {
            steps {
                echo 'Releasing the application...'
                // You can add steps to notify users or finalize the release here
                // For example:
                // sh 'echo "Application released!"'
                // Or you might trigger a notification to a chat system, etc.
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
