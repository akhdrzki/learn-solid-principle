"""
Here's a Open Closed, it means always open for extension but closed for modified existing class.
"""

from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = []

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


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("processing debit payment")
        print(f"verifying security code {security_code}")
        status = order.status == "paid"
        print(status)


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("processing credit payment")
        print(f"verifying security code {security_code}")
        status = order.status == "paid"
        print(status)


class GopayPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("processing credit payment")
        print(f"verifying security code {security_code}")
        status = order.status == "paid"
        print(status)


def main():
    order = Order()
    payment = GopayPaymentProcessor()

    order.add_item("sari roti", 3, 7500)
    order.add_item("indomilk choco", 2, 5300)
    print(order.total_price())
    payment.pay(order, "t6jskf")


if __name__ == "__main__":
    main()
