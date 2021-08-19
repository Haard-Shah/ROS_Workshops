""" Simple Servo test python file depends on the GPIOzero library
"""

from gpiozero import Servo
from time import sleep

servo = Servo(17) # GPIO Pin

while True:
    servo.mid()
    print("mid")
    sleep(0.5)

    servo.min()
    print("min")
    sleep(1)

    servo.mid()
    print("mid")
    sleep(0.5)

    servo.max()
    print("max")
    sleep(1)
