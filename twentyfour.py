tupleInput = eval(input("Enter a tuple of integers: "))

listUser = list(tupleInput)

stringUser = ""

for ch in listUser:
    stringUser = stringUser + str(ch)

print(stringUser)
