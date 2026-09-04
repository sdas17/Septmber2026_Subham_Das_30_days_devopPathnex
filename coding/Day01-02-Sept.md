name:install nginx
host:yes
become:all
-name:install nginx
   yum:
      name:install nginx
      state:present

docker --version
docker  run image echo "hellow world"


# Docker File
FROM ubuntu:22.04
CMD ["echo", "Hello Pathnex"]