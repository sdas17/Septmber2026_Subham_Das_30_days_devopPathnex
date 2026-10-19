docker --version
docker run ubntu echo "hello world"

From:ubuntu:22.04
cmd:['echo','hello pathnex']

name:install nginx
host:all
become:yes
tasks:
 -name:install nginx
  yum:
    name:nginx
    state:present
