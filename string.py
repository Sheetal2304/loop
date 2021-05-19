string="sheetal navgurukul student"
i=0
while i<len(string):
	if string[i]=="a":
		i+=1
		continue
	if string[i]=="u":
		i=i+1
		continue
	print(string[i],end="")
	i=i+1