from library_item import Book, DVD, Magazine
from library import Library
from database import Database


library = Library()

book = Book("Dune")
dvd = DVD("The Matrix")
magazine = Magazine("National Geographic")

library.add_item(book)
library.add_item(dvd)
library.add_item(magazine)


# Checkout
library.checkout("Dune")


# Print items
for item in library.list_all():
    print(item)


# Sort alphabetically
items = sorted(library.list_all())

print("\nSorted:")
for item in items:
    print(item)


# Save
database = Database()
database.save(library.list_all())


# Load
loaded_items = database.load()

print("\nLoaded:")
for item in loaded_items:
    print(item)