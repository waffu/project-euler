import time
cache = {}
largest = 0
start = time.time()
for n in range(2,1000000):
	c,x=0,n #x = unmodified n
	while n>1:
		if n in cache:
			c+=cache[n]
			break
		if n%2==0:
			n/=2 
			c+=1
		else:
			n=(n*3)+1 
			c+=1
	if c>largest:
		cache[x]=c+1
		largest=c
		ans = x
end = time.time()
print(end-start)
print(largest)
print(ans)
input()