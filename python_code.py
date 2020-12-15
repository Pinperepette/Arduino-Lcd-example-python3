#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time

#set your port
port = '/dev/cu.usbmodem14301'

# use it to type from keyboard in real time
def scrivi_da_tastiera():
    s = serial.Serial(port, 9600) 
    time.sleep(2) 
    s.write(('Ready...').encode('utf-8'))
    while True:
        str = input('Enter text: ').encode('utf-8')
        str = str.strip()
        if str == b'exit' :
            break
        s.write(str)

# from python_code import scrivi_come_modulo as arw
# use it to interact with your projects

def scrivi_come_modulo(text):
    s = serial.Serial(port, 9600) 
    time.sleep(2) 
    str = text.encode('utf-8')
    str = str.strip()
    s.write(str)
      

if __name__ == "__main__":
    scrivi_da_tastiera()