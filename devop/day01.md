#ansible write yaml file 
name:install nginx
host:all
become:yes
tasks:
-name:insstall nginx
 yum:
  name:install yum
  state:present
 -name:install service
 service:
   name:nginx
   state:present
   enable:true
 
 #terraform
 provider "aws"{
region:"ap-south-1"



 }

 resource "aws-instance_type""pathnext-2"{
tag={
name='pathnext-ec2"

 }
ami:"ami-c2
instance type:"c2
 }

 ## 🔹 Kubernetes Task — Create Nginx Pod
 apiversion:v1
 kind:pod
 metadata:
 name:pathnex-pod
 spec:
  container:
   -name:web
   image:nginx:latest
   ports:
   port:8080
  #!/bin/bash
  echo "Date":${Date}"
  echo "Hostname:${Hostname}"
  pipline {
  agent any
  stages {
  stage('checkout'){
  steps{
   git branch :'main"  url: 'https://github.com/Pathnex/sample-java-app.git'


  }
 stage('list of file '){
 steps{
 sh "ls -lah"

 }


stages:
 -checkout
git-checkout:
 stage:script
 script:
  -git clone url
  -cd sample-url
  -ls -lah

