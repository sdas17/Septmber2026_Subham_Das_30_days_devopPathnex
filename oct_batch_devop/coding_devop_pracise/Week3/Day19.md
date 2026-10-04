#learn ansible command (22-09-2026)
#ansible is agent less command
#only for sst port is open 
ssh port 22 
if we change port 2205 changes configuration file
linux 
window winrm 5985 http
window winrm 5956 https
ansible puppet and chef pull based 

---
-- name:install prometuse for monitoring
   hosts:all
   become:yes
   tasks:
       -name:install Promotheus depdencies
        yum:
	  -promtheus
	  -promethus-node-exporter
	  state:present
       -name:start promotheus service
        service:
	   name:prometus
	   state:started
	   enable:yes

#terraform -setup aws cloud watch for monitoring
resource "aws-cloudwatch_log_group" "pathnex_log_group"{ name="pathnex-log-group"
}
resource "aws_cloudwatch_log_stream" "pathnex_log_stream"{log_group_name= aws_cloudwatch_log_group.patxhnex_log_group.name
name="pathnex-log-stream"
}
#kubernates -Deploy Fluentd for loggin
apiVersion:app/v1
kind:deployment
metdata:
   name:fluentd
spec:
  replicas:1
  selector:
    mathchLabels:
       app:fluentd
remplate:
  metdata:
   labels:
     app:fluentd
 spec:
   containers:
    -name:fluentd
      image:fluent/fluentd
      ports:
        -continerPort:2424
---
apiversion:v1
kind:Service
metdata:
 name:fluentd
spec:
 selector:
   app:fluentd
 ports:
  -protocol:TCP

🔹 Jenkinsfile — Integrating Prometheus Monitoring in Pipeline
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                docker.build('pathnex-web-app')
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Monitor Deployment') {
            steps {
                script {
                    sh 'kubectl apply -f kubernetes/deployment.yaml'
                    sh 'kubectl get pods --watch'
                }
            }
        }
    }
}
#gitlab cicd 
stages:
 -build
 -push
 -deployee
build:
  stage:build
  scripts:
    -docker build -t application
push:
 stage:push
 script:
  - docker login -u "$ci_Registry_user" -p $ci_registry_passoerd"
  -docker push applciation
deployee:
 stage:deployee
 script:
  kubectl apply -f kubeenrate/deployment.yaml
  kubectl get pords --watch

#fast api application 
from fastapi import FastAPI
app=FASTAPI()
@app.get("/")
def get_home():
    return "helllow wordl"
 
#docker file 
FROM python:3.11
workdir /opt/pathnex/fast_app
Copy ..
RUN pip install api:uvicorn --reload 
CMD:["python","opt/pathnex/fast-app/"]


