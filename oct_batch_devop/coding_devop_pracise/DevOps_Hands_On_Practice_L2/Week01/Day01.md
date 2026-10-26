Docker 
docker --version
docker run ubuntu echo hello_pathnet

From ubtuntu:22.00.4
cmd ['echo','hello pathnexxt']

name:install nginx
host:all
become:yes
tasks
  -name: install ngix
  yum:
   name:nginx
   state:present

