class Car(object):

    wheels = 4
    windows = 4
    windshield = 1

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car is %s and model of the car is %s" %(self.make, self.model))



c1 = Car("Honda", "Civic")
c1.wheels = 3
print(c1.wheels)
c1.info()
c2 = Car("Mazda", "3")
c2.info()
print(c2.wheels)
print(Car.wheels)