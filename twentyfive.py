# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

tupleOfTuples = eval(input("Enter tuple of tuples: "))
userSearch = input("Enter a String to Search in Tuple of Tuples: ")
listOfLists = [list(x) for x in tupleOfTuples]

for ch in listOfLists:
    for i in ch:
        if userSearch == i:
            print("check if", userSearch, " present in tuple of tuples ")
            print(True)
            break
        else:
            print("check if", userSearch, " present in tuple of tuples ")
            print(False)
            break
    break
