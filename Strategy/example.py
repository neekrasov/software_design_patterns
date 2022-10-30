from abc import ABC


class ListStrategy(ABC):
    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    def add_list_item(self, buffer, item):
        pass


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f" * {item}")


class HTMLListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append("<ul>")

    def end(self, buffer):
        buffer.append("</ul>")

    def add_list_item(self, buffer, item):
        buffer.append(f"  <li>{item}</li>")


class OutputFormat:
    MARKDOWN = 1
    HTML = 2


class TextProcessor:
    def __init__(self, list_strategy=HTMLListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        ls = self.list_strategy
        ls.start(self.buffer)
        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    def set_output_format(self, list_strategy):
        if list_strategy == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif list_strategy == OutputFormat.HTML:
            self.list_strategy = HTMLListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "\n".join(self.buffer)


if __name__ == "__main__":
    test = ["foo", "bar", "baz"]
    tp = TextProcessor()
    tp.append_list(test)
    print(tp)

    tp.clear()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(test)

    print(tp)
