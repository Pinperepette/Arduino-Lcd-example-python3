#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time

#set your port
port = '/dev/cu.usbmodem14301'

def scrivi():
    s = serial.Serial(port, 9600) 
    time.sleep(2) 
    s.write(('Ready...').encode('utf-8'))
    while True:
        str = input('Enter text: ').encode('utf-8')
        str = str.strip()
        if str == b'exit' :
            break
        s.write(str)

if __name__ == "__main__":
    scrivi()