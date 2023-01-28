# [Abstract Base Classes]
from collections import namedtuple
from abc import ABC, abstractclassmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
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

    @abstractclassmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


stream = MemoryStream()
stream.open()

# [Polymorphism]


class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])

# [Duck Typing] Remove the baseclass UIControl above (demo)


# [Extending Built-in Types]


class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.lower())
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")

# [Data Classes]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(id(p1))
print(id(p2))


Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
p3 = Point(x=10, y=20)
print(p1 == p2)
