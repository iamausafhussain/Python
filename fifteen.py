# [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'), ('item4', '1.1')]

tuple = eval(input("Enter a list of tuple strings: "))

list = [list(elem) for elem in tuple]
# print(list)

float__list = []

for ch in list:
    print(ch[1][1])
    float__list = sorted(float__list, key=lambda x: float(x))

print(float__list)
