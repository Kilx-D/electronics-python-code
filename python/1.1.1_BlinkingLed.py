#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LedPin = 21
ledpin2 = 26
ledpin3 = 16
ledpin4 = 20
def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set LedPin's mode to output,and initial level to High(3.3v)
    
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(ledpin2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(ledpin3, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(ledpin4, GPIO.OUT, initial=GPIO.HIGH)
# Define a main function for main process
def main():
    while True:
        print ('...LED ON')
        # Turn on LED
        
        GPIO.output(LedPin, GPIO.LOW)
        GPIO.output(ledpin2, GPIO.LOW)
        GPIO.output(ledpin3, GPIO.LOW)
        GPIO.output(ledpin4, GPIO.LOW)
        # time.sleep(0.5)
        # print ('LED OFF...')
        # # Turn off LED
        # GPIO.output(LedPin, GPIO.HIGH)
        # time.sleep(0.5)
# Define a destroy function for clean up everything after the script finished
def destroy():
    # Turn off LED
    GPIO.output(LedPin, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()                   
# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()