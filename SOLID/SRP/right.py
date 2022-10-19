class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    j = Journal()

    j.add_entry("I cried today.")
    j.add_entry("I ate a bug.")

    PersistenceManager.save_to_file(j, "SOLID/SRP/some_folder/journal.txt")
