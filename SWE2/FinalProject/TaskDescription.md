
Task Description: Geometric Shapes System
Project Overview
This project implements a robust geometric shape management system using Python. It demonstrates the application of Object-Oriented Programming (OOP) principles and several Software Engineering design patterns to handle 2D and 3D shapes.

Features
Geometric Shapes: Support for Circle, Rectangle, Square, Ball, Cube, and Rectangular Prism.

OOP Principles: Utilizes abstraction, inheritance, and encapsulation with property decorators and validation.

Design Patterns:

Singleton: Ensures only one instance of the ShapeFactory exists.

Factory Method: Provides a centralized interface for creating various shape objects.

Composite Pattern: Allows grouping multiple 2D shapes into a ShapeGroup that can be treated as a single shape for area and perimeter calculations.

Template Method: The ShapeReporter defines a skeleton for reporting measurements (Area, Perimeter, Volume) while allowing specific shape implementations to provide the data.

Unit Testing: Comprehensive test suite using pytest with parameterized scenarios to verify both "pass" and "fail" logic for all shape calculations.
