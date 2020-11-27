class Car(object):
    def __init__(self):
        print("You just created a new car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stoped.")

"""
Inheritance
"""
class BMW(Car):
    def __init__(self):
        Car.__init__(self)
        print("You just created a BMW instance")

    def drive(self):
        super(BMW, self).drive()
        print("BMW started, enjoy your drive")

    def headlights(self):
        print("Headlights are on")

#c = Car()
#c.drive()
#c.stop()

b = BMW()
b.drive()
b.headlights()
b.stop()