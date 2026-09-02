import json
from library_item import LibraryItem


class Database:

    def __init__(self, filename="database.txt"):
        self.filename = filename

    def save(self, items):

        with open(self.filename, "w") as file:

            for item in items:

                data = {
                    "type": item.__class__.__name__,
                    "title": item.title,
                    "status": item._status.value
                }

                file.write(json.dumps(data) + "\n")

    def load(self):

        items = []

        with open(self.filename, "r") as file:

            for line in file:

                data = json.loads(line)

                item = LibraryItem.from_dict(data)

                items.append(item)

        return items