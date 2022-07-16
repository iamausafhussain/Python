l = eval(input("Enter list of numbers: "))

for i in l:
    if i == max(l):
        print("max position is", l.index(i))
    elif i == min(l):
        print("min position is", l.index(i))