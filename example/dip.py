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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuthorizer(Authorizer):
    authorized = False

    def verify_code(self, code: str):
        print(f"verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class WhatsappAuthorizer(Authorizer):
    authorized = False

    def verify_wa_code(self, wa_code: str):
        print(f"verifying whatsapp code {wa_code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str, authorizer: Authorizer) -> None:
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order: Order) -> None:
        if not self.authorizer.is_authorized():
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
    def __init__(self, security_code: str, authorizer: Authorizer) -> None:
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order: Order) -> None:
        if not self.authorizer.is_authorized():
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
    authorizer = WhatsappAuthorizer()
    payment = GopayPaymentProcessor("123", authorizer)
    authorizer.verify_wa_code("wa009")
    order.add_item("sari roti", 3, 7500)
    order.add_item("indomilk choco", 2, 5300)
    print(order.total_price())
    payment.pay(order)


if __name__ == "__main__":
    main()
