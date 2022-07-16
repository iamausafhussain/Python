# [(), (), (), ('a', 'b'), ('a', 'b', 'c'), ('d')]
listOfTuples = eval(input("Enter list of tuples: "))

listOfList = [list(x) for x in listOfTuples]
res = list(filter(None, listOfList))
listOfTuples = [tuple(x) for x in res]

print(listOfTuples)