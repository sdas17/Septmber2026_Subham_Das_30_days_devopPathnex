#Docker 
#expose port mapping
From nginx
Expose 80
docker run -d -p 8080:90 nginx

 # GitLab CI/CD — Build, Push, and Deploy with Helm
 stage
 build
 push
 deployee

 #Jenkinsfile — Multi-Stage Pipeline

 pipeline create 
 check they code github
 build docker iamge
 push they docker image
 deployee kubernate

 🔹 Ansible — Install Helm on Server
- name: Install Helm
  hosts: all
  become: yes
  tasks:
    - name: Download Helm
      get_url:
        url: https://get.helm.sh/helm-v3.7.0-linux-amd64.tar.gz
        dest: /tmp/helm.tar.gz

    - name: Extract Helm
      unarchive:
        src: /tmp/helm.tar.gz
        dest: /usr/local/bin/
        remote_src: yes

    - name: Set Helm binary permissions
      file:
        path: /usr/local/bin/helm
        mode: '0755'
🔹 Terraform — Provision EC2 with Elastic IP
resource "aws_eip" "pathnex_eip" {
  instance = aws_instance.pathnex_ec2.id
}

resource "aws_instance" "pathnex_ec2" {
  ami           = "ami-0abcd1234abcd1234"
  instance_type = "t3.medium"
  
  tags = {
    Name = "Pathnex-EC2"
  }
}
