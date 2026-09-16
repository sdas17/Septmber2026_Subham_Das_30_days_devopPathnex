#gitlab
stages:
   -build
   -push
   -deployee

-build
   stage:build
   scripts:docker build -t my_app
-push
   stage:push
   scripts:docker push -t my_app
-deployee
   stage:deployee
   scripts:kubtecl apply  -f app.yaml 

🔹 GitLab CI/CD — Environment-Specific Deployments
stages:
   -build
   -push
   -deployee
build:
  stage:build
  script:docker build -t my-app
push :
  stage:push
  script:docker push my-app
deployee:
 stage:deployee
 script:kubetcl apply -g my_app.yaml

 pipeline {
  agent any
  stages{
   stage('build'){
    steps {
       echo 'Building Docker image'
                sh 'docker build -t pathnex-web-app .'
    }
    stage('test){
      steps{
         echo 'Running tests'
      }
    }
    stage('deploye'){
      steps{
         sh 'kubectl apply -f deployment.yaml'
      }

    
    }
   }
  }
 }

 FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]


Day 15 — Automation with Terraform, Ansible, and CI/CD Pipelines
🔹 Ansible — Deploy a Web Application to Multiple Hosts
- name: Deploy web application to multiple hosts
  hosts: all
  become: yes
  tasks:
    - name: Copy web app files
      copy:
        src: /path/to/web/app/
        dest: /var/www/html/
    - name: Start web app service
      service:
        name: apache2
        state: started
        enabled: yes
🔹 Terraform — Create EC2 with ALB (Application Load Balancer)
resource "aws_lb" "pathnex_lb" {
  name               = "pathnex-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.allow_ssh_http.id]
  subnets            = [aws_subnet.public.id]
}

resource "aws_instance" "pathnex_ec2" {
  ami             = "ami-0abcd1234abcd1234"
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.allow_ssh_http.name]

  tags = {
    Name = "Pathnex-EC2"
  }
}