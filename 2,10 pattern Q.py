user=int(input("enter the number"))
i=2
j=10
count=1
while count<=user:
	if count>user:
		break
	if i%2==0:
		print(i,end=" ")
		print(j,end=" ")
		j=j+10
	count+=1	
	i+=1