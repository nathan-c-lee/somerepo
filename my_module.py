

def ask_name():
  mn = input(">> what is your name?: ")
  if mn.isalpha():
    print(f'hello {mn}, goodbye {mn}', "\n")
    return False
  else:
    print("error, bad input", "\n")
    return True
