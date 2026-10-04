name:install docker 
host:yes
become:all
task:
  -name:install docker
   yum
     name:install docker
     state:present
     service:
      name:docker
      state:start
      enable:true
resource "aws_vpc""main"{
    cidr_block="10.0.0.0/15"
}
resource "aws_instance""pathnex_ec2"{
 ami=
 instance_type
 subnet_id
 tags={
 name:'sd
 }
}
  
Kubernetes — Pod with Volume Mount
apiVersion: v1
kind: Pod
metadata:
  name: pathnex-pod
spec:
  containers:
    - name: web
      image: nginx
      volumeMounts:
        - mountPath: /usr/share/nginx/html
          name: html-volume
  volumes:
    - name: html-volume
      hostPath:
        path: /data
        type: Directory


🔹 Shell Script — Check for Running Services
#!/bin/bash
services=("nginx" "docker" "httpd")
for service in "${services[@]}"
do
  if systemctl is-active --quiet $service; then
    echo "$service is running"
  else
    echo "$service is not running"
  fi
done

🔹 Docker
# Node.js Application (JavaScript)
console.log("Hello Pathnex");

# Docker File
FROM node:18
WORKDIR /opt/pathnex/node-app
COPY app.js /opt/pathnex/node-app/
CMD ["node", "/opt/pathnex/node-app/app.js"]

# Real Path
/opt/pathnex/node-app

