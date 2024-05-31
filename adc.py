# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import socket
import struct

import datetime

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)
#print("{:>5}\t{:>5}".format("raw", "v"))

# while True:
#     #print("{:>5}\t{:>5.4f}".format(chan.value, chan.voltage))
#     voltageOut="{:5.10f}".format(chan.voltage)
#     print(voltageOut)   
# 
#     time.sleep(0.5)
    
    
#serverMACAddress = "40:ec:99:3e:6a:ce"
serverMACAddress = "48:e7:da:2e:f0:6c"
port = 4 
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))   
try:
    while 1:        
        #text = input()
        #if text == "quit":
        #    break
        #s.send(bytes(text, 'UTF-8'))
        voltageOut="{:5.10f}".format(chan.voltage)
        s.send(bytes(voltageOut), 'UTF-8')
        #print(s.send(bytes(str(chan.voltage), 'UTF-8')))
        time.sleep(0.5)
except Exception as e:
     # creating/opening a file
    f = open("/home/gbliao/log.txt", "a+") 
    # writing in the file
    t=datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S ")
    
    a=str(e)
    f.write(t+a+"\n")     
    # closing the file
    f.close() 
    print(e)
    s.close()
