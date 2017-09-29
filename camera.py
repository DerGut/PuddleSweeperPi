import RPi.GPIO as GPIO
import GPIO_setup
import time


class Camera(object):
	"""docstring for Camera"""
	def __init__(self):
		# Init yaw servo
		self.yaw = GPIO.PWM(GPIO_setup.SER7, 50) # GPIO 06 als PWM mit 50Hz
		self.yaw.start(0)
		# Init pitch servo
		self.pitch = GPIO.PWM(GPIO_setup.SER8, 50) # GPIO 12 als PWM mit 50Hz
		self.pitch.start(0)

		self.yaw_angle = 90
		self.pitch_angle = 90

	def set_yaw(self):
		duty = float(self.yaw_angle) / 20.0 + 2.5
		self.yaw.ChangeDutyCycle(duty)

	def set_pitch(self):
		duty = float(self.pitch_angle) / 20.0 + 2.5
		self.pitch.ChangeDutyCycle(duty)

	def turn_left(self, duration=0):
		self.yaw_angle += int(duration * 10)
		print "Yaw angle: ", self.yaw_angle
		self.set_yaw()
		if duration > 0:
			time.sleep(duration)

	def turn_right(self, duration=0):
		self.yaw_angle -= int(duration * 10)
		print "Yaw angle: ", self.yaw_angle
		self.set_yaw()
		if duration > 0:
			time.sleep(duration)

	def turn_up(self, duration=0):
		self.pitch_angle += int(duration * 10)
		print "Pitch angle: ", self.pitch_angle
		self.set_pitch()
		if duration > 0:
			time.sleep(duration)

	def turn_down(self, duration=0):
		self.pitch_angle -= int(duration * 10)
		print "Pitch angle: ", self.pitch_angle
		self.set_pitch()
		if duration > 0:
			time.sleep(duration)

	def camera_left(self, duration=0):
		print("Camera left")

