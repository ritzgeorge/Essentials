class vehicle:
	def __init__(self,make,model,year,weight):
		self.make=make
		self.model=model
		self.year=year
		self.weight=weight
		self.tripssincemaintainance=0
		self.needsmaintance=False
	def needsmaintance(self):
		self.needsmaintance=False
		self.tripssincemaintainance=0
	def repair(self):
		self.needsmaintance=False
		self.tripssincemaintainance=0	


class car(vehicle):
	def __init__(self,make,model,year,weight):
		vehicle.__init__(self,make,model,year,weight)
	def drivng(self,drive):
		self.drive=drive
		if drive==True:
			print('driving')		
				
	def stop(self,drive):
		drive=False
		if drive==False:
			self.tripssincemaintainance+=1
		if self.tripssincemaintainance>100:
			self.needsmaintance=True	

car1=car('kia','seltos','2020',2040)
car2=car('benz','s class','1999',3000)
car3=car('bmw','m3','2000',2500)
car1.drivng(True)
car1.stop(False)
car1.repair()
print(car1.model,car1.make,car1.needsmaintance,car1.tripssincemaintainance)
print(car2.model)




				




