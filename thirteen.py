tuplex = eval(input("Enter a tuple to reverse it: "))

listx = list(tuplex)
listx.reverse()
tuplex = tuple(listx)

print(tuplex)