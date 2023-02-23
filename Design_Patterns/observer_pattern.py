# You are building a trading app and want to 
# notify users when the stock price changes.
# The Observer pattern can be used to notify users of the changes.

# We will create 2x classes - User and Stock.
# The Stock class will be the observable object, being watched for changes.
# The User class will be the observer, and will be notified of any changes.

from random import randint
class Stock:
    def __init__(self, symbol: str, price: float) -> None:
        self.symbol = symbol
        self.price = price
        self.observers = set()

    def attach(self, observer):
        self.observers.add(observer)
    
    def dettach(self, observer):
        self.observers.remove(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update(self)
    
    def set_price(self, price: float):
        self.price = price
        self.notify()
    

class User:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def update(self, stock) -> str:
        print(f'{self.name} recieved an update for {stock.symbol}: {stock.price}')


google: Stock = Stock('GOOG', 957.89)
facebook: Stock = Stock('FB', 320.40)



user1: User = User('John')
user2: User = User('Jane')

google.attach(user1)
google.attach(user2)
facebook.attach(user1)
facebook.attach(user2)

google.set_price(1240.15)
facebook.set_price(635.01)



# Output
# Jane recieved an update for GOOG: 1240.15
# John recieved an update for GOOG: 1240.15
# Jane recieved an update for FB: 635.01
# John recieved an update for FB: 635.01