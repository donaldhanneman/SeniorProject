import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number for the PWM output
GPIO.setmode(GPIO.BOARD)
pwm_pin = 8
GPIO.setup(pwm_pin, GPIO.OUT)

# Set the PWM frequency to 70 beats per minute (1 beat per 0.857 seconds)
pwm_frequency = 1 / 0.857
pwm = GPIO.PWM(pwm_pin, pwm_frequency)

# Start the PWM with a duty cycle of 0%
pwm.start(0)

try:
    while True:
        # Simulate a heart rate by gradually increasing the duty cycle
        for i in range(0, 101, 5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.01)
        # Then gradually decreasing the duty cycle
        for i in range(100, -1, -5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.01)

except KeyboardInterrupt:
    # Clean up and exit when the program is interrupted
    pwm.stop()
    GPIO.cleanup()
