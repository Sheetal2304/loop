user=int(input("enter the number"))
count=0
i=1
while i<=user:
	if user%i==0:
		count+=1
	i+=1
if count==2:
	print('it is a prime number')
else:
	print('it is not a prime number')