# (('333', '33'), ('1416', '55'))

tupleOfTuples = eval(input("Enter tuple of tuples: "))

listOfList = [list(x) for x in tupleOfTuples]
listOfList = [[int(float(j)) for j in i] for i in listOfList]

print(listOfList)


