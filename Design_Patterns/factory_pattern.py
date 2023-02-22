# We have a shop selling different products.
# We want to create an object to represent our product and its properties
# A Factory design pattern will allow us to craete a ProductFactory class
# to allow us to create instances of the different type of products we want to selll.

# base class - all products inherits from this
class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


class Clothing(Product):
    def __init__(self, name: str, price: float, size: str) -> None:
        super().__init__(name, price)
        self.size = size


class Electronics(Product):
    def __init__(self, name: str, price: float, warranty: str) -> None:
        super().__init__(name, price)
        self.warranty = warranty


class Book(Product):
    def __init__(self, name: str, price: float, author: str) -> None:
        super().__init__(name, price)
        self.author = author


# this class creates the individual products
class ProductFactory:
    def create_product(self, product_type: str, *args: tuple):
        if product_type == 'clothing':
            return Clothing(*args)
        elif product_type == 'electronics':
            return Electronics(*args)
        elif product_type == 'book':
            return Book(*args)
        else:
            raise ValueError(f'Invalid product type: {product_type}')


# implementation
factory: ProductFactory = ProductFactory()
product1: Clothing = factory.create_product('clothing', 'T-Shirt', 19.99, 'L')
product2: Electronics = factory.create_product('electronics', 'Smartphone', 799.99, '2 years')
product3: Book = factory.create_product('book', 'Python for Data Science Handbok', 49.99, 'Jake VanderPlas')

print(f'Product 1: {product1.name}, {product1.price}, {product1.size}')
print(f'Product 2: {product2.name}, {product2.price}, {product2.warranty}')
print(f'Product 3: {product3.name}, {product3.price}, {product3.author}')

# Output
# Product 1: T-Shirt, 19.99, L
# Product 2: Smartphone, 799.99, 2 years
# Product 3: Python for Data Science Handbok, 49.99, Jake VanderPlas