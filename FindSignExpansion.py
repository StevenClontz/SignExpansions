import math

def calcBinary(s):
  return (1 / (2 ** (s)))

def invert(se):
  new_se = ""
  for element in se:
    if element == "R":
      new_se += "L"
    elif element == "L":
      new_se += "R"
  return new_se

def se(num, steps = None, stop = False):
  se = ""
  placeholdernum = num
  num_se = (math.modf(float(abs(placeholdernum))))


  # Integer
  se = se.ljust(int(num_se[1]) + len(se), "R")

  # Decimal
  if num_se[0] == 0.0:
    if num < 0: return invert(se)
    return (se)
  se += "R"

  bse = "L"
  binary = num_se[0]
  s = 1
  treeVal = 0
  if steps is None:
    while s <= steps and binary != 0:
      treeVal += calcBinary(s)
      # print(binary,treeVal)
      if binary == treeVal:
        # print("a")
        break
      elif binary > treeVal:
        # print("b")
        bse += "R"
      elif binary < treeVal:
        # print("c")
        bse += "L"
        treeVal -= 2 * calcBinary(s) / 2
      s += 1
  elif steps > 0: 
    while s <= steps and binary != 0: 
      treeVal += calcBinary(s) 
      #print(binary,treeVal)
      if binary == treeVal:
        #print("a")
        break
      elif binary > treeVal:
        #print("b")
        bse += "R"
      elif binary < treeVal:
        #print("c")
        bse += "L"
        treeVal -= 2 * calcBinary(s)/2
      s += 1
    if stop is True and binary != treeVal:
      return "Error"

  if num < 0: return invert(se+bse)
  return(se + bse)


print(se(-3.75,20, False))
