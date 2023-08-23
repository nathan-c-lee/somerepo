import os
from my_module import ask_name

while True:
	with open("a_file.txt", "r") as file:
	
		for line in file:
			print(line)
	
	while ask_name():
		continue

	q = input("\ntype 'q' to quit: ").lower()
	if q == "q":
		break
	else:
		continue



