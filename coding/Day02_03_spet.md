# Day 02 — Services & Tags

## 1. Ansible — Install & Enable Nginx

```yaml
- name: Install and start Nginx on Pathnex
  hosts: all
  become: yes

  tasks:
    - name: Install nginx
      yum:
        name: nginx
        state: present

    - name: Enable nginx
      service:
        name: nginx
        state: started
        enabled: yes
```

### Remember

```text
yum      → Install package
present  → Package should be installed
service  → Manage service
started  → Start service now
enabled  → Start service automatically after reboot
become   → Run with elevated privileges
```

---

## 2. Terraform — EC2 with Tags

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "PathnexEC2" {
  ami           = "ami-0abcd1234abcd1234"
  instance_type = "r5.2xlarge"

  tags = {
    Name        = "Pathnex-Server"
    Environment = "Training"
    Owner       = "PathnexStudent"
  }
}
```

### Remember

```text
provider       → AWS
region         → Where to create the resource
aws_instance   → EC2
ami            → OS/image
instance_type  → EC2 size
tags           → Identify/organize the resource
```

⚠️ `ami-0abcd1234abcd1234` is an example placeholder. You must use a **real AMI ID available in `us-east-1`** before running `terraform apply`.

---

## 3. Kubernetes — Deployment with 2 Replicas

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: pathnex-deployment

spec:
  replicas: 2

  selector:
    matchLabels:
      app: pathnex-app

  template:
    metadata:
      labels:
        app: pathnex-app

    spec:
      containers:
        - name: app
          image: nginx
          ports:
            - containerPort: 80
```

### Remember the structure

```text
Deployment
   ↓
replicas: 2
   ↓
Pod Template
   ↓
Container
   ↓
nginx
   ↓
Port 80
```

Important:

```yaml
selector:
  matchLabels:
    app: pathnex-app
```

must match:

```yaml
template:
  metadata:
    labels:
      app: pathnex-app
```

---

## 4. Shell Script — Disk Usage

```bash
#!/bin/bash

df -h
```

### What it does

`df -h` displays filesystem disk usage in a human-readable format.

Example:

```text
Filesystem   Size   Used   Avail   Use%
/dev/sda1     50G    20G     30G    40%
```

Remember:

```text
df → Disk/filesystem usage
-h → Human readable
```

---

## 5. Docker — Images & Containers

### Download Ubuntu image

```bash
docker pull ubuntu
```

### List Docker images

```bash
docker images
```

### List all containers

```bash
docker ps -a
```

Remember:

```text
docker pull  → Download image
docker images → List images
docker ps    → Running containers
docker ps -a → All containers
```

---

## 6. Dockerfile

```dockerfile
FROM ubuntu:22.04

RUN apt update

CMD ["echo", "Hello Pathnex"]
```

### Dockerfile instructions

```text
FROM → Base image
RUN  → Execute command while building image
CMD  → Default command when container starts
```

### Build the image

```bash
docker build -t pathnex-app .
```

### Run the container

```bash
docker run pathnex-app
```

Expected output:

```text
Hello Pathnex
```

---

# Day 02 Quick Revision

| Technology     | What you learned                  |
| -------------- | --------------------------------- |
| **Ansible**    | Install, start and enable Nginx   |
| **Terraform**  | Create EC2 and add tags           |
| **Kubernetes** | Deployment with 2 replicas        |
| **Shell**      | Check disk usage with `df -h`     |
| **Docker**     | Images, containers and Dockerfile |

## Interview Memory Trick

```text
Ansible    → Configure
Terraform  → Provision
Kubernetes → Orchestrate
Docker     → Containerize
Shell      → Automate
```
