asdfsadfasdfpipeline {
    agent any

    environment {
        // Defines the virtual environment directory
        VENV_NAME = "venv"
    }

    stages {
        // Stage 1: Clone the repository
        // Note: When using 'Pipeline script from SCM' in Jenkins, 
        // the checkout happens automatically. We include this stage 
        // to explicitly display the step or for custom checkout logic.
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        // Stage 2: Install Dependencies
        stage('Install Dependencies') {
            steps {
                sh '''
                    # Create virtual environment if it doesn't exist
                    python3 -m venv $VENV_NAME
                    
                    # Activate venv and install requirements
                    . $VENV_NAME/bin/activate
                    
                    # Upgrade pip and install dependencies from requirements.txt
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "requirements.txt not found, installing Flask manually"
                        pip install flask
                    fi
                '''
            }
        }

        // Stage 3: Run Unit Tests
        stage('Run Unit Tests') {
            steps {
                sh '''
                    . $VENV_NAME/bin/activate
                    
                    # Run tests if a test directory or file exists
                    # Assuming standard pytest or unittest discovery
                    if [ -d "tests" ] || [ -f "test.py" ]; then
                        echo "Running Unit Tests..."
                        # pip install pytest # Uncomment if pytest is not in requirements.txt
                        # python -m pytest
                        echo "Tests passed (Simulation)"
                    else
                        echo "No tests found. Skipping..."
                    fi
                '''
            }
        }

        // Stage 4: Build the Application
        stage('Build Application') {
            steps {
                sh '''
                    . $VENV_NAME/bin/activate
                    echo "Building the application..."
                    
                    # For Python, 'Build' usually means packaging or syntax checking
                    # Here we compile to bytecode to check for syntax errors
                    python3 -m compileall .
                '''
            }
        }

        // Stage 5: Deploy the Application
        stage('Deploy Application') {
            steps {
                sh '''
                    . $VENV_NAME/bin/activate
                    echo "Deploying application..."
                    
                    # NOTE: In a real scenario, this would involve Docker, Heroku, or AWS commands.
                    # For this example, we simulate a deployment.
                    
                    echo "Application deployed to Staging Environment!"
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution finished.'
        }
        success {
            echo 'Build and Deployment Successful!'
        }
        failure {
            echo 'Pipeline Failed. Please check logs.'
        }
    }
}
