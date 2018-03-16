mixColumn = [
  [2,3,1,1],
  [1,2,3,1],
  [1,1,2,3],
  [3,1,1,2]
]

def xor1(element):
  return element
def xor2(element):  
  firstBit = element[0]
  elementAferShift = bin(int(element, 2)) << 1
  # print(elementAferShift)
  # Check if the 1st bit is set:
  if (firstBit == 1):
    print("maka xor dengan lalala")
  return element
def xor3(element): 
  return element

def multiply(element, mixColumnNumber):
  element = '{0:08b}'.format(int(element, 16))
  if (mixColumnNumber == 2):
    return xor2(element)
  elif (mixColumnNumber == 3):
    return xor3(element)
  else :
    return xor1(element)
  # return "{} x {}".format(element, mixColumnNumber)

def calculate(array):
  listMultiply = []
  for i in range(0, len(array)):
    listMultiply.append(multiply(array[i], mixColumn[0][i]))
  sumMixColumn(listMultiply)

def sumMixColumn(listMultiply):
  print(listMultiply)

def main():
  # array = input("Input array (split by \',\'): ")
  array = "63,6B,67,76"
  calculate(array.split(','))

main()