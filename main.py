# movements for the bioreactor 

# we are going to want to start with ensuring that the pump is completely off first
from machine import Pin
import time  # inserting time delay
import serial  # will need this for comport connection to the DUT

# this will be the class that we end up calling too
# this file where be where the functions will be stored and then imported into
# the running file itself

# OUT1  and OUT2
In1 = Pin(6, Pin.OUT),
In2 = Pin(7, Pin.OUT),
EN_A = Pin(8, Pin.OUT),

# need a comport connection, can be either direct or pulled from a different file
ser = serial.Serial('COM4')
print(ser.name)
ser.read(3)


# Stop
def stop():
    In1.low()
    In2.low()

stop()


# Forward
def move_forward():

    In1.high()
    In2.low()


# Backward
def move_backward():
    In1.low()
    In2.high()


'''
#Ask for user input for which mode they would want to run

user_mode = input("1-Forward\n2-Reverse\n3-Pulsality\n")
user_time = input("Enter time duration in seconds: ")

 f user_mode == 1:  # condition in this case
'''


'''
user_mode1 = input("1-Forward\n2-Reverse\n3-Pulsality\n")
user_tim1 = input("Input time in seconds ")

while True:
    stop()
    if user_mode1 == 1:
        move_forward()
        time.sleep(10)
'''

stop()
