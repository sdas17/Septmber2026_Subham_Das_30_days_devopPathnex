Day 23 — Serverless Architecture & Microservices

1. AWS Lambda

Goal: Deploy a Python Lambda function using AWS CLI.

Lambda structure
lambda/
├── lambda_function.py
└── requirements.txt

Example handler:

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from Pathnex Lambda!"
    }

aws lambda create-function \
  --function-name pathnex-lambda \
  --runtime python3.12 \
  --role arn:aws:iam::<ACCOUNT_ID>:role/lambda-execution-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://lambda.zip

    resource "aws_api_gateway_rest_api" "pathnex_api" {
  name        = "pathnex-api"
  description = "Pathnex API"
}
resource "aws_lambda_function" "pathnex_lambda" {
  function_name = "pathnex-lambda"
  runtime       = "python3.12"
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "lambda_function.lambda_handler"
  filename      = "lambda.zip"
}
resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id             = aws_api_gateway_rest_api.pathnex_api.id
  resource_id             = aws_api_gateway_resource.pathnex_resource.id
  http_method             = aws_api_gateway_method.pathnex_method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.pathnex_lambda.invoke_arn
}
helm install pathnex-microservice ./microservice-chart
helm list
kubectl get pods
kubectl get svc
kubectl get deployment

pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Lambda function...'
                sh 'zip -r lambda.zip lambda/'
            }
        }

        stage('Deploy to AWS Lambda') {
            steps {
                sh '''
                    aws lambda update-function-code \
                    --function-name pathnex-lambda \
                    --zip-file fileb://lambda.zip
                '''
            }
        }
    }
}

stages:
  - build
  - deploy

build:
  stage: build
  script:
    - zip -r lambda.zip lambda/

deploy:
  stage: deploy
  script:
    - aws lambda update-function-code
      --function-name pathnex-lambda
      --zip-file fileb://lambda.zip