-
 name:install nginx
 host:all
 become:yes
tasks:
  -name:install nginx
   yum:
     name:nginx
     state:present

--
docker --version
docker run ubuntu echo "hello pathnext"

FROM node:22
WORKDIR /app
COPY package.json
RUN npm install
COPY ..
EXPOSE 8080
CMD ["npm","start"]