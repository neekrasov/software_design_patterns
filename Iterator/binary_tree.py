class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)

    def __str__(self) -> str:
        return f"Node: {self.value}"


class InOrderIterator:  # with state
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False
        while self.current.left:
            self.current = self.current.left

    def __iter__(self):
        return self

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current

        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            return self.current


def traverse_in_order(node):  # without state
    if node.left:
        yield from traverse_in_order(node.left)
    yield node
    if node.right:
        yield from traverse_in_order(node.right)


if __name__ == "__main__":
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    it = iter(root)
    print([next(it).value for _ in range(7)])
