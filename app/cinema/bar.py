from app.people.customer import Customer as Customer


class CinemaBar:
    def __init__(self) -> None:
        pass

    @staticmethod
    def sell_product(product: str, customer: "Customer") -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
