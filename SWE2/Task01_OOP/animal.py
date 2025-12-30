from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def info(self):
        print(f"Animal: {self.name}")

class Dog(Animal):
    def make_sound(self):
        return "Woof! 🐶"

    def move(self):
        return "Runs on four legs."

    def eat(self):
        return "Eats bones and meat."

class Cat(Animal):
    def make_sound(self):
        return "Meow! 🐱"

    def move(self):
        return "Walks silently and jumps gracefully."

    def eat(self):
        return "Eats fish and milk."

class Bird(Animal):
    def make_sound(self):
        return "Chirp! 🐦"

    def move(self):
        return "Flies in the sky."

    def eat(self):
        return "Eats worms and grains."

class Fish(Animal):
    def make_sound(self):
        return "..."

    def move(self):
        return "Swims in water."

    def eat(self):
        return "Eats small insects and plants."

class Horse(Animal):
    def make_sound(self):
        return "Neigh! 🐴"

    def move(self):
        return "Runs fast on open fields."

    def eat(self):
        return "Eats grass and hay."

def show_animal_details(animal):
    animal.info()
    print(f"Sound: {animal.make_sound()}")
    print(f"Movement: {animal.move()}")
    print(f"Diet: {animal.eat()}")
    print("-" * 50)

animals = [
    Dog("Buddy"),
    Cat("Luna"),
    Bird("Kiwi"),
    Fish("Nemo"),
    Horse("Thunder")
]

for a in animals:
    show_animal_details(a)
