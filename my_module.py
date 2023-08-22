

def ask_name():
  mn = input(">> what is your name?: ")
  if mn.isalpha():
    print(f'hello {mn}, goodbye {mn}', "")
    return False
  else:
    print("error, bad input", "")
    return True
