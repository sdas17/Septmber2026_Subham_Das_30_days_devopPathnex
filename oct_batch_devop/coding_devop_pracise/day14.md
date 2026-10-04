# Configure AWS Provider
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "pathnex" {
  ami           = "ami-0f559c3642608c138"
  instance_type = "t3.micro"
  count         = 1

  key_name = "pathnextaugust"

  subnet_id = "subnet-025ab06378fcd0dce"

  vpc_security_group_ids = ["sg-0deca6ca57c31e8e3"]
  tags = {
    Name = "pathnex"
  }
}

output "ec2_public_ips" {
  value = aws_instance.pathnex[*].public_ip
}

docker code 
from:
Entrypoint
cmd

 GitLab CI/CD — Multi-Stage Deployment with Helm
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
    - helm upgrade --install pathnex-nginx pathnex/nginx-ingress

