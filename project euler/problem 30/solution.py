# upper bound received from (9^5 + 9^5 + 9^5 + 9^5 + 9^5)+1
print(sum([n for n in range(295246) if n==sum([int(num)**5 for num in str(n)])])-1)