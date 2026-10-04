docker 
docker exec -it  pathnext-nginx bash
docker stats

docker run -d --memory='512m' --cpus='1.0' nginx

#jenkins file -lambda function deployement pipline
pipeline {
agent:any
stages{
stage('build'){
steps{
echo 'build lambda function package...
sh 'zip -r lambda.zip lambda/

}
stage('deployee to lambda'){
steps{
scripts{
sh 'aws lambda update-function-cpde --function-name pathnext-lambda

}
}


}
#kubernate -deploy serveerless using kubless
apiversion:kubless.io/v1beta1
kind:function
metdata:
 name:pathnex-lambda
 namespcae:default
spec:
 runtime:nodejs14
 handler:index.handler
 function:[
  module.export =function(event,contetnt){
  contxt.succeed('hello world')
  }

  # Day 27 — Serverless Scaling with Lambda and DynamoDB
🔹 Ansible — Deploy Serverless Lambda Functions
- name: Deploy Serverless Lambda Function
  hosts: localhost
  tasks:
    - name: Create Lambda function
      command: aws lambda create-function --function-name pathnex-lambda --runtime nodejs14.x --role arn:aws:iam::123456789012:role/lambda-role --handler index.handler --zip-file fileb://lambda.zip
🔹 Terraform — Create DynamoDB Table for Serverless Application
resource "aws_dynamodb_table" "pathnex_table" {
  name           = "pathnex-table"
  hash_key       = "id"
  billing_mode   = "PAY_PER_REQUEST"
  attribute {
    name = "id"
    type = "S"
  }
}
🔹
