##state present,absent,started,stopped
##enable true and false

name: Install Nginx on Pathnex server
  hosts: all
  become: yes

  tasks:
    - name: Install nginx
      yum:
        name: nginx
        state: present

   docker --version
   docker run ubantu echo "hello world"
   FROM UBANTU 2.
   CMD ["echo", "Hello Pathnex"]
