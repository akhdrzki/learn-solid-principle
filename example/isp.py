"""
Here's a Interface Segregation Principle. 
This principle solve our problem that in this case we have auth_sms but it does'nt need to place into all subclass. 
Because just 2 subclasses that does need this feature. So here we can create new abstractmethod but it does place on new subclass that prefer 
to PaymentProcessor as parent class. So now we can use the auth_sms for specific subclass.
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
"""


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


"""
This new subclass has auth_sms abstaction so it solve the matter for specific subclass acquired
"""


class PaymentProcessor_with_SMSAuth(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code: str) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor_with_SMSAuth):
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


class GopayPaymentProcessor(PaymentProcessor_with_SMSAuth):
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
