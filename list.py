#listbto add unique values
myUniquelist=[]
myLeftovers=[]
def call(a):
	if a in myUniquelist:
	  print('false')
	  myLeftovers.append(a)
	else: 
	   	myUniquelist.append(a)
call(1)
call(2)
call(3)
call(4)
call(1)
call(2)
print(myUniquelist)
print(myLeftovers)
