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
                    // Run pytest inside the Docker container for test_helpers.py
                    bat 'docker run --rm jimmythinh1404/blur-detect python -m unittest discover -s . -p "test_*.py"'
                }
            }
        }
        stage('Code Quality Check')
        { 
            steps {
                echo "Code Quality Check"
            }
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
                bat 'docker run -d --name blur-detect-test -p 5001:5000 jimmythinh1404/blur-detect'
            }
        }

        stage('Release') {
            steps {
                echo 'Releasing the application...'
                // You can add steps to notify users or finalize the release here
                // For example:
                // sh 'echo "Application released!"'
                // Or you might trigger a notification to a chat system, etc.
                // Stop the existing production container if it exists
                // bat 'docker stop blur-detect-prod || echo "No existing production container to stop."'
                // bat 'docker rm blur-detect-prod || echo "No existing production container to remove."'

                // Deploy the application to the production environment
                bat 'docker run -d --name blur-detect-prod -p 80:5000 jimmythinh1404/blur-detect'
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
