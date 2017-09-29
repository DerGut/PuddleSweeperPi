import sys
import termios
import contextlib
import RPi.GPIO as GPIO

from smart_car import SmartCar
from camera import Camera

@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)

def main():
	car = SmartCar()
	cam = Camera()
	with raw_mode(sys.stdin):
	    try:
	        while True:
	            ch = sys.stdin.read(1)
	            if not ch or ch == chr(4):
	                break
	        
	            ordnum = '%02x' % ord(ch)
	            print ordnum
	            if ordnum == '77':  # W
	            	car.move_forwards(0.1)
	            elif ordnum == '61':  # A
	            	car.turn_left(0.1)
	            elif ordnum == '64':  # D
	            	car.turn_right(0.1)
	            elif ordnum == '73':  # S
	            	car.move_backwards(0.1)
	            elif ordnum == '6a':  # J
	            	cam.turn_left(1)
	            elif ordnum == '6b':  # K
	            	cam.turn_right(1)
	            elif ordnum == '6c':  # L
	            	cam.turn_down(1)
	            elif ordnum == '69':
	            	cam.turn_up(1)

	    except (KeyboardInterrupt, EOFError):
	        GPIO.cleanup()


if __name__ == '__main__':
	main()
