et up the ExecScripts directory
cp -r ../../ExecScripts /tmp

# Setup Daytona sarmonitor
cp -r ../../Scheduler+Agent/daytona_sarmonitor /tmp

# Install sysstat for sar and iostat
sudo yum install sysstat -y

cd ../../Scheduler+Agent

# Start Agent
nohup python ./agent.py &
