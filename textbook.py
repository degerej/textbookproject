from person import Person


class Textbook:
    def __init__(self,title1, first, last, age,  isbn_number, qty_in_inventory, price, publisher, year_published):
        self.title = title1
        self.author = Person(first, last, age)
        self.ISBN = isbn_number
        self.quantity = qty_in_inventory
        self.price = price
        self.publisher = publisher
        self.year = year_published

    def add_inventory(self, qty):
        self.quantity = self.quantity + qty

    def deducting_inventory(self, qty):
        if self.quantity >= qty:
            self.quantity = self.quantity - qty
            return
