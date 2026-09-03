name:install nginx
host:
become:
task:
name:install nginx
yum:
  name:install nginx
  start:present



docker --version
docker run ubutu echo "hello pathnext"

from:ubuntu
cmd:["echo","pathnext"]
