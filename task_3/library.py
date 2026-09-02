class Library:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def checkout(self, title):
        item = self.find_by_title(title)

        if item is None:
            return False

        return item.checkout()

    def return_item(self, title):
        item = self.find_by_title(title)

        if item is None:
            return False

        return item.return_item()

    def find_by_title(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item

        return None

    def list_available(self):
        available = []

        for item in self.items:
            if item._status.name == "AVAILABLE":
                available.append(item)

        return available

    def list_all(self):
        return self.items