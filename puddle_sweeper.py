import sys
import math
import pip

sys.path.append("../..")
if sys.version_info < (3, 5):
	raise Exception('Please use Python version 3.5 or greater.')

from qiskit import QuantumProgram
import Qconfig

def install(package):
	pip.main(['install', package])

# install('IBMQuantumExperience')


# import getpass, random, numpy


class Player(object):
	"""docstring for Player"""

	def __init__(self, board_length=10, device="local_qasm_simulator", shots=1000):

		self.playing_board = board_length * [None]

		self.device = device
		self.shots = shots

		self.Q_program = QuantumProgram()
		self.Q_program.set_api(Qconfig.APItoken, Qconfig.config[
			"url"])  # set the APIToken and API url
		# current qubit of field
		self.qubit_register = self.Q_program.create_quantum_register(
			"qubit_register", 1)
		# declare register of classical bits to hold measurement results
		self.c_register = self.Q_program.create_classical_register(
			"c_register", 1)
		# create circuit
		self.qasm_code = self.Q_program.create_circuit(
			"qasm_code", [self.qubit_register], [self.c_register])

		# Location of the player along the board
		self.index = 0


	def look_at_field(self, field_value):
		validate = True
		while validate:
			if field_value.lower() == 'puddle':
				value = 3
				validate = False
			elif field_value.lower() == 'mud':
				value = 2
				validate = False
			elif field_value.lower() == 'grass':
				value = 1
				validate = False
			elif field_value.lower() == 'flowers':
				value = 0
				validate = False
			else:
				print(">> I am sorry but I couldn't understand you")
				print(">> The board is made up of Mud, Grass, Flowers and Puddle(s)")

		# Set inner representation of board to the new information
		self.qubit_register = self.Q_program.create_quantum_register("qubit_register", 1)
		# declare register of classical bits to hold measurement results
		self.c_register = self.Q_program.create_classical_register("c_register", 1)
		# create circuit
		self.qasm_code = self.Q_program.create_circuit("qasm_code", 
			[self.qubit_register], [self.c_register])
		self.qasm_code.u3((value / 3) * math.pi, 0.0, 0.0, self.qubit_register[0])

	def move(self, steps):
		#
		# Actual movement (robot)
		#
		# Update location index
		self.index = self.index + steps


	def predict_next_field(self):
		self.qasm_code.measure(self.qubit_register[0], self.c_register[0])

		# Executes the current QASM script
		# print(self.Q_program.get_qasm("qasm_code"))
		results = self.Q_program.execute(
			["qasm_code"], backend=self.device, shots=self.shots, silent=False)
		counts = results.get_counts("qasm_code")
		# print(">> My qubits calculated some {}/{} ratio".format(counts['0']/self.shots, counts['1']/self.shots))

		if counts['0'] >= (0.99 * self.shots):
			print(">> Oh flowers, perfekt. I can just move on!")
	
			# if the field shows a 0, the robot goes to the next field
			self.move(1)
			self.playing_board[self.index - 1] = 0

		elif counts['0'] >= (0.65 * self.shots):
			print('>> It´s grass! Is there a puddle behind me? If yes I can just move on. Otherwise I need to jump over the puddle in front of me!')

			# if the field shows a 1, the robot checks the previous field and then makes a decision
			# is there a puddle in the previous field, the robot moves on
			if self.playing_board[self.index - 1] == 3:
				self.move(1)
				self.playing_board[self.index - 1] = 1

			# is there no puddle, the robot makes a jump over the following field	
			else:
				self.move(2)
				self.playing_board[self.index - 2] = 1
				self.playing_board[self.index - 1] = 3

		elif counts['0'] >= (0.1 * self.shots):
			print(">> Urgh, thats muddy… There have to be two puddles around me! Is there one behind me? Well, I need to jump anyways.")
			# if the field shows a 2, the robot makes a jump
			self.move(2)
			self.playing_board[self.index - 2] = 2
			self.playing_board[self.index - 1] = 3

		else:
			# if the field shows a 3, the robot falls into the puddle and loses the game
			sys.exit('>> Oh no, I fell into a puddle. Can we play again?')



print("-------------------------------------")
print("-                                   -")
print("-      Welcome to PuddleSweeper     -")
print("-                                   -")
print("-------------------------------------")
print(">> Hey!")
print(">> I´m farmer robbi.")
print(">>")
print(">> Mhmmm, do you smell the oilsoup? I need to get to the house to my wifes´lunch. ")
print(">> But look, there are many puddles on my way, which I need to avoid. Don´t want to get rusty…")
print(">> The only safe way to get there is to watch my steps and jump over the puddles.")
print(">> Near flower fields there are no puddles, I can pass without worries.")
print(">> But on grass I have to be careful, as there is one puddle close by.")
print(">> The most dangerous ground is mud, there are two puddles around me.")
print(">> Ready? ")
print(">> Then let´s go!")
print(">> ")
print(">> ")




length = int(input(">> Please tell me the board length:\n"))
player = Player(length)

while player.index < length:
	# Blablabla game loop
	print("Field no. {}".format(player.index+1))

	field = input(">> What ground am I on?\n  I cannot see it myself as I'm not connected to the internet.\n")	
	player.look_at_field(field)
	player.predict_next_field()
	print()
	print()

print('>> I win! What a great game.')
print(">> Yes we made it! Thank you for your support! Let´s get some of this delicious oilsoup.")


