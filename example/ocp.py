"""
Here's a Open Closed, it means always open for extension but closed for modified existing class.
We have a problem here. We try to add more payment class we can assume it as Paypal payment.
The matter is Paypal doesn't use security code, its use email instead.
So here Open Closed Principle solved the problem by define subclass of parent class (PaymentProcessor) 
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
Abstract class that has similar purpose as Interface
"""


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order, security_code: str) -> None:
        pass


"""
Before we just define PaymentProcessor and write some method in it, here we created PaymentProcessor as Abstract Method, and created 
few subclass that has its own responsibilites. The focused is don't modified whole exists code as new purposes.
"""


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("processing debit payment")
        print(f"verifying security code {security_code}")
        status = order.status = "paid"
        print(status)


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("processing credit payment")
        print(f"verifying security code {security_code}")
        order.status = "paid"


class GopayPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("processing gopay payment")
        print(f"verifying security code {security_code}")
        status = order.status = "paid"
        print(status)


def main():
    order = Order()
    payment = DebitPaymentProcessor()

    order.add_item("sari roti", 3, 7500)
    order.add_item("indomilk choco", 2, 5300)
    print(order.total_price())
    payment.pay(order, "t6jskf")


if __name__ == "__main__":
    main()
