# cart
class Cart:
    def __init__(self):
        self.items = {}   # {product_name: {"price": x, "qty": y}}

    def add_item(self, name, price, qty=1):
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0")
        if price < 0:
            raise ValueError("Price cannot be negative")

        if name in self.items:
            self.items[name]["qty"] += qty
        else:
            self.items[name] = {"price": price, "qty": qty}

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"{name} not in cart")
        del self.items[name]

    def update_qty(self, name, qty):
        if name not in self.items:
            raise KeyError(f"{name} not in cart")
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.items[name]["qty"] = qty

    def get_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["qty"]
        return total

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100")
        total = self.get_total()
        discount = total * (percent / 100)
        return round(total - discount, 2)

    def item_count(self):
        return sum(item["qty"] for item in self.items.values())

    def clear(self):
        self.items = {}

    def is_empty(self):
        return len(self.items) == 0