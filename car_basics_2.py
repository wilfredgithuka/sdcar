#!/usr/bin/env python

# Wilfred Githuka
# Raymond Wanyoike
# Githuka.com
# Self Driving RC Car Project
# Basics
# Enjoy

import sys
import termios
import time
import tty

import RPi.GPIO as io
io.setmode(io.BCM)

# Settings for the two DC motors on the RC car.Defining the two GPIO pins used
# for the input and starting the PWM and seting the motors' speed to 0

FrontMotorGpioPositive = 24
FrontMotorGpioNegative = 25
BackMotorGpioPositive = 4
BackMotorGpioNegative = 17


def reset_motors():
    """Reset everything to back to zero."""

    for i in (FrontMotorGpioPositive, FrontMotorGpioNegative, BackMotorGpioPositive, BackMotorGpioNegative):
        io.setup(i, io.OUT)
        # Setting The PWM to False
        io.output(i, Fals


reset_motors()


FrontMotor = io.PWM(4, 100)
BackMotor = io.PWM(4, 100)

def get_keypress():
    """Lets get the keypress from terminal."""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def motor_movement(motor, direction):
    """Motor movement logic, front & back.

    arg motor: 'front' or 'back'
    arg direction: True is (forward or left)
                   False is (backward or right)
    """

    if motor == 'front':
        io.output(FrontMotorGpioPositive, direction)
        io.output(FrontMotorGpioNegative, not direction)

    if motor == 'back':
        io.output(BackMotorGpioPositive, direction)
        io.output(BackMotorGpioNegative, not direction)

        # Hack to invert power on direction change
        if direction:
            BackMotor.ChangeDutyCycle(99)
        else:
            BackMotor.ChangeDutyCycle(0)


FrontMotor.start(0)
BackMotor.start(0)

if __name__ == '__main__':
    print("w or s : Front or Back Movement")
    print("a or d : Left or Right Movement")

    # The infinite loop
    while True:
        char = get_keypress()

        # Front / Back
        if (char == "w"):
            motor_movement('back', True)
        if (char == "s"):
            motor_movement('back', False)

        # Right / Left
        if (char == "a"):
            motor_movement('front', True)
        if (char == "d"):
            motor_movement('front', False)

        # Exit!
        if (char == "x"):
            print("Program Ended")
            reset_motors()
            break

    io.cleanup()

