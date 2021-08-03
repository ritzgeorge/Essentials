filename=print(input('enter filename '))
file=open('filename','r+')
f=file.write()
if f =='':
	print('no such file')
	i=input('enter the text')
	filenew=('filename.txt','w')
else: 
	r=input('read file y/n')
	if r=='y':
		print(f)
	if r =='n':
		print(' ')
d=input('delete file y/n')
if d=='y':
	print('deleted')

filename.close()				
		


