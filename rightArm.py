import RPi.GPIO as GPIO
import time

rightArmPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(rightArmPin, GPIO.OUT)

rightArm = GPIO.PWM(rightArmPin,51)

rightArm.start(7.5)

try:
    while True:
        rightArm.ChangeDutyCycle(7.5)
        time.sleep(.3)
        rightArm.ChangeDutyCycle(10)
        time.sleep(.3)
except KeyboardInterrupt:
        rightArm.stop()
        GPIO.cleanup()