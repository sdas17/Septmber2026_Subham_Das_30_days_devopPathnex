#  just learn how to create yaml file
apiversion:v1
kind:service
metadata:tcs
spec:
   selector:
     app:nginx
   ports:
     por:8080
     targethost:8781
#kind 
service
pod
configmap
secreat

metadata
===
#resource ka naam kiya haine
name 
#resource kanha par haine
namespace
label

spec:
 selector : kis pod pakdna hane
 ports: kid pod ka port haine
Day 13 — Advanced Automation with CloudFormation and CI/CD
name:
host:
become:
task:
  name:
  yum:
   name:
   state:

  name:
  serive:
    name:
    state:
    enable

🔹 Terraform — Create IAM Users and Policies

resource "aws_iam_policy" "iam_policy:{
  name:
  description:
  poicy: jsonEncode({
    statement=[
      {
        Affect:"s3-list-bucket"
        action:allow
        resource:
      }
    ]
  })

}
🔹 Kubernetes — Deploy Nginx with ConfigMap and Secrets
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
data:
  nginx.conf: |
    server {
      listen 80;
      server_name localhost;
      location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
      }
    }
    github ci and cd
    stages:
    build
    push
   build:
  stage: build
  script:
    - docker build -t pathnex-web-app .

push:
  stage: push
  script:
    - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD"
    - docker push pathnex-web-app

deploy:
  stage: deploy
  script:
    - helm repo add pathnex https://charts.pathnex.com
    - helm install pathnex-nginx pathnex/nginx-ingress

    🔹 Docker
# COPY vs ADD
FROM ubuntu
COPY pathnex-file.txt /opt/pathnex/files/
ADD pathnex.tar.gz /opt/pathnex/extracted/