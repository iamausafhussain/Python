row = int(input("row: "))
col = int(input("col: "))

sum = 0
m = 0
id = 0

for i in range(row):
    for j in range(col):
        sum += int(input())
    if sum > m:
        m = sum
        id = i + 1
    sum = 0
print(id)
