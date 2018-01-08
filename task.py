a = int(input())
b = int(input())
c = int(input())
if a >= b:
    a, b = b, a
    if b >= c:
        b, c = c, b
    if a >= b:
        a, b = b, a
elif a >= c:
    a, c = c, a
    if b >= c:
        b, c = c, b
else:
    if b >= c:
        b, c = c, b
print(a, b, c)
