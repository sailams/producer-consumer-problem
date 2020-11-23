# Producer-consumer-problem
Python Source code to solve producer consumer problem using Redis as Messaging Queue

# Pre-requisites:
You will need access to an Ubuntu 20.04 server that has a non-root with sudo privileges and a firewall configured with ufw. 

### Installing Instructions
* Step 1 — Update your local apt package cache: 
$sudo apt update

 * Step 2 - Install Redis by using the below command in the terminal
$ sudo apt install redis-server

* Step 3 - Install Python3.8 by using the below command in the terminal
$ sudo apt install python3.8 

* Step 4 - Check Redis and Python is UP and working
  To test that Redis is functioning correctly, connect to the server using redis-cli, Redis’s command-line client:
$redis-cli

* In the prompt that follows, test connectivity with the ping command:
$ping

* Expected Output
PONG

* Check python version by typing:
$python3.8 --version

### Set up
* Run producer process separate terminal using the below command
$ python3.8 Producer.py 
* Run consumer process in another terminal using the below command 
$ python3.8 Consumer.py

#Expected Output
* Produce shall produce random integer every second for consumer process to consume and print the smallest of 2 numbers consumed at any point of time.











