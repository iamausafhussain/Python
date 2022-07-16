# ((10,10,10,12), (30,45,56,45), (81,80,39,32), (1,2,3,4))
tupleOfTuple = eval(input("Enter Tuple of Tuples: "))

listOfList = [list(x) for x in tupleOfTuple]
print(listOfList)

sumList = []
count = 0
res = []

for i in range(len(listOfList)):
    sumList.append(sum(listOfList[i]))

for ch in sumList:
    res.append(ch/len(listOfList[count]))
    count += 1

print("SumList: ", sumList)
print("result: ", res)


