class Organism:
    isAlive =True
    def eat(self):
        print("This organism consume food to survive")
class Animal(Organism):
    def run(self):
        print("this animals can run")

class Lion(Animal):
    def chase(self):
        print("the lion chases other animals")  

lion = Lion()
print(lion.isAlive)
lion.run()
lion.chase()
lion.eat()
