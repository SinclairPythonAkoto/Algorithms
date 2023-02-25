# You are working on a e-commerce website that sell products.
# You want to implement a discount system that applies discounts
# to the different products, depending on the user type, season etc.
# The Strategy pattern could be used to define interchangeable algorithims,
# encapsulate each one, and then make them interchangeable.
# This will allow you to create 2x different operations from the same function, 
# inherited from a single base (abstract) class.


class Product:
    def __init__(self, name: str, price: int, category: str) -> None:
        self.name = name
        self.price = price
        self.category = category


# abstract class that defines interface for discounts
class Discount:
    def apply_discount(self, product: Product) -> float:
        """
        Applies discount to product and returns the discounted price.
        """
        raise NotImplementedError


class SeasonalDiscount(Discount):
    def apply_discount(self, product: Product) -> float:
        if product.category == 'clothing':
            return product.price * 0.8
        else:
            return product.price * 0.9


class MemberDiscount(Discount):
    def apply_discount(self, product: Product) -> float:
        if product.category == 'electronics':
            return product.price * 0.95
        else:
            return product.price * 0.9


class Checkout:
    def __init__(self, discount: Discount) -> None:
        self.discount = discount
    
    def calculate_total(self, products: list[Product]) -> float:
        total_price = 0
        for product in products:
            total_price += self.discount.apply_discount(product)
        return total_price


products: list[Product] = [
    Product('T-Shirt', 20, 'clothing'),
    Product('Shoes', 50, 'clothing'),
    Product('TV', 500, 'electronics'),
    Product('Phone', 800, 'electronics')
]

seasonal_discount: SeasonalDiscount = SeasonalDiscount()
member_discount: MemberDiscount = MemberDiscount()

checkout: Checkout = Checkout(seasonal_discount)
total_price: float = checkout.calculate_total(products)
print(f'Total price with seasonal discount: {total_price}')

checkout: Checkout = Checkout(member_discount)
total_price: float = checkout.calculate_total(products)
print(f'Total price with member discount: {total_price}')