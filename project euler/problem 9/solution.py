# range received from 1000-2
print([a*b*(a*a+b*b)**0.5 for a in range(1,500) for b in range(a,500) if a+b+(a*a+b*b)**0.5==1000])