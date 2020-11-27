class Fruit(object):
    def __init__(self):
        print("You just picked a fruit")

    def nutrition(self):
        print("Fruits are healthy")

    def fruit_shape(self):
        print("There are lots of fruit shapes")


class Mango(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("You just picked a Mango")

    def nutrition(self):
        print("This fruit has a lot of sugar")

    def color(self):
        print("This fruit is color yellow")


f = Fruit()
f.nutrition()
f.fruit_shape()

print('*' * 50)

m = Mango()
m.nutrition()
m.fruit_shape()
m.color()