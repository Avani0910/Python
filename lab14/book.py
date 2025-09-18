class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        """Display the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
        print("-" * 30)

    def apply_discount(self, discount_percent):
        """Apply a discount to the price of the book."""
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount


# Example usage
if __name__ == "__main__":
    # (a) Create two book objects
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 20.00)
    book2 = Book("1984", "George Orwell", 15.00)

    print("Initial Book Details:")
    book1.display_details()
    book2.display_details()

    # (b) Apply 10% discount to one of the books
    print("After Applying 10% Discount to Book 2:")
    book2.apply_discount(10)
    book2.display_details()
