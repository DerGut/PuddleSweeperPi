#! /usr/bin/python
# -*- coding:utf-8 -*-

import time
import RPi.GPIO as GPIO

print("Setting up GPIO...")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ENA = 13  # Right wheels on
ENB = 20  # Left wheels on	
IN1 = 19  # Right wheels backwards
IN2 = 16  # Right wheels forwards
IN3 = 21  # Left wheels backwards
IN4 = 26  # Left wheels forwards
SER7 = 6  # Camera servo yaw
SER8 = 12  # Camera servo pitch

GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup motor pins
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

# Setup camera pins
GPIO.setup(SER7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SER8, GPIO.OUT)

time.sleep(2)

print("Setup done!")

