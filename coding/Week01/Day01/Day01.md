day01 ansible +docker basic

ansible is automate server configure
docker is create and run container

ansible playbook

yaml
name:install nginx on pathnex server
server:all
become :yes

tasks:
   -name:install nginx
   yum:
     name:nginx
     state:present


lin1 name:install nginx server
# this is just the name/decription on the play

line2
host:all

beome:all

tasks:
 -name:install nginx

yum:
name:nginx
state:present
