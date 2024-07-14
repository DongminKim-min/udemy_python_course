'''Unlimited Arguments'''

def add(*args):
    print(args[2]) #args: tuple
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(3, 4, 5, 6)

def calculate(n, **kwargs):
    print(kwargs) # kwargs: dict
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self,**kw):
        self.make = kw.get("make") # .get() -> it doesn't make errors even if there is no corresponding argument
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make= "Nissan", model="GT-R", seats=4)
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)