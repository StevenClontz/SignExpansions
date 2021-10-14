def getValue(element):
  if element == "R": return 1
  elif element == "L": return -1
  else: return 0
# Calculating the diadtic portion of our number
def binaryCalc(binaryStep, element):
  return getValue(element) * (1/(2**(binaryStep)))
# Calculating a single LR list
def calculate(list):
  initialSign = list[0]
  sum = 0
  binaryStep = 0
  signChange = False
  for element in list:
    if (signChange is False and element == initialSign == "R"):
      sum += 1
    elif (signChange is False and element == initialSign == "L"):
      sum += -1
    elif (element != initialSign and signChange is False):
      signChange = True
      binaryStep += 1
      sum += binaryCalc(binaryStep, element)
    else: # Sign change is True, rest is binary calculation
      binaryStep += 1
      sum += binaryCalc(binaryStep, element)
  return sum
# Gets the point where the diadic portion begins
def getSplitPoint(list, initialSign):
  step = 0
  for element in list:
    if (element == initialSign):
      step += 1
    else:
      if element == '0': step += 1
      else: return step
# Create a larger list and set up the two numbers to add listwise
def createSpace(list1,list2,initialSign1,initialSign2):
  _list1 = list(list1)
  ogList2 = len(list2)
  # List extension
  list1.extend(['0'] * (2 * (len(list2) - 1)))
  list2.extend(['0'] * (len(list1)-len(list2)))
  # List shifting
  for i in range(ogList2-1):
    list1.insert(0, list1.pop())
  xShift = int(getSplitPoint(list1, initialSign1) or 0)
  yShift = int(getSplitPoint(list2, initialSign2) or 0)
  for i in range (xShift - yShift):
    list2.insert(0, list2.pop())
  return getSplitPoint(list1,initialSign1)
# Assumes that we are not dealing with whole numbers!
def addNumbers(list1,list2):
  print("Value 1:",calculate(list1),list1,"\nValue 2:",calculate(list2),list2)
  splitPoint = createSpace(list1,list2,list1[0],list2[0])
  sumList = addElements(list1,list2, splitPoint)
  print("Value 3:", calculate(sumList), sumList)
def addElements(list1, list2, splitPoint):
  sumList = []
  print(splitPoint)
  RFlag = False
  LFlag = False
  for i in range( len(list1) - 1, -1, -1) :
    elementConcat = (list1[i] + list2[i]).replace("0","")
    if i >= splitPoint:
      if elementConcat == "L" or elementConcat == "R":
        sumList.insert(0,elementConcat)
      elif (elementConcat == "LR") or (elementConcat == "RL"):
        if sumList[0] == "R":
          if i == splitPoint:
            LFlag = True
          sumList.insert(0,"R")
          sumList[1] = "L"
        elif sumList[0] == "L":
          if i == splitPoint:
            RFlag = True
          sumList.insert(0,"L")
          sumList[1] = "R"
      elif elementConcat == "RR":
        sumList.insert(0,"L")
      elif elementConcat == "LL":
        sumList.insert(0,"R")
    else:
      if elementConcat == "R":
        sumList.insert(0,"R")
      elif elementConcat == "L":
        sumList.insert(0,"L")
  if RFlag is True: sumList.insert(len(sumList),"R")
  if LFlag is True: sumList.insert(len(sumList),"L")
  return sumList

from random import choice
x = [choice(["R","L"]) for _ in range(3)]
y = [choice(["R","L"]) for _ in range(3)]

addNumbers(x,y)


      


