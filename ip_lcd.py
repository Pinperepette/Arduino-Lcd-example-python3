#!/usr/bin/env python
# -*- coding: utf-8 -*-

# find it every 10 seconds and send it to the lcd

import serial , time, requests

port = '/dev/cu.usbmodem14301'

while True:
    s = serial.Serial(port, 9600) 
    r = requests.get('https://api.ipify.org')
    s.write(r.text.encode('utf-8'))
    time.sleep(10)

