def checkGeneratable(a):
    ls = list(map(int, str(a)))
    i = len(ls)
    sum = 0
    while sum < a:
        sum = 0
        for j in range(i):
            sum = sum + ls[len(ls)-j-1]
        ls.append(sum)
    if a == ls[-1]:
        return 1
    else:
        return 2


n = int(input())
ns = str(n)
k = int(input())
b=ns[len(ns) - k :]
a = checkGeneratable(int(b))
if a == 1:
    print("Generated")
else:
    print("Cannot be Generated")


