# Parent Class
class Animal:
    def __init__(self, name, colour, food):
        self.name = name
        self.colour = colour
        self.food = food


    def make_noise(self):
        return f"I am a cat and I like mice"

# Child 1 Class
class Cat(Animal):
    def __init__(self, name, colour, food, number_of_paws):
        super().__init__(name, colour, food)
        self.number_of_paws = number_of_paws


# Child 2 Class
class Chicken(Animal):
    def __init__(self, name, colour, food, number_of_legs):
        super().__init__(name, colour, food)
        self.number_of_legs = number_of_legs

    def make_noise(self):
        return f"I am a chicken and I do cluck, cluck!"

chicken = Chicken("Ada", "yellow", "grain", 2)
print(chicken.name)
print(chicken.colour)
print(chicken.make_noise())

cat = Cat("Mona", "black", "mice", 4)
print(cat.name)
print(cat.colour)
print(cat.make_noise())
