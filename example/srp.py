"""
Here's a Single Responsibility
"""


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


class PaymentProcessor:
    def pay_debit(self, order: Order, security_code):
        print("processing debit payment")
        print(f"verifying security code {security_code}")
        status = order.status = "paid"
        print(status)

    def pay_credit(self, order: Order, security_code):
        print("processing credit payment")
        print(f"verifying security code {security_code}")
        status = order.status = "paid"
        print(status)

    def pay_gopay(self, order:Order, security_code):
        print("processing credit payment")
        print(f"verifying security code {security_code}")
        status = order.status = "paid"
        print(status)


def main():
    order = Order()
    payment = PaymentProcessor()

    order.add_item("sari roti", 3, 7500)
    order.add_item("indomilk choco", 2, 5300)
    print(order.total_price())
    payment.pay_gopay(order, "t5j6kl")


if __name__ == "__main__":
    main()
