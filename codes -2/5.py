from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class AllInOneMachine(Printer, Scanner):
    def print_document(self):
        return "Printing document!"

    def scan_document(self):
        return "Scanning document!"

class SimplePrinter(Printer):
    def print_document(self):
        return "Printing document only!"

machine = AllInOneMachine()
print(machine.print_document())
print(machine.scan_document())

printer = SimplePrinter()
print(printer.print_document())