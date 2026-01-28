class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError
    
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    def fax(self, document):
        pass

    def scan(self,document):
        pass

# Old fashioned printer will not have fax or scan 
# as can do "PASS" but when someone tries to use FAX or SCAN its wont do anything that is confusing
# we can so raise NotImplementedError - This will be ok where application is small where code can be looked at
# but for large application it is a problem
# so instead of having a big interfae break it into small pieces
class OldFashionedPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

#------------------------- SOLUTION----------------------

class Printer:
    @abstractmethod
    def print(self,document):
        pass

class Scanner:
    @abstractmethod
    def scan(self,document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        pass
    def scan(self, document):
        pass

class MultiFunctionDevice(Printer,Scanner):
    @abstractmethod
    def print(self, document):
        pass
    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __inti__(self,printer,scanner):
        self.scanner = scanner
        self.printer = printer
    def print(self, document):
        self.printer.print(document)
    def scan(self, document):
        self.scanner.scan(document)