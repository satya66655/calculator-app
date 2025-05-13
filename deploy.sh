#!/bin/bash

sudo yum install -y python3 git
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install Flask

sudo pkill -f app.py || true
rm -rf calculator-app
git clone https://github.com/satya66655/calculator-app.git
cd calculator-app
nohup sudo python3 app.py > app.log 2>&1 &

