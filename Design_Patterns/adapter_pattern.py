"""Adaptor Pattern

Suppose you have a third-party payment gateway that provides an interface for processing payments. 
However, you have a new requirement to use a different payment gateway that has a different interface. 
You could write a new payment processing class that implements the new interface, 
but this would require a lot of code duplication. The Adapter pattern could be used
to create a class that adapts the old payment processing class to the new interface.
"""

class OldPaymentGateway:
    def process_payment(self, amount: int) -> str:
        print(f'Processing payment for amount {amount}')


class NewPaymentGateway:
    def process(self, amount: int) -> str:
        print(f'Processing payment for amount {amount}')


# uses OPG method by passing OPG class in init
class PaymentGatewayAdapter:
    def __init__(self, old_gateway: OldPaymentGateway):
        self.old_gateway = old_gateway
    
    def process(self, amount):
        self.old_gateway.process_payment(amount)  # need to pass in OPG object to use the method


old_gateway: OldPaymentGateway = OldPaymentGateway()
adapter: PaymentGatewayAdapter = PaymentGatewayAdapter(old_gateway)
new_gateway: NewPaymentGateway = NewPaymentGateway()

amount: int = 100
adapter.process(amount)
new_gateway.process(amount)


# Output
# Processing payment for amount 100
# Processing payment for amount 100