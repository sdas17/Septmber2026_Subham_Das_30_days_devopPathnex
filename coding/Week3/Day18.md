#Docker 
docker run -d --name pathnex-redix redis

#check docer version
docker --version

docker images
docker pull

#remove images
docker rmi nginx

docker build -t my_app:100

docker run -d --name pathnex-redix redx


doker run -d --name my-ngix -p 8080:9090

docker ps
docker logs --tail 200 container name


🔹 Kubernetes — Horizontal Pod Autoscaler with Multiple Replicas

apiversion:app/v1
kind:Deployment
metadata:
  name:pathnex-web-app
spec:
  replica:3

  selector:
    mathchlabel:
       name:path-app
   template:
      metdata:
        label:
	  name:path-app
   spec:
      container:
       - name:path-nex_app
	images:nginx
     ports: 
       containerport:9090

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: pathnex-web-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: pathnex-web-app
  minReplicas: 2
  maxReplicas: 10


# terraform 

terraform {
required_provider{
aws={
source="hasicorp/aws"
version="~>5.0"

}

}
provider{
region="ap-south-1"

}

resource "aws-lb""app"{
loadbalncer:
securitygroup:
name:
internal:
}

resource "aws_autoscaling_group" "pathnex_asg" {
  desired_capacity     = 3
  max_size             = 5
  min_size             = 2
  vpc_zone_identifier  = [aws_subnet.public.id, aws_subnet.public2.id]
  launch_configuration = aws_launch_configuration.pathnex_config.id
}
 name: Setup HAProxy Load Balancer
  hosts: all
  become: yes
  tasks:
    - name: Install HAProxy
      yum:
        name: haproxy
        state: present
    - name: Configure HAProxy
      template:
        src: haproxy.cfg.j2
        dest: /etc/haproxy/haproxy.cfg
    - name: Start HAProxy service
      service:
        name: haproxy
        state: started
        enabled: yes


stages:
  - build
  - push
  - deploy

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
    - kubectl apply -f kubernetes/blue-deployment.yaml
    - kubectl apply -f kubernetes/green-deployment.yaml
    - kubectl rollout status deployment/blue-deployment
    - kubectl rollout status deployment/green-deployment


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
        stage('Blue-Green Deployment') {
            steps {
                script {
                    sh 'kubectl apply -f kubernetes/blue-deployment.yaml'
                    sh 'kubectl apply -f kubernetes/green-deployment.yaml'
                    sh 'kubectl rollout status deployment/blue-deployment'
                    sh 'kubectl rollout status deployment/green-deployment'
                }
            }
        }
    }
}



