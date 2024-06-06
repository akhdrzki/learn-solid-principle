"""
Here's a Liskov Substitution.
"""

from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "Open"

    def add_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self) -> int:
        total = 0

        for quantity, price in zip(self.quantities, self.prices):
            total += quantity * price
        return total


"""
Abstract method.
We also define more abstract method in PaymentProcessor Class, the purpose is assume that our subclass does need auth_sms to verifying transaction,
So here we defined the abstractmethod 
"""


class PaymentProcessor(ABC):
    @abstractmethod
    def auth_sms(self, code: str) -> None:
        pass

    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code: str) -> None:
        print(f"verifying sms code {code}")
        self.verified = True

    def pay(self, order: Order) -> None:
        if not self.verified:
            raise Exception("unauthorized")

        print("processing debit payment")
        print(f"verifying security code {self.security_code}")
        status = order.status = "paid"
        print(status)


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order) -> None:
        print("processing credit payment")
        print(f"verifying security code {self.security_code}")
        status = order.status = "paid"
        print(status)


class GopayPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code: str) -> None:
        print(f"verifying sms code {code}")
        self.verified = True

    def pay(self, order: Order) -> None:
        if not self.verified:
            raise Exception("unauthorized")

        print("processing gopay payment")
        print(f"verifying security code {self.security_code}")
        status = order.status = "paid"
        print(status)


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_code: str) -> None:
        self.email_code = email_code

    def pay(self, order: Order) -> None:
        print("processing paypal payment")
        print(f"verifying security code {self.email_code}")
        status = order.status = "paid"
        print(status)


def main():
    order = Order()
    payment = GopayPaymentProcessor("123")

    order.add_item("sari roti", 3, 7500)
    order.add_item("indomilk choco", 2, 5300)
    print(order.total_price())
    payment.auth_sms("0091")
    payment.pay(order)


if __name__ == "__main__":
    main()
