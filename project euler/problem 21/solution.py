d, t = {}, 0
x = int(input("check up to: "))
for n in range(x+1):
    d[n] = sum([j for j in range(1,n) if n%j==0])
    if d[n] in d and d[d[n]]==n and n!=d[n]:t+=n+d[n]
print(t)