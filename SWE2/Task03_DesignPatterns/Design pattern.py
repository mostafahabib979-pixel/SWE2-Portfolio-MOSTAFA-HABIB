from abc import ABC, abstractmethod
import math


class area(ABC):
    @abstractmethod
    def area(self):
        pass


class perimeter(ABC):
    @abstractmethod
    def perimeter(self):
        pass


class volume(ABC):
    @abstractmethod
    def volume(self):
        pass

class shape(ABC):

    def __init__(self, name):
        self.name = name

    def showInfo(self):
        print(f"Name : {self.name}")

    def _calculate_area(self):
        raise NotImplementedError("Area calculation not defined for this shape.")

    def _calculate_perimeter(self):
        raise NotImplementedError("Perimeter calculation not defined for this shape.")

    def _calculate_volume(self):
        raise NotImplementedError("Volume calculation not defined for this shape.")

class circle(shape,perimeter,area):

    def __init__(self, radius):
        super().__init__("circle")
        self._radius = 0
        self.setradius(radius)


    def setradius(self, newradius):
        if newradius <= 0:
            raise ValueError("Radius must be a positive number.")
        else:
            self._radius = newradius

    def area(self):
        return math.pi * self._radius * self._radius


    def perimeter(self):
        return (2 * math.pi * self._radius)

    def _calculate_area(self):
        return self.area()

    def _calculate_perimeter(self):
        return self.perimeter()

class rectangle(shape,perimeter,area):
    def __init__(self, width, length):
        super().__init__("rectangle")
        self._width = 0
        self._length = 0
        self.setwidth(width)
        self.setlength(length)



    def setwidth(self, width):
        if width <= 0:
            raise ValueError("Width must be a positive number.")
        else:
            self._width = width



    def setlength(self, length):
        if length <= 0:
            raise ValueError("Length must be a positive number.")
        else:
            self._length = length


    def area(self):
        return self._width * self._length


    def perimeter(self):
        return ( self._width + self._length ) * 2

    def _calculate_area(self):
        return self.area()

    def _calculate_perimeter(self):
        return self.perimeter()

class square(shape,perimeter,area):
    def __init__(self, length):
        super().__init__("square")
        self._length = 0
        self.setlength(length)



    def setlength(self, length):
        if length <= 0:
            raise ValueError("Length must be a positive number.")
        else:
            self._length = length


    def area(self):
        return self._length * self._length


    def perimeter(self):
        return self._length * 4

    def _calculate_area(self):
        return self.area()

    def _calculate_perimeter(self):
        return self.perimeter()



class ball(shape,volume):
    def __init__(self, radius):
        super().__init__("ball")
        self._radius = 0
        self.setradius(radius)


    def setradius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        else:
            self._radius = radius


    def volume(self):
        return 4/3 * math.pi * self._radius * self._radius * self._radius

    def _calculate_volume(self):
        return self.volume()



class cube(shape, volume):
    def __init__(self, length):
        super().__init__("cube")
        self._length = 0
        self.setlength(length)


    def setlength(self, length):
        if length <= 0:
            raise ValueError("Length must be a positive number.")
        else:
            self._length = length


    def volume(self):
        return self._length * self._length * self._length

    def _calculate_volume(self):
        return self.volume()



class RectangulerPrism(shape,volume):
    def __init__(self, width, length, height):
        super().__init__("rectanguler Prism")
        self._width = 0
        self._length = 0
        self._height = 0
        self.setwidth(width)
        self.setlength(length)
        self.setheight(height)


    def setwidth(self, width):
        if width <= 0:
            raise ValueError("Width must be a positive number.")
        else:
            self._width = width


    def setlength(self, length):
        if length <= 0:
            raise ValueError("Length must be a positive number.")
        else:
            self._length = length

    
    def setheight(self, height):
        if height <= 0:
            raise ValueError("Height must be a positive number.")
        else:
            self._height = height


    def volume(self):
        return self._width * self._length * self._height

    def _calculate_volume(self):
        return self.volume()


#Composite------------------------------------------------------------------
class ShapeGroup(shape, area, perimeter):

    def __init__(self, name="2D Shapes Group"):
        super().__init__(name)
        self.components = []

    def add(self, component):

        if isinstance(component, (area, perimeter)):
            self.components.append(component)
        else:
            raise TypeError("Component must be a 2D shape")

    def remove(self, component):

        self.components.remove(component)

    def area(self):

        return sum(c.area() for c in self.components)

    def perimeter(self):

        return sum(c.perimeter() for c in self.components)

    def showInfo(self):

        super().showInfo()
        print(f"  --- Contains {len(self.components)} components:")
        for i, c in enumerate(self.components):
            print(f"  {i+1}. {c.name}")
        print("  ---\n")

    def _calculate_area(self):
        return self.area()

    def _calculate_perimeter(self):
        return self.perimeter()
#---------------------------------------------------------------------------


#Factory Method ------------------------------------------------------------
class ShapeFactory:


    @staticmethod
    def create_shape(shape_type, **kwargs):

        shape_type = shape_type.lower()

        if shape_type == 'circle':
            return circle(kwargs['radius'])
        elif shape_type == 'rectangle':
            return rectangle(kwargs['width'], kwargs['length'])
        elif shape_type == 'square':
            return square(kwargs['length'])
        elif shape_type == 'ball':
            return ball(kwargs['radius'])
        elif shape_type == 'cube':
            return cube(kwargs['length'])
        elif shape_type == 'rectangularprism':
            return RectangulerPrism(kwargs['width'], kwargs['length'], kwargs['height'])
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

#---------------------------------------------------------------------------


#Templete ------------------------------------------------------------------
class ShapeReporter:


    def __init__(self, shape_object: shape):
        self.shape_object = shape_object


    def report_all_measurements(self):


        shape_name = self.shape_object.name.capitalize()

        print(f"\nReport for ======== {shape_name} ========")


        hooks = [
            (self.shape_object._calculate_area, "Area"),
            (self.shape_object._calculate_perimeter, "Perimeter"),
            (self.shape_object._calculate_volume, "Volume"),
        ]


        for hook, unit in hooks:
            try:

                value = hook()

                print(f"- {unit}: {value:.2f}")

            except NotImplementedError:

                print(f"- {unit}: (Not defined for this shape type)")

        print(f"\n=====================================")

#---------------------------------------------------------------------------


#--------------main code-----------------

print("-" * 50)

print("### 1. Creating Shapes using Factory Method :")

s_circle = ShapeFactory.create_shape('circle', radius=5)
s_rectangle = ShapeFactory.create_shape('rectangle', width=4, length=6)
s_square = ShapeFactory.create_shape('square', length=3)
s_ball = ShapeFactory.create_shape('ball', radius=2)
s_cube = ShapeFactory.create_shape('cube', length=3)
s_prism = ShapeFactory.create_shape('rectangularprism', width=2, length=5, height=4)
print("Successfully created all shapes.\n")


print("-" * 50)


print("### 2. Grouping Shapes using Composite Pattern :")


group_2d = ShapeGroup("2D Shapes")
group_2d.add(s_circle)
group_2d.add(s_rectangle)


master_group = ShapeGroup("Master Collection")
master_group.add(group_2d)
master_group.add(s_square)

group_2d.showInfo()
master_group.showInfo()

print(f"\n**Master Group Calculations :**")

print(f"Total Master Area: {master_group.area():.2f}")
print(f"Total Master Perimeter: {master_group.perimeter():.2f}\n")

print("-" * 50)


print("### 3. Reporting using Template Method :")


print("Report: Circle (2D)")
ShapeReporter(s_circle).report_all_measurements()


print("Report: Cube (3D)")
ShapeReporter(s_cube).report_all_measurements()


print("Report: Master Collection (Composite)")
ShapeReporter(master_group).report_all_measurements()