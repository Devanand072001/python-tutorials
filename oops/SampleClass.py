class Myclass:
    def __init__(self, real=0, img=0):
        print("constructor executing")
        self.real_part = real
        self.img_part = img

    def displayNumber(self):
        print("{} + {}j".format(self.real_part, self.img_part))


complexNumber = Myclass(30, 39)
complexNumber.displayNumber()
print(complexNumber.real_part)