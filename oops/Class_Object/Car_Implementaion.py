from Car import Car

car1 = Car("maruthi","dezire",'grey',2017)
print("car variable",Car.wheels)#class variable
car1.wheels = 3 #object variable

print(car1.manufacturer)
print(car1.color)
print(car1.model)
print(car1.year)

print(car1.__dict__)

for key,value in car1.__dict__.items():
    print(key," : ", value)

car1.start()
car1.drive()
car1.stop()