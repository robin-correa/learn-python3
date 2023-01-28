# [Properties]

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(10)
product.price = 1
print(product.price)

# [Inheritance]
# Animal2: Parent, Base
# Mammal2: Child, Sub


class Animal2:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal2 (Animal2):
    def walk(self):
        print("walk")


class Fish(Animal2):
    def swim(self):
        print("swim")


m = Mammal2()
m.eat()
print(m.age)

# [The Object Class] Note: Every class that we have (directly / indirectly) derives from the Object class

m = Mammal2()
print(isinstance(m, object))
print(issubclass(Mammal2, object))

# [Method Overriding]


class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)  # 1
print(m.weight)  # 2

# [Multiple Inheritance]


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass

# [A Good Example of Inheritance]


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
