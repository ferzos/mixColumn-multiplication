mixColumn = [
  [2,3,1,1],
  [1,2,3,1],
  [1,1,2,3],
  [3,1,1,2]
]

def shiftRight(element):
  return element[1:]+'0'

def xor(element1, element2):
  result = ''
  for i in range (0, len(element1)):
    if (element1[i] != element2[i]):
      result += '1'
    else:
      result += '0'
  return result

def xor2(element):  
  firstBit = element[0]
  element = shiftRight(element)
  if (firstBit == '1'):
    return xor(element, '00011011')
  
  return element
  
def xor3(element): 
  elementAfterXor2 = xor2(element)
  return xor(elementAfterXor2, element)

def multiply(elementMCNumber, elementColumn):
  elementColumnBinary = '{0:08b}'.format(int(elementColumn, 16))
  if (elementMCNumber == 2):
    return xor2(elementColumnBinary)
  elif (elementMCNumber == 3):
    return xor3(elementColumnBinary)
  else :
    return elementColumnBinary

def calculate(row, column):
  multiplyAnswerList = []  
  for i in range(0, 4):
    multiplyAnswerList.append(multiply(row[i], column[i]))
  sumMixColumn(multiplyAnswerList)

def multipleColumn(mixColumn, column):
  for i in range(0, 4):
    calculate(mixColumn[i], column)

def sumMixColumn(multiplyAnswerList):
  answer = '00000000'
  for entry in multiplyAnswerList:
    answer = xor(answer, entry)
  print(hex(int(answer, 2)))

def main():
  column = [
    # COLUMN 1
    ["87","6E","46","A6"],
    # COLUMN 2
    ["F2","4C","E7","8C"],
    # COLUMN 3
    ["4D","90","4A","D8"],
    # COLUMN 4
    ["97","EC","C3","95"],
  ]
  for i in range(0, 4):
    print("Column ke-{}: ".format(i+1))
    multipleColumn(mixColumn, column[i])
    print('\n')

main()