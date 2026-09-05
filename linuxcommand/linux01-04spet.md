1. File & Directory Commands
Command	Definition	Example
ls	Lists files and directories	ls
ls -l	Lists files in long format with permissions, owner, group, size, date	ls -l
ls -a	Shows hidden files also	ls -a
ls -la	Long format + hidden files	ls -la
ls -lh	Long format with human-readable sizes	ls -lh
ls -lah	Long format + hidden files + human-readable sizes	ls -lah
ls -lS	Lists files in long format, sorted by size	ls -lS
ls -lt	Lists files sorted by modification time	ls -lt
pwd	Prints the current working directory	pwd
cd	Changes the current directory	cd /tmp
mkdir	Creates a directory	mkdir test
touch	Creates an empty file or updates its timestamp	touch file.txt
cat	Displays file contents; can also concatenate files	cat file.txt
file	Displays the type of a file	file test.txt
rm	Removes files	rm file.txt
rm -r	Removes directories and their contents recursively	rm -r test/
mv	Moves or renames files/directories	mv old.txt new.txt
2. Linux File Permissions

Linux permissions have 3 categories:

Owner    Group    Others
 rwx      rwx       rwx

Permission values:

r = read    = 4
w = write   = 2
x = execute = 1

Example:

chmod 444 file.txt

Means:

Owner  = read
Group  = read
Others = read

So:

444 = r-- r-- r--
chmod

Changes file or directory permissions.

chmod 755 script.sh

Means:

Owner  = rwx = 7
Group  = r-x = 5
Others = r-x = 5
3. Ownership
chown

Changes the owner of a file/directory.

chown user file.txt

Change owner and group:

chown user:group file.txt
chgrp

Changes the group ownership.

chgrp developers file.txt
4. Links
Hard Link

A hard link is another directory entry pointing to the same inode/data.

ln file.txt hardlink.txt
Soft Link / Symbolic Link

A soft link is a pointer/reference to another file.

ln -s file.txt softlink.txt

Remember:

Hard link  → same inode
Soft link  → points to pathname
5. Paths
Absolute Path

Path starting from the root /.

/home/user/file.txt
Relative Path

Path relative to your current directory.

./file.txt
../file.txt
6. grep

grep searches for a pattern/text inside files or command output.

grep "error" logfile.txt

Example:

ls -l | grep file.txt

This searches the ls -l output for file.txt.

7. head

Displays the beginning of a file.

head file.txt

Show first 5 lines:

head -n 5 file.txt
8. tail

Displays the end of a file.

tail file.txt

Show last 5 lines:

tail -n 5 file.txt

Very important for DevOps:

tail -f application.log

Continuously watches new log entries.

9. find

find searches for files and directories based on conditions such as name, type, size, permissions, etc.

Example:

find . -type f

Find files by name:

find . -name "*.log"

Find directories:

find . -type d

Find top 10 largest files:

find . -type f -printf "%s %p\n" | sort -nr | head -10

Here:

%s → file size
%p → file path
10. sed

sed is a stream editor used to search, replace, delete, or modify text.

Replace first occurrence in each line:

sed 's/old/new/' file.txt

Replace all occurrences:

sed 's/old/new/g' file.txt

Modify the file directly:

sed -i 's/old/new/g' file.txt
11. awk

awk is a text-processing and data-extraction tool, commonly used to work with columns/fields.

Example:

awk '{print $1}' file.txt

Prints the first column.

awk '{print $1, $3}' file.txt

Prints the first and third columns.

12. umask

umask controls the default permissions of newly created files and directories.

Check:

umask

Example:

umask 022

Default maximum permissions:

File       = 666
Directory  = 777

With umask 022:

File       → 644
Directory  → 755

Remember:

File:       666
Directory:  777
umask 022
13. Archive Commands
zip

Creates a ZIP archive.

zip files.zip file1.txt file2.txt
unzip

Extracts a ZIP file.

unzip files.zip
tar

Used to archive multiple files/directories and commonly combine archiving with compression.

Common:

tar -cvf archive.tar folder/

For gzip:

tar -czvf archive.tar.gz folder/

For bzip2:

tar -cjvf archive.tar.bz2 folder/

For xz:

tar -cJvf archive.tar.xz folder/

Remember the common options:

c = create
x = extract
v = verbose
f = file
z = gzip
j = bzip2
J = xz
14. Process Management
ps

Displays information about running processes.

ps

Common:

ps aux

Shows processes for all users with detailed information.

top

Displays real-time process, CPU, memory, and system-load information.

top
kill

Sends a signal to a process.

kill PID

Forcefully terminate:

kill -9 PID

-9 sends SIGKILL.

pkill

Kills processes based on their name/pattern.

pkill nginx
pgrep

Finds the PID of processes based on name/pattern.

pgrep nginx

Easy way to remember:

ps     → see processes
top    → monitor processes
pgrep  → find PID
pkill  → kill by name
kill   → kill by PID
15. Terraform Commands You've Learned
Command	Definition
terraform init	Initializes the Terraform working directory and downloads required providers/modules
terraform plan	Shows what Terraform plans to create, modify, or destroy
terraform apply	Applies the Terraform configuration and creates/changes infrastructure
terraform destroy	Destroys infrastructure managed by Terraform

The basic Terraform lifecycle:

terraform init
       ↓
terraform plan
       ↓
terraform apply
       ↓
terraform destroy
mkdir day{01..02}.md

find 

find . name e*
find . type  Day*

size 

