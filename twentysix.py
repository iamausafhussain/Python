
# (1,2,3,4) (3,5,2,1) (2,2,3,1)
a = eval(input("Enter tuple a: "))
b = eval(input("Enter tuple b: "))
c = eval(input("Enter tuple c: "))

a = list(a)
b = list(b)
c = list(c)
sum = []

for i in range(0, len(a)):
    sum.append(a[i] + b[i] + c[i])
print(tuple(sum))

