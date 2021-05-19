user=int(input("enter the number"))
sum=0
i=1
while i<user:
	if user%i==0:
		sum+=i
	i=i+1
print(sum)	
if sum==user:
	print("it is a perfect number")
else:
	print("it's not a perfect number")