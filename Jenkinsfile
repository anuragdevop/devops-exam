pipeline {
    agent any

    environment {
        AWS_REGION = "ap-south-1"
        S3_BUCKET = "467.devops.candidate.exam"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/anuragdevop/devops-exam.git'
            }
        }

        stage('Terraform Init') {
            steps {
                sh 'terraform init -backend-config="bucket=${S3_BUCKET}"'
            }
        }

        stage('Terraform Validate') {
            steps {
                sh 'terraform validate'
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
                sh '''
                zip -r lambda.zip lambda_function.py
                aws lambda update-function-code --function-name candidate_lambda --zip-file fileb://lambda.zip --region ${AWS_REGION}
                '''
            }
        }

        stage('Invoke Lambda') {
            steps {
                script {
                    def response = sh(script: 'aws lambda invoke --function-name candidate_lambda --log-type Tail lambda_response.json --region ${AWS_REGION}', returnStdout: true).trim()
                    echo "Lambda Response: ${response}"
                }
            }
        }
    }
}

