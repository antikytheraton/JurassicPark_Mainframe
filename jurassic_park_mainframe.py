# Jurassic Park mainframe

from random import randint
from sys import exit
from comm_system import Comm_system #the file i want to import from

class Jpark_mainframe(object):
	def mainframe_home(self):
		print("=====Welcome to the Jurassic Park Mainframe=====")
		print("==========Security Administration===============")
		print("===========Communications Systems===============")
		print("===============System Settings==================")
		print("===================Quit=========================")

		prompt = input("What would you like to do? ")

		while prompt != "Quit":

			if prompt == "Security Administration":
				print("Please enter the 5-digit passcode: ")
				security_passcode = "%d%d%d%d%d" % (2, 0, 1, 2, randint(1, 2))
				security_guess = input(": ")
				security_guesses = 0

				while security_guess != security_passcode and security_guesses < 7:
					print("Incorrect. Please enter the security passcode.")
					security_guesses += 1
					security_guess = input(": ")

					if security_guess == security_passcode:
						print("=========Security Administration=======")
						print("Area 1 Fences: Off")
						print("Area 2 Fences: On")
						print("Area 3 Fences: Off")
						print("Velociraptor Compound: Off")
						print("Lobby Security System: Off")
						print("Entrance Facility System: Off")
						print("To enable all systems, enter 'On'")

						enable_security = input(": ")

						if enable_security == "On":
							print("Systems Online.")

					if prompt == "System Settings":
						print("You do not have acces ti system settings.")
						exit(0)

					if prompt == "Communications Systems":
						print("===========Communications Systems===========")
						print("error: 'comm_link' missing in directories")
						exit(0)
						return Comm_system.run 

the_game = Jpark_mainframe()
the_game.mainframe_home()