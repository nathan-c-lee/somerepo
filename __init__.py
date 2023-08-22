

def ask_name():
    mn = input("what is your name")
  if mn.isalpha():
    print(f'hello {mn}')
    return False, mn
  else:
    print("error, bad input")
    return True
