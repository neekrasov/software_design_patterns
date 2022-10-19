# Возможно появление других типов, которые нужно будет сохранять в файл
# Нарушение принципа единственной ответственности


class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def save(
        self, filename
    ):  # wrong, this is not the responsibility of the Journal class
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(
        self, filename
    ):  # wrong, this is not the responsibility of the Journal class
        pass

    def low_from_web(
        self, uri
    ):  # wrong, this is not the responsibility of the Journal class
        pass

    def __str__(self):
        return "\n".join(self.entries)


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")

print(f"Journal entries:\n{j}")
