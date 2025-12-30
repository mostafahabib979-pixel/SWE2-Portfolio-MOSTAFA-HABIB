Reflection: Geometric Shapes & Design Patterns
What I Learned
Through this task, I gained a deeper understanding of how to implement Design Patterns in a practical scenario. Specifically:

I learned how the Composite Pattern simplifies the management of complex hierarchies, such as treating a group of shapes as a single object.

I practiced implementing the Singleton Pattern to control resource instantiation for a Factory class.

I learned how to use Abstact Base Classes (ABC) to enforce contracts for area, perimeter, and volume calculations across different classes.

What Was Challenging
The most challenging part was implementing the Template Method in the ShapeReporter class. I had to ensure that the reporter could gracefully handle shapes that do not support certain measurements (e.g., a Circle does not have a Volume) by catching NotImplementedError.

Setting up parameterized unit tests in pytest required careful organization to ensure both expected successes and failures were handled correctly within the same test functions.

What I Improved from Previous Tasks
Input Validation: I improved the robustness of my classes by using @property setters to ensure that dimensions like radius and length are always positive numbers, raising ValueError otherwise.

Testing Coverage: Compared to previous tasks, I increased my testing rigor by including "fail" scenarios in my test data to verify that my assertions correctly identify incorrect calculations.
