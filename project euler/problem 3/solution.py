n = 600851475143
i = 2
while i*i<n+1:
    if n%i==0:n=n/i
    else:i+=1
print (n)
