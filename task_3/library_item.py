from enum import Enum


class ItemStatus(Enum):
    AVAILABLE = "Available"
    CHECKED_OUT = "Checked Out"
    LOST = "Lost"


class LibraryItem:
    # Used to create the correct subclass from a dictionary
    item_types = {}

    def __init__(self, title):
        self.title = title
        self._status = ItemStatus.AVAILABLE

    # ---------- Status methods ----------

    def checkout(self):
        if self._status != ItemStatus.AVAILABLE:
            return False

        self._status = ItemStatus.CHECKED_OUT
        return True

    def return_item(self):
        if self._status != ItemStatus.CHECKED_OUT:
            return False

        self._status = ItemStatus.AVAILABLE
        return True

    def mark_lost(self):
        if self._status == ItemStatus.LOST:
            return False

        self._status = ItemStatus.LOST
        return True

    # ---------- Loan period ----------

    def loan_period(self):
        raise NotImplementedError

    # ---------- Sorting ----------

    def __lt__(self, other):
        return self.title.lower() < other.title.lower()

    # ---------- Printing ----------

    def __str__(self):
        return f"{self.title} ({self.__class__.__name__}) — {self._status.value}"

    def __repr__(self):
        return f"{self.__class__.__name__}(title='{self.title}', status='{self._status.name}')"

    # ---------- Dictionary constructor ----------

    @classmethod
    def from_dict(cls, data):
        item_type = data["type"]

        item_class = cls.item_types[item_type]

        item = item_class(data["title"])

        item._status = ItemStatus(data["status"])

        return item

    # ---------- ISBN validation ----------

    @staticmethod
    def valid_isbn(isbn):
        """
        Checks ISBN-13.
        Returns True if the ISBN is valid.
        """

        isbn = isbn.replace("-", "").replace(" ", "")

        if len(isbn) != 13:
            return False

        if not isbn.isdigit():
            return False

        total = 0

        for i in range(12):
            if i % 2 == 0:
                total += int(isbn[i])
            else:
                total += int(isbn[i]) * 3

        check_digit = (10 - (total % 10)) % 10

        return check_digit == int(isbn[12])


class Book(LibraryItem):

    def loan_period(self):
        return 21


class DVD(LibraryItem):

    def loan_period(self):
        return 5


class Magazine(LibraryItem):

    def loan_period(self):
        return 14


# Register the item types
LibraryItem.item_types = {
    "Book": Book,
    "DVD": DVD,
    "Magazine": Magazine
}