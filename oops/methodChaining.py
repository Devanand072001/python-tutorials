# method chaining = calling multiple methods sequentially
# each call performs an action on the same object and returns self
class Car:
    def turnON(self):
        print("the engine turned on")
        return self

    def drive(self):
        print("the diver dives the car")
        return self

    def stop(self):
        print("The brakes are applied")
        return self

    def turn_Off(self):
        print("The engine turned off")
        return self


car = Car()
# car.turnON().drive()
car.turnON().drive().stop().turn_Off()
# the above can be written as
car.turnON()\
    .drive()\
    .stop()\
    .turn_Off()
