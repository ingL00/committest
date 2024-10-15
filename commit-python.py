def loop(name):
  result = ""
  for i in range(len(name)-1, -1, -1):
    result += name[i]
  return result


if __name__ == '__main__':
  print(loop("heraldo yusron"))