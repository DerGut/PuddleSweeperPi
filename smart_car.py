import GPIO_setup

import RPi.GPIO as GPIO
import time

class SmartCar(object):
	"""docstring for SmartCar"""
	def __init__(self):
		self.left_on = GPIO_setup.ENB
		self.right_on = GPIO_setup.ENA
		self.left_forward = GPIO_setup.IN4
		self.left_backward = GPIO_setup.IN3
		self.right_forward = GPIO_setup.IN2
		self.right_backward = GPIO_setup.IN1

	def stop_moving(self):
		print("Stop!")
		# Turn off motors
		GPIO.output(self.right_on, False)
		GPIO.output(self.left_on, False)
		# Stop movement
		GPIO.output(self.right_backward, False)
		GPIO.output(self.right_forward, False)
		GPIO.output(self.left_backward, False)
		GPIO.output(self.left_forward, False)

	def move_forwards(self, duration=0):
		print("Move forward")
		# Turn on motors
		GPIO.output(self.right_on, True)
		GPIO.output(self.left_on, True)
		# Speed up
		GPIO.output(self.right_forward, True)
		GPIO.output(self.left_forward, True)
		# Stop reverse direction
		GPIO.output(self.right_backward, False)
		GPIO.output(self.left_backward, False)
		if duration > 0:
			time.sleep(duration)
			self.stop_moving()

	def move_backwards(self, duration=0):
		print("Move back")
		# Turn on motors
		GPIO.output(self.right_on, True)
		GPIO.output(self.left_on, True)
		# Speed up
		GPIO.output(self.right_backward, True)
		GPIO.output(self.left_backward, True)
		# Stop reverse direction
		GPIO.output(self.right_forward, False)
		GPIO.output(self.left_forward, False)
		if duration > 0:
			time.sleep(duration)
			self.stop_moving()

	def turn_left(self, duration=0):
		print("Turn left")
		# Turn on motors
		GPIO.output(self.right_on, True)
		GPIO.output(self.left_on, False)
		# Speed up
		GPIO.output(self.right_forward, True)
		# Stop reverse direction
		GPIO.output(self.right_backward, False)
		GPIO.output(self.left_backward, False)
		GPIO.output(self.left_forward, False)
		if duration > 0:
			time.sleep(duration)
			self.stop_moving()

	def turn_right(self, duration=0):
		print("Turn right")
		# Turn on motors
		GPIO.output(self.right_on, False)
		GPIO.output(self.left_on, True)
		# Speed up
		GPIO.output(self.left_forward, True)
		# Stop reverse direction
		GPIO.output(self.right_backward, False)
		GPIO.output(self.right_forward, False)
		GPIO.output(self.left_backward, False)
		if duration > 0:
			time.sleep(duration)
			self.stop_moving()

		