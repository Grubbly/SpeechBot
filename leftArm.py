import RPi.GPIO as GPIO
import time

leftArmPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(leftArmPin, GPIO.OUT)

leftArm = GPIO.PWM(leftArmPin,50)

leftArm.start(15)

try:
    while True:
        leftArm.ChangeDutyCycle(7.5)
        time.sleep(.3)
        leftArm.ChangeDutyCycle(10)
        time.sleep(.3)
except KeyboardInterrupt:
        leftArm.stop()
        GPIO.cleanup()
