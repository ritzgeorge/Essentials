songdictionay={1:'pumped up',2:'foster',3:'3.24',4:'alternative'}
print(songdictionay)
for i in range(4):
	print(songdictionay[i+1])
while(True):
	a=int(input('enter key\n'))
	
	if a in songdictionay:
		print('true')
	else:
		print('false')
	b=str(input('enter value'))
	if b in songdictionay:
		print('true')
	else:
		print('false')
		break


