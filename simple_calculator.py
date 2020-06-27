# Simple calculator
# @lxndroc 2020
# https://www.quora.com/What-are-some-Python-projects-I-can-build-without-any-modules-using-only-the-basics-and-displaying-everything-in-console/answer/Alexandros-Xafopoulos
# The program asks for two numbers and an operator,
# so you can add, subtract, multiply, divide, or power.

def calculate():
	number_of_calculations = 0
	while True:
		number1 = int(input("Enter your first number or 0 to quit: "))
		operator = input("Enter your operator: + for +, - for -, x for x, d for ÷, p for power: ")
		number2 = int(input("Enter your second number: "))
		number_of_calculations += 1
		if operator == "+":
 			print(f"{number1}+{number2}\n\t{number1 + number2}")
		elif operator == "-":
			print(f"{number1}-{number2}\n\t{number1 - number2}")
		elif operator == "x":
			print(f"{number1}*{number2}\n\t{number1 * number2}")
		elif operator == "d":
			print(f"{number1}/{number2}\n\t{number1 / number2}")
		elif operator == "p":
			print(f"{number1}**{number2}\n\t{number1 ** number2}")
		elif operator == "0":
			print(f"Number of calculations = {number_of_calculations}")
			print("See you next time")
			break

calculate()
