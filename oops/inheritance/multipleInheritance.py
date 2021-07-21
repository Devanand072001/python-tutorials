class Pray:
    def flee(self):
        print("this animal flees")


class Predator:
    def hunt(self):
        print("This animal hunts")


class Deer(Pray):
    pass


class Tiger(Predator):
    pass


class Fish(Pray, Predator):  # multiple inheritance
    pass


deer = Deer()
fish = Fish()

deer.flee()

fish.flee()
fish.hunt()
