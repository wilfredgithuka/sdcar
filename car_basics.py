#Wilfred Githuka
#Githuka.com
#Self Driving RC Car Project
#Back Wheels Locomotion Only
#Enjoy

import RPi.GPIO as io
io.setmode(io.BCM)
import sys, tty, termios, time

# Settings forthe two DC motors on the RC car.Defining the two GPIO pins used for the input
# and starting the PWM and seting the motors' speed to 0

BackMotorGpioPositive = 4
BackMotorGpioNegative = 17
io.setup(BackMotorGpioPositive, io.OUT)
io.setup(BackMotorGpioNegative, io.OUT)
BackMotor = io.PWM(4,100)
BackMotor.start(0)
BackMotor.ChangeDutyCycle(0)

SteeringMotorGpioPositive = 24
SteeringMotorGpioNegative = 25
io.setup(SteeringMotorGpioPositive, io.OUT)
io.setup(SteeringMotorGpioNegative, io.OUT)
SteeringMotor = io.PWM(4,100)
SteeringMotor.start(0)
SteeringMotor.ChangeDutyCycle(0)

## Lets get some keypress

def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
        finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# Motor Movement Section

def BackMotorFoward():
        io.output(BackMotorGpioPositive, True)
        io.output(BackMotorGpioNegative, False)
def BackMotorReverse():
        io.output(BackMotorGpioPositive, False)
        io.output(BackMotorGpioNegative, True)

# Setting The PWM to False so that the wheels do not start moving when the code is run, they must wait for keypress
io.output(BackMotorGpioPositive, False)
io.output(BackMotorGpioNegative, False)

# Global Variables for Front Wheels, not used now
WheelStatus = "center"

# UI
print("w or s : Front or Back Movement")

# The infinite loop that waits for key press

while True:
        char = getch()
        if (char == "w"):
                BackMotorFoward()
                BackMotor.ChangeDutyCycle(99)
        if (char == "s"):
                BackMotorReverse()
                BackMotor.ChangeDutyCycle(99)
        if (char == "x"):
                print("Program Ended")
                break
                BackMotor.ChangeDutyCycle(0)
                char = ""

io.cleanup()
