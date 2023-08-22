import os
from somerepo import ask_name()

with open("a_file.txt", "r") as file:
	for line in file:
		print(line)

while ask_name():
	continue

