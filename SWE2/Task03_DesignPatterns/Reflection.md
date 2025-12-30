Reflection


What I learned 

I learned how to use Python's __new__ dunder method to control instance creation, which is essential for implementing the Singleton pattern correctly.

I gained a deeper understanding of the Composite pattern, specifically how to design a common interface (inheriting from shape, area, perimeter) that allows a list of objects to be processed exactly like a single object.

I learned how to utilize the abc module to enforce strict interfaces, ensuring that concrete classes provide necessary implementations for the Template pattern to function without crashing.


What was challenging 

Implementing the Template Method in ShapeReporter was challenging because 2D shapes (like Circles) do not have volume, and 3D shapes (like Cubes) do not have a standard "area" in the same context. I had to implement error handling (try...except NotImplementedError) within the template loop to ensure the report generation didn't fail when a measurement wasn't applicable.

Ensuring the Composite ShapeGroup only accepted compatible components (shapes that support area/perimeter) required careful type checking in the add method.


What I improved from previous tasks 

I improved my code modularity by decoupling the object creation from the main execution logic using the Factory pattern, whereas in previous tasks I instantiated classes directly in the main block.

I improved the scalability of my code; previously, adding a new operation (like reporting) required modifying every shape class. With the Template pattern, I created a single reporter class that handles all shapes dynamically.
