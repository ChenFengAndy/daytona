#!/bin/bash

# Set up the ExecScripts directory
cp -r ../../ExecScripts /tmp

# Setup Daytona sarmonitor
cp -r ../../Scheduler+Agent/daytona_sarmonitor /tmp

# Install sysstat for sar and iostat
sudo apt-get install sysstat -y
sudo apt-get install python-requests

sudo apt-get install python-mysql.connector -y
sudo apt-get install strace

cd ../../Scheduler+Agent

# Start Agent
sudo nohup python ./agent.py > agent_nohup.out 2>&1 &