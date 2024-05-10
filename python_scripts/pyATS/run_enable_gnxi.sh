#!/bin/bash
cd ~/pyats/
. bin/activate
python3 enable_gnxi.py | tee /tmp/`cat /etc/hostname`-c9300.log