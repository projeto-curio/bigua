#!/bin/bash

# Hello message
echo -e "\e[32m# Welcome to EasyWaze installer\e[0m"

# Check if is sudo
if [ "$EUID" -ne 0 ]
  then echo -e "\e[31m[ERROR] Please run as root\e[0m"
  exit
fi

export APP_NAME=bigua

# Create network
echo -e "\e[32mCreating network...\e[0m"
docker network create $APP_NAME >/dev/null 2>/dev/null || true

# Run main background process
docker run -d --restart=unless-stopped \
    --name $APP_NAME-main \
    --user=$USER_NAME \
    --network $APP_NAME \
    thenets/easywaze
