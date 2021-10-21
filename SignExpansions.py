class Surreal:
    # Initialize and handle improper suffixes
    def __init__(self, int = 0, suffix = ""):
        self.int = int
        self.suffix = suffix
        self.se = None
        self.Float = 0

        # Improper suffix handling
        # (x) = x(!x)
        # We account for this improper suffix by correcting the integer value by +- 1
        if suffix != "":
            if self.suffix[0] == "R" and self.int >= 0:
                self.int += 1
                # Can't ensure that suffix length > 1, so correct it in-place
                self.suffix = self.suffix.replace("R","L",1)
            elif self.suffix[0] == "L" and self.int <= 0:
                self.int -= 1
                self.suffix = self.suffix.replace("L","R",1)
    # Create the float value for the sign expansion
    def fraction(self):
        s = 1
        self.Float = 0
        for c in self.suffix:
            if c == "L":
                self.Float -= (1 / (2 ** (s)))
            elif c == "R":
                self.Float += (1 / (2 ** (s)))
            s += 1
        return self.int + self.Float
    # Create the sign expansion string
    def signexpansion(self):
        if (self.int >= 0):
            if self.suffix == "": return ("R" * (self.int))
            return ("R" * (self.int)) + self.suffix
        elif (self.int < 0):
            if self.suffix == "": return ("L" * (-self.int))
            return ("L" * -(self.int)) + self.suffix
    # Method for indexing through a string
    def suffix_int(self, index):
        try:
            if self.suffix[index] == "L":
                return -1
            elif self.suffix[index] == "R":
                return 1
        except:
            return 0
    # Add two surreal numbers, return a new surreal number object
    def add(self, surreal2):
        intsum = self.int + surreal2.int
        sumstring = ""
        remainder = 0

        #print("IntSum",intsum)
        #print(self.suffix,surreal2.suffix)

        for i in range(max(len(self.suffix), len(surreal2.suffix)) - 1, -1, -1):
            stepsum = self.suffix_int(i) + surreal2.suffix_int(i) + remainder
            # Now we can safely reset the remainder
            remainder = 0

            # -1 and 1 could represent two sums each
            if stepsum == -1: sumstring = "L" + sumstring
            elif stepsum == 1: sumstring = "R" + sumstring

            # -3, 3 mean we add and carry remainder
            if stepsum == 3:
                remainder = 1
                sumstring = "R" + sumstring
            if stepsum == -3:
                remainder = -1
                sumstring = "L" + sumstring

            # 0L = LR ; 0R = RL
            # 0,2,-2 mean we can't add to sumstring if it is empty; Carry remainder for 2,-2
            if (stepsum % 2 == 0):
                if sumstring == "": pass
                elif sumstring[0] == "R":

                    sumstring = sumstring.replace("R", "RL", 1)
                elif sumstring[0] == "L":

                    sumstring = sumstring.replace("L", "LR", 1)
                if stepsum == 2: remainder = 1
                elif stepsum == -2: remainder = -1

        return Surreal(intsum+remainder,sumstring)

x = Surreal(3, "LRL") # RRR | LRL => 3 -1/2 + 1/4 - 1/8 = 2.625           RRR|LRL
print("X", x.signexpansion(), x.fraction())
print("----------------------------------")
y = Surreal(1,"R") # 1 R => 2 L = 1.5                                     RR|L
print("Y", y.signexpansion(), y.fraction())
print("----------------------------------")
z = x.add(y)                                      #                       RRRRR|LLL
print("Z", z.signexpansion(), z.fraction())
print("----------------------------------")

