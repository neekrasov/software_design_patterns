import abc

# Создание интерфейсов, содержащих много программный членов, не лучшая идея.
# Иначе придётся инициализировать методы, которые могут не понадобиться.


class Printer(abc.ABC):

    abc.abstractclassmethod

    def print(self, document):
        raise NotImplementedError


class Scanner(abc.ABC):

    abc.abstractclassmethod

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionDevice(Printer, Scanner):
    @abc.abstractclassmethod
    def print(self, document):
        pass

    @abc.abstractclassmethod
    def scan(self, document):
        pass


class MultiFunctionalMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner) -> None:
        self._scanner = scanner
        self._printer = printer

    def print(self, document):
        self._scanner.scan(document)

    def scan(self, document):
        self._printer.print(document)
