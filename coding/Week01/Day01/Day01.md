day01 ansible +docker basic

ansible is automate server configure
docker is create and run container

ansible playbook

NAME → HOSTS → BECOME → TASKS → MODULE → NAME → STATE

yaml
- name: Install nginx
  hosts: all
  become: yes

  tasks:
    - name: Install nginx
      yum:
        name: nginx
        state: present