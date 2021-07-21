class Car:
    # manufacturer = None
    # model = None
    # color = None
    # year = None
    wheels = 4 # class variable

    def __init__(self,manufacturer,model,color,year):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.year = year
    
    def start(self):
        print("the car engine reviving.....")
    
    def drive(self):
        print("the car is moving>>>>")

    def stop(self):
        print("the brakes are applied |||")