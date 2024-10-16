def loop(name):
  result = ""
  for i in range(len(name)-1, -1, -1):
    result += name[i]
  return result

def encrypt(name):
  result = ""
  for i in range(len(name)):
    result += chr(ord(name[i])+1) 
  return result
  
def capitalize(name):
  result = name.upper()
  return result

if __name__ == '__main__':
  reverse = loop("heraldo yusron")
  encrypt = encrypt(reverse)
  capital = capitalize(encrypt)

  print(capital)
