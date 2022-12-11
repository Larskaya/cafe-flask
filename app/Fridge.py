class Fridge:
    def __init__(self) -> None:
        self.products_amount = 0
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        self.products_amount += 1

    def remove_product(self, product):
        self.products.remove(product)
        self.products_amount -= 1

    def check(self):
        items = {'amount': self.products_amount, 'products': self.products}
        return items
