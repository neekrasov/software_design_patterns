import abc


class Machine(abc.ABC):
    @abc.abstractmethod
    def print(self, document):
        raise NotImplementedError

    @abc.abstractmethod
    def fax(self, document):
        raise NotImplementedError

    @abc.abstractmethod
    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):  # <-- this is wrong (but it's not detected)
        """Not Supported"""
        pass
