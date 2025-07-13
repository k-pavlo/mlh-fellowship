#!/bin/bash

# go into the project folder
cd /root/mlh-fellowship/

# fetch the latest changes
git fetch && git reset origin/main --hard

# enter the python virtual environment
source python3-virtualenv/bin/activate

# make sure all required dependencies are installed 
pip install -r requirements.txt

# restart myportfolio service
systemctl daemon-reload
systemctl restart myportfolio
