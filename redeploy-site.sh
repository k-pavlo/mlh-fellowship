#!/bin/bash

# go into the project folder
cd /root/mlh-fellowship/

# fetch the latest changes
git fetch && git reset origin/main --hard

# spin containers down to prevent out of memory issues
docker compose -f docker-compose.prod.yml down

# rebuild and spin up containers 
docker compose -f docker-compose.prod.yml up -d --build
