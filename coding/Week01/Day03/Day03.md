name:
host:
become
task:
  name:install nginx
  yum:
    name:install nginx
    state:present
  name: Start apache
   service:
    name:install nginx
    state:installed
    enable:true


provider "aws" :{
  region:"south"
}
resource "aws_instance" "PathnexEC2" {
  ami           = "ami-0abcd1234abcd1234"
  instance_type = "t3.medium"
  tags = {
    Name = "Pathnex-T3"
  }
}

apiVersion
    ↓
Kubernetes ko API version batao

kind
    ↓
Deployment create karo

metadata
    ↓
Deployment ka naam
pathnex-deployment

spec
    ↓
Deployment ko kya karna hai?

replicas: 2
    ↓
2 Pods maintain karo

selector
    ↓
Kaunse Pods manage karne hain?
app=pathnex-app

template
    ↓
Pod ka blueprint

🔹 Kubernetes — Create a ReplicaSet with 3 Replicas
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: pathnex-replicaset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: pathnex-app
  template:
    metadata:
      labels:
        app: pathnex-app
    spec:
      containers:
        - name: app
          image: nginx
          ports:
            - containerPort: 80

🔹 Docker
# Docker File for Nginx Web Server
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html

# HTML
<h1>Hello Pathnex</h1>

# Bash
# Real Path
/usr/share/nginx/html

# Bash
docker build -t pathnex-nginx .
docker run -d -p 80:80 pathnex-nginx

metadata
    ↓
Pod ki information

labels
    ↓
Pod ki identity
app=pathnex-app

spec
    ↓
Pod ke andar kya run karna hai?

containers
    ↓
Container define karo

name
    ↓
Container ka naam

image
    ↓
Nginx image use karo

ports
    ↓
Container ka port

containerPort: 80
    ↓
Nginx port 80
