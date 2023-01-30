import tkinter as tk
from machine import Pin
import time

# Define pins for controlling the motor
IN1 = Pin(6, Pin.OUT)
IN2 = Pin(7, Pin.OUT)
EN_A = Pin(8, Pin.OUT)

# Function to stop the motor
def stop():
    IN1.value(0)
    IN2.value(0)

# Function to move the motor forward
def move_forward():
    IN1.value(1)
    IN2.value(0)

# Function to move the motor backward
def move_backward():
    IN1.value(0)
    IN2.value(1)

# Create the GUI
root = tk.Tk()
root.title("Motor Control")

# Add buttons for controlling the motor
stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack()

forward_button = tk.Button(root, text="Forward", command=move_forward)
forward_button.pack()

backward_button = tk.Button(root, text="Backward", command=move_backward)
backward_button.pack()

# Start the GUI
root.mainloop()

