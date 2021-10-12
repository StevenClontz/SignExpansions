# Obtain value of an L or R for the purpose of binaryCalc()
def getValue(element):
    if element == "R":
        return 1
    elif element == "L":
        return -1
    else:
        return 0
# Calculating the diadtic portion of our number
def binaryCalc(binaryStep, element):
    return getValue(element) * (1 / (2 ** (binaryStep)))
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
        else:  # Sign change is True, rest is binary calculation
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
            if element == '0':
                step += 1
            else:
                return step
def addDecimal(list):
    returnString = ""
    decimalSum = sum([getValue(x) for x in list])
    if decimalSum == 0: return None
    if decimalSum > 0:
        for i in range(decimalSum):
            returnString += "R"
    elif decimalSum < 0:
        for i in range(decimalSum):
            returnString += "L"
    return returnString
def addBinary(list1,list2,decimalpart):

    sumList = []
    remainder = ""
    for i in range(max(len(list1),len(list2))-1,-1,-1):
        try: b1 = list1[i]
        except: b1 = ""
        try: b2 = list2[i]
        except: b2 = ""
        thisstring = b1 + b2 + remainder
        remainder = ""
        if thisstring == "R" or thisstring == "L":                      # Rule 0
            sumList.insert(0,thisstring)
        elif thisstring == "LL":                                        # Rule 2
            remainder = "L"
            if sumList == []: pass
            elif sumList[0] == "R":
                sumList[0] = "L"
                sumList.insert(0, "R")
            elif sumList[0] == "L":
                sumList[0] = "R"
                sumList.insert(0, "L")
        elif thisstring == "RR":                            # Rule 2
            remainder = "R"
            if sumList == []: pass
            elif sumList[0] == "L":
                sumList[0] == "R"
                sumList.insert(0, "L")
            elif sumList[0] == "R":
                sumList[0] == "L"
                sumList.insert(0, "R")
        elif "L" in thisstring and "R" in thisstring:
            if thisstring.count("R") == 2:                              # Rule 2
                sumList.insert(0,"R")
            if thisstring.count("L") == 2:
                sumList.insert(0,"L")
            elif len(sumList) > 1:                                     # Rule 1
                if sumList[0] == "R":
                    sumList[0] == "L"
                    sumList.insert(0,"R")
                if sumList[0] == "L":
                    sumList[0] == "R"
                    sumList.insert(0,"L")

    if sumList != []:
        if decimalpart == [] or decimalpart[-1] == sumList[0] == "R": sumList.insert(1,"L")      # Rule 3
        elif decimalpart[-1] == sumList[0] == "L": sumList.insert(1, "R")
    if remainder != "": decimalpart = addDecimal(list(decimalpart)+[remainder])

    #print(decimalpart)
    #print(sumList)

    return (decimalpart+''.join(sumList))
def addNumbers(list1, list2):
    if getSplitPoint(list1,list1[0]) is None:
        decimal1 = list1
        binary1 = []
    else:
        decimal1 = list1[:getSplitPoint(list1,list1[0])]
        binary1 = list1[getSplitPoint(list1, list1[0]):]

    if getSplitPoint(list2, list2[0]) is None:
        decimal2 = list2
        binary2 = []
    else:
        decimal2 = list2[:getSplitPoint(list2, list2[0])]
        binary2 = list2[getSplitPoint(list2, list2[0]):]

    decimalpart = addDecimal(decimal1+decimal2)

    return addBinary(binary1,binary2,decimalpart)

x = list("RLRRRLR")
y = list("RRRLLRLRL")

num = addNumbers(x,y)

num = list(num)

print("Value 1:", calculate(x), ''.join(x),
      "\nValue 2:", calculate(y), ''.join(y),
      "\nSum:", calculate(num), ''.join(num))



