Description
Description This task involves the implementation of advanced Object-Oriented Programming (OOP) design patterns to manage geometric shapes. The goal was to refactor standard class logic into scalable, maintainable patterns. The following design patterns were implemented in the solution:

Singleton Pattern:

Implemented within the ShapeFactory class.

Ensures that only one instance of the factory exists throughout the program's lifecycle by overriding the __new__ method and checking if an instance is already created.

Factory Method Pattern:

Implemented via the ShapeFactory.create_shape static method.

Centralizes the object creation logic. It takes a shape_type string (e.g., "circle", "cube") and returns the corresponding object instance, hiding the instantiation logic from the client code.

Composite Pattern:

Implemented via the ShapeGroup class.

Allows individual objects (like circle or square) and compositions of objects (groups of shapes) to be treated uniformly.

The ShapeGroup calculates the total area and perimeter by iterating through its child components, demonstrating recursive structure handling.

Template Method Pattern:

Implemented in the ShapeReporter class.

Defines the skeleton of an algorithm in the report_all_measurements method.

It calls a series of hooks (_calculate_area, _calculate_perimeter, _calculate_volume). The steps are fixed, but the implementation of these steps relies on the specific shape subclass (deferring definition to the subclasses).
