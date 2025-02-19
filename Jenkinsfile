pipeline {
    agent any

    environment {
        AWS_REGION = "ap-south-1"
        S3_BUCKET = "467.devops.candidate.exam"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/anuragdevop/devops-exam.git'
            }
        }

        stage('Terraform Init') {
            steps {
                sh 'terraform init'
            }
        }

        stage('Terraform Plan') {
            steps {
                sh 'terraform plan'
            }
        }

        stage('Terraform Apply') {
            steps {
                sh 'terraform apply -auto-approve'
            }
        }

        stage('Deploy Lambda') {
            steps {
                sh 'zip -r lambda.zip lambda_function.py'
                sh 'aws lambda update-function-code --function-name candidate_lambda --zip-file fileb://lambda.zip'
            }
        }

        stage('Invoke Lambda') {
            steps {
                script {
                    def response = sh(script: 'aws lambda invoke --function-name candidate_lambda --log-type Tail lambda_response.json', returnStdout: true).trim()
                    echo "Lambda Response: ${response}"
                }
            }
        }
    }
}

