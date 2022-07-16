
m1 = []
r1 = int(input("Enter number of rows of matrix 1: "))
c1 = int(input("Enter number of columns of matrix 1: "))

for i in range(r1):
    a = []
    for j in range(c1):
        a.append(int(input("Enter value: ")))
    m1.append(a)
print("Inputted matrix 1: ")
for i in range(r1):
    print(m1[i])

m2 = []
r2 = int(input("Enter number of rows of matrix 2: "))
c2 = int(input("Enter number of columns of matrix 2: "))

for i in range(r2):
    b = []
    for j in range(c2):
        b.append(int(input("Enter value: ")))
    m2.append(b)
print("Inputted matrix 2: ")
for i in range(r1):
    print(m2[i])

sum = []

if(r1 == r2 and c1 == c2):
    sum = [[m1[i][j] + m2[i][j]  for j in range(len(m1[0]))] for i in range(len(m1))]
else:
    print("Not compatible!!")

print("Sum: ")
for i in range(r1):
    print(sum[i])

