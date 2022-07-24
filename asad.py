
# 4
# red
# blue
# green
# yellow
# 1
# yellow

n = int(input())
l = []

for i in range(n):
    a = input()
    l.append(a)

startIndex = int(input())
target = input()

print(l)
l1 = l[startIndex::] + l[:startIndex:]
l2 = l[startIndex:: -1] + l[:startIndex: -1]
print(l1)
print(l2)

right = l1.index(target)
left = l2.index(target)

if right > left:
    print(left)
else:
    print(right)