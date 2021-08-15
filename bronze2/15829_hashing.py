import math

L = int(input())
s = str(input())

sum = 0
r = 31
M = 1234567891
for i in range(L):
    sum += ((ord(s[i]) - 96) * (r ** i))

sum = sum % M

print(sum)