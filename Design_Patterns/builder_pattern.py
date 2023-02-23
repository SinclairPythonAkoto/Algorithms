# You have an app that allows customers to make their own custom sandwiches.
# The user can choose the type of bread, meat, cheese, vegetables and/or condiments.
# The builder pattern will allow us to create the sandwich with the custom ingredients.
# We will build a SandwichBuilder class that can build different types of sandwhiches.


class Sandwich:
    def __init__(self) -> None:
        self.bread = None
        self.meat = None
        self.cheese = None
        self.vegetables = []
        self.condiments = []

    def __str__(self) -> str:
        return f'{self.bread} sandwich with {self.meat}, {self.cheese}, {",".join(self.vegetables)}, and {",".join(self.condiments)}'


class SandwichBuilder:
    def __init__(self) -> None:
        self.sandwich: Sandwich = Sandwich()

    def add_bread(self, bread) -> None:
        self.sandwich.bread = bread
    
    def add_meat(self, meat) -> None:
        self.sandwich.meat = meat
    
    def add_cheese(self, cheese) -> None:
        self.sandwich.cheese = cheese
    
    def add_vegetables(self, *vegetables) -> None:
        self.sandwich.vegetables.extend(vegetables)
    
    def add_condiments(self, *condiments) -> None:
        self.sandwich.condiments.extend(condiments)
    
    def get_sandwich(self):
        return self.sandwich
    

# implementation
builder: SandwichBuilder = SandwichBuilder()
builder.add_bread("wheat")
builder.add_meat("tuna")
builder.add_cheese("Mozzarella")
builder.add_vegetables("lettuce", "tomato", "onions")
builder.add_condiments("ketchup", "hot sauce")

sandwich: Sandwich = builder.get_sandwich()
print(f"You ordered: {sandwich}")

# Output
# You ordered: wheat sandwich with tuna, Mozzarella, lettuce,tomato,onions, and ketchup,hot sauce