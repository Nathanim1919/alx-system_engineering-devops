0x0D. Web stack debugging #0
Description
The "Web stack debugging" series is designed to train in the art of debugging. In this project, the goal is to bring a webstack to a working state by manually fixing issues and then creating a Bash script to automate the process.

Tasks
0. Give me a page!
Objective: Get Apache to run on the container and return a page containing "Hello Holberton" when querying the root.

Example:

bash
Copy code
docker run -p 8080:80 -d -it holbertonschool/265-0
docker ps
curl 0:8080
Expected Output:

Copy code
Hello Holberton
Requirements
Allowed editors: vi, vim, emacs
Files interpreted on Ubuntu 14.04 LTS
All files should end with a new line
README.md file at the root is mandatory
Bash script files must be executable
Bash scripts must pass Shellcheck without any error
Bash scripts must run without error
First line of all Bash scripts should be #!/usr/bin/env bash
Second line of all Bash scripts should be a comment explaining the script's purpose
Installation
For this project, you will be given a container that you can use to solve the task. If you want to experiment or solve the problem locally, you can install Docker on your machine, Ubuntu 14.04 VM, or Ubuntu 16.04 VM if upgraded.

Docker Installation - Mac OS
Docker Installation - Windows
Docker Installation - Ubuntu 14.04
Docker Installation - Ubuntu 16.04
Resources
curl command
