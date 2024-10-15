def loop(name):
  result = ""
  for i in range(len(name)-1, -1, -1):
    result += name[i]
  return result

def encrypt(name):
 for i in range(len(name)):
  print(chr(ord(name[i])+1))
  
def capitalize(name):
  result = name.upper()
  return result

if __name__ == '__main__':
  reverse = loop("heraldo yusron")
  encrypt_reverse = encrypt(reverse)
  capital = capitalize(reverse)
  print(capital)
