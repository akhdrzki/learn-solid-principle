"""
Here's a basic example, my goals here to update these code into more readable with Single Responsibility.. 
It means i should separate some method that has its own responsibilites.. at this case we'll be separate pay method as possible.
Checking srp.py for the updated:)
"""


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
        for i in range(len(self.prices)):
            total += self.prices[i] * self.quantities[i]
        return total

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("processing debit payment type")
            print(f"verifying security code {security_code}")
        elif payment_type == "credit":
            print("processing credit payment type")
            print(f"verifying security code {security_code}")
        elif payment_type == "gopay":
            print("processing gopay payment type")
            print(f"verifying security code {security_code}")


def main():
    order = Order()

    order.add_item("sari roti", 3, 7500)
    order.add_item("indomilk choco", 2, 5300)
    print(order.total_price())
    order.pay("gopay", "50rt3d")


if __name__ == "__main__":
    main()
