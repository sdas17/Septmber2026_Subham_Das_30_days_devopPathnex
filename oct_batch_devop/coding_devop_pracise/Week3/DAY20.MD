#git lab cicd
stages
 -build
 -push
 -deployee

build:
stage:build
build:
   docker build -t application_name
push:
 stage:push
 script:
   docker push application_name
 deployee:
 stage:deployee
 script:
   kubectl apply -f tag_name.yml
   kubectl get pods --watch

name:configuration firewall with iptable
host:all
become:yes
tasks:
   - name: Set default policies to drop all traffic
      command: iptables -P INPUT DROP
    - name: Allow SSH and HTTP traffic
      command: iptables -A INPUT -p tcp --dport 22 -j ACCEPT
      command: iptables -A INPUT -p tcp --dport 80 -j ACCEPT
    - name: Save iptables configuration
      command: service iptables save

 resource "aws-security-group""path_next"{ name_prefix = "pathnex-sg-"
  description = "Allow SSH and HTTP"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  }
  docker createnetwork pathnext
  docker run  --dit  --name c1  --newtwork pathnex-network ubnuty

