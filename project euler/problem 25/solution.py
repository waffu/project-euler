a, b = 1, 1
l = [1]
while len(str(a)) < 1000:
    a, b = b, b+a
    l.append(a)
    print(a)
print(len(l))