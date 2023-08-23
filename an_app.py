import os
from my_module import ask_name

while True:
	with open("a_file.txt", "r") as file:
	
		for line in file:
			if "//" in line:
				while ask_name():
					continue
			else:
				print(line)

	q = input("type 'q' to quit: ").lower()
	if q == "q":
		break
	else:
		continue



