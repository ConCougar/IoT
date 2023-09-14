# from pyfirmata import Arduino, SERVO

#PORT="COM7"

#pin=10

#board=Arduino(PORT)

#board.digital[pin].mode=SERVO

#def rotateServo(pin, angle):
#    board.digital[pin].write(angle)

#def doorAutomate(val):
#    if val==0:
#        rotateServo(pin, 220)
#    elif val==1:
#        rotateServo(pin, 40)


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT) # servo pin 11 with PWM

servo = GPIO.PWM(11,50) # pulse frequency at pin 11

servo.start(0)
print("Waiting for 1 second")
time.sleep(1)

print ("Rotating at intervals of 12 degrees")
duty = 2
while duty <= 17:
servo.ChangeDutyCycle(duty)
time.sleep(1)
duty = duty + 1

print ("Turning back to 0 degrees")
servo.ChangeDutyCycle(2)
time.sleep(1)
servo.ChangeDutyCycle(0)

Servo.stop()
GPIO.cleanup()
print ("Everything's cleaned up")