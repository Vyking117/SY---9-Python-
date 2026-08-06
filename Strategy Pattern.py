# Parent Class 
class PaymentStrategy:

    # This method will be overridden
    def pay(self, amount):
        pass


# Credit Card Strategy
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")
        print("Reward Points Earned: 20")
        print("Payment Successful!\n")


# PayPal Strategy
class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")
        print("Reward Points Earned: 10")
        print("Payment Successful!\n")


# UPI Strategy (Novelty)
class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
        print("Reward Points Earned: 15")
        print("Payment Successful!\n")


# Context Class
class PaymentContext:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


# Main Program

payment = PaymentContext(CreditCardPayment())
payment.pay(1000)

payment.set_strategy(PayPalPayment())
payment.pay(500)

payment.set_strategy(UPIPayment())
payment.pay(700)