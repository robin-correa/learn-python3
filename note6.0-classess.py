# Notes:
# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack

# [Creating Classes]

class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))

# [Constructors]


class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point1(1, 2)
print(point.x)
point.draw()

# [Class vs Instance Attributes]


class Point2:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# Class level attributes shared across all instances of the class
Point2.default_color = "yellow"
point = Point2(1, 2)
print(point.default_color)  # Instance attribute
print(Point2.default_color)  # Class Reference attribute
point.draw()

another = Point2(1, 2)
another.draw()

# [Class vs Instance Methods]


class Point3:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point3(0, 0)
point = Point3.zero()
point.draw()

# [Magic Methods]


class Point4:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point4(1, 2)
print(str(point))

# [Comparing Objects]


class Point5:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point5(10, 20)
other = Point5(1, 2)

print(point == other)
print(point > other)

# [Performing Arithmetic Operations]


class Point6:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point6(self.x + other.x, self.y + other.y)


point = Point6(10, 20)
other = Point6(1, 2)
combined = point + other
print(combined.x)

# [Making Custom Containers]


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)  # {'python': 3}

# [Private Members]


class TagCloud2:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud2()
cloud.add("python")
cloud.add("python")
cloud.add("python")
# AttributeError: 'TagCloud2' object has no attribute '__tags'
print(cloud.__tags['PYTHON'])
