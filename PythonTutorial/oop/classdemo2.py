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

c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()