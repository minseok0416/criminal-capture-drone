import RPi.GPIO as GPIO
from time import sleep

servoPin = 12
SERVO_MAX_DUTY=12
SERVO_MIN_DUTY=3

GPIO.setmode(GPIO.BCM) 
GPIO.setup(servoPin,GPIO.OUT)

servo = GPIO.PWM(servoPin,50)
servo.start(0)
GPIO.setwarnings(False)

def set_servo_degree(degree):
    if degree > 180:
        degree = 180
    elif degree <0:
        degree = 0
    
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    servo.ChangeDutyCycle(duty) 



set_servo_degree(0)
sleep(1)
GPIO.cleanup()