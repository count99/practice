class Dog:
    memo = "Human's friend or food."
    def __init__(self, color, kind):
            self.color = color
            self.kind = kind

    def bark(self):
        print ("{}.Ｗang....Wang....".format(self.color))

    @staticmethod
    def bite():
        print ("bite you")



Dog.bite()
a= Dog("黃狗", "大狗")
a.bark()