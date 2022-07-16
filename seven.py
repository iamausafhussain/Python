l = eval(input("Enter a list of numbers: "))

even = []
odd = []

for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even list: ", even)
print("Odd list: ", odd)