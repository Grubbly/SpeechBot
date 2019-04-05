import RPi.GPIO as GPIO
import time

leftArmPin = 17
rightArmPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(leftArmPin, GPIO.OUT)
GPIO.setup(rightArmPin, GPIO.OUT)

leftArm = GPIO.PWM(leftArmPin,50)
rightArm = GPIO.PWM(rightArmPin,51)

leftArm.start(7.5)
rightArm.start(7.5)

leftArm.ChangeDutyCycle(7.5)
time.sleep(.3)
leftArm.ChangeDutyCycle(10)
time.sleep(.3)
rightArm.ChangeDutyCycle(7.5)
time.sleep(.3)
rightArm.ChangeDutyCycle(10)
time.sleep(.3)
leftArm.ChangeDutyCycle(7.5)
time.sleep(.3)
leftArm.ChangeDutyCycle(10)
time.sleep(.3)
rightArm.ChangeDutyCycle(7.5)
time.sleep(.3)
rightArm.ChangeDutyCycle(10)
time.sleep(.3)
leftArm.ChangeDutyCycle(7.5)
time.sleep(.3)
leftArm.ChangeDutyCycle(10)
time.sleep(.3)
rightArm.ChangeDutyCycle(7.5)
time.sleep(.3)
rightArm.ChangeDutyCycle(10)
time.sleep(.3)
leftArm.ChangeDutyCycle(7.5)
time.sleep(.3)
leftArm.ChangeDutyCycle(10)
time.sleep(.3)
rightArm.ChangeDutyCycle(7.5)
time.sleep(.3)
rightArm.ChangeDutyCycle(10)
time.sleep(.3)

leftArm.stop()
rightArm.stop()
GPIO.cleanup()
