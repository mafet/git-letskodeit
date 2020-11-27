car = {"make": "Mazda", "model" : "3", "year" : "2015"}


try:
    print(car["color"])
except:
    print("No such thing!")
finally:
    print("You are awesome!")
