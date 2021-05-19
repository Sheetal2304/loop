row=1
j=65
space=7
while row<=7:
	time=1
	print(space*" ",end=" ")
	while time<=row:
		print(chr(j),end=" ")
		time+=1	
	print()
	row+=2
	space-=2
	j+=1