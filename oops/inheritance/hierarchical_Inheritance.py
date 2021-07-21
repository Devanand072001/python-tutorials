class Animal:
    isAlive = True

    def sleep(self):
        print("this animal is sleeping...")

    def eat(self):
        print("this animal is eating>>>")


class Dog(Animal):
    # ovveriding
    def sleep(self):
        print("the dog is sleeping")

    def run(self):
        print("The dog can run")


class Eagle(Animal):
    # ovveriding
    def sleep(self):
        print("the eagle is sleeping")

    def fly(self):
        print("the eagle can fly")


class Shark(Animal):
    # ovveriding
    def sleep(self):
        print("the shark is sleeping")

    def swim(self):
        print("shark can swim")


dog = Dog()
eagle = Eagle()
shark = Shark()

dog.run()
eagle.fly()
shark.swim()

dog.sleep()
eagle.sleep()
shark.sleep()
