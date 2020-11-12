# producer-consumer-problem
Python Source code to solve producer consumer problem using Redis as Messaging Queue


Prerequisites:
You will need access to an Ubuntu 20.04 server that has a non-root with sudo privileges and a firewall configured with ufw. 

Step 1 — Installing Redis & Python3.8
Begin by updating your local apt package cache:
sudo apt update

Then install Redis by typing:
sudo apt install redis-server

Then install Python3.8 by typing:
sudo apt install python3.8 

Step 2 - Test Redis and Python is working 
To test that Redis is functioning correctly, connect to the server using redis-cli, Redis’s command-line client:
redis-cli

In the prompt that follows, test connectivity with the ping command:
ping

Expected Output
PONG

Check python version by typing:
python3.8 -V

Step 3 - Run producer process and consumer process in separate terminal using the below command

python3.8 Producer.py (one terminal) and python3.8 Consumer.py (another terminal)











