from colorama import Fore, Back, Style

class Variable:

	def __init__(self, name, value):
		self.name = name
		self.value = value

	def __str__(self):
		return Style.BRIGHT + Fore.BLUE + self.name + Fore.RESET + Style.RESET_ALL + ' = ' + str(self.value)

