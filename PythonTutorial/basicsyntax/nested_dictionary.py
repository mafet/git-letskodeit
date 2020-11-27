cars = {'bmw':{'model':'550i', 'year': 2016},
        'benz':{'model':'E3250', 'year': 2015}
        }


car = {'make':'bmw', 'year': 2016, 'model':'550i'}
print(car.keys())
print(cars.keys())
print('*' * 50)
print(car.values())
print(cars.values())
print('*' * 50)
print(car.items())
print(cars.items())

print('*' * 50)
car_copy = car.copy()
print(car_copy)

print(car.pop('model'))
print(car)

d={"key1": ['a', 2, 'c'], "key2": [4, 5, 6], "key3": [7, 8, 9]}
print(d["key1"][2])