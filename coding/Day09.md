day -09 

Day 09 — Docker Integration with Jenkins & GitLab
🔹 Ansible — Setup Docker Container for Nginx
- name: Setup Docker Container for Nginx
  hosts: all
  become: yes
  tasks:
    - name: Pull Nginx image
      docker_image:
        name: nginx
        source: pull
    - name: Run Nginx container
      docker_container:
        name: nginx-container
        image: nginx
        state: started
        published_ports:
          - "8080:80"

    🔹 Kubernetes — Horizontal Pod Autoscaler (HPA)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pathnex-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pathnex-app
  template:
    metadata:
      labels:
        app: pathnex-app
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
🔹 GitLab CI/CD — Deploy to Kubernetes
stages:
  - deploy

deploy:
  stage: deploy
  script:
    - kubectl apply -f kubernetes/deployment.yaml


🔹 Docker
# Environment Variables
FROM ubuntu:22.04
ENV INSTITUTE=Pathnex
ENV COURSE=DevOps
CMD echo "$INSTITUTE - $COURSE"