user=int(input("enter the number"))
x=user
sum=0
while user>0:
	a=user%10
	user=user//10
	sum+=a
# print(sum)
if x%sum==0:
	print("it is a harshad number")
else:
	print("it is not a harshad number")