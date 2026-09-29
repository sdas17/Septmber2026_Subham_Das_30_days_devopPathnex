docker compose up

version:'2'
 services:
   web:
    image:
    container_name:
    ports:
     -'80'-80
 stages:
  - backup
  - restore

backup:
  stage: backup
  script:
    - tar -czvf /tmp/backup.tar.gz kubernetes/deployment.yaml

restore:
  stage: restore
  script:
    - tar -xzvf /tmp/backup.tar.gz -C kubernetes/

  pipeline {
    agent any
    stages {
        stage('Backup') {
            steps {
                echo 'Backing up Jenkins workspace...'
                sh 'tar -czvf /tmp/jenkins-backup.tar.gz ${WORKSPACE}'
            }
        }
        stage('Restore') {
            steps {
                echo 'Restoring Jenkins workspace...'
                sh 'tar -xzvf /tmp/jenkins-backup.tar.gz -C ${WORKSPACE}'
            }
        }
    }
}

- name: Backup and Restore Files
  hosts: all
  become: yes
  tasks:
    - name: Create backup of /etc directory
      command: tar -czvf /tmp/etc-backup.tar.gz /etc
    - name: Copy backup to remote server
      copy:
        src: /tmp/etc-backup.tar.gz
        dest: /tmp/etc-backup.tar.gz
    - name: Restore backup from remote server
      command: tar -xzvf /tmp/etc-backup.tar.gz -C /
🔹 Terraform — Create S3 Bucket with Cross-Region Replication
resource "aws_s3_bucket" "pathnex_bucket" {
  bucket = "pathnex-backup-bucket"
  region = "us-east-1"

  versioning {
    enabled = true
  }
}

resource "aws_s3_bucket" "pathnex_backup_bucket_eu" {
  bucket = "pathnex-backup-bucket-eu"
  region = "eu-west-1"

  versioning {
    enabled = true
  }
}

resource "aws_s3_bucket_object" "pathnex_backup_file" {
  bucket = aws_s3_bucket.pathnex_bucket.bucket
  key    = "backup.tar.gz"
  source = "pathnex-backup.tar.gz"
}
