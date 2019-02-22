class SuperC:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def SupAbMethod(self):
        raise NotImplementedError("Abstract method - not implemented in Super class")

class subC(SuperC):
    def __init__(self, name, phone, pin):
        super().__init__(name, phone)
        self.pin = pin
    def SupAbMethod(self):
        return print("Implemented in Sub Class")

def Main():
    
    pdirs=[subC("First", 1, 201301), subC("Second", 2, 201301), subC("Third", 3, 201301)]
    for pdir in pdirs:
        print("Name " +pdir.name +", Phone "+ str(pdir.phone) +", PIN "+str(pdir.pin))

if __name__ == '__main__':
    Main()