# Combining builders via interface


class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    @staticmethod
    def create(name):  # violation of the OCP (open-closed principle)
        return HtmlBuilder(name)

    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.__str(0)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=self.root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(name=child_name, text=child_text))
        return self

    def __str__(self):
        return str(self.__root)


if __name__ == "__main__":
    element = (
        HtmlElement()
            .create("ul")
            .add_child("li", "hello")
            .add_child("li", "world")
    )

    builder = (
        HtmlBuilder("ul")
            .add_child("li", "hello")
            .add_child("li", "world")
    )

    print("With element: \n", element)
    print("\nWith builder: \n", builder)
