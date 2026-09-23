from math import *
S = int(input())
lim = isqrt(S)
for a in range(lim + 1):
    b2 = S - a * a
    b = isqrt(b2)
    if b * b == b2:
        print("YES")
        print(0, 0)
        print(a, b)
        print(a - b, a + b)
        print(-b, a)
        break
else:
    print("NO")