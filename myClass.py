class testClass:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

def Main():
    ex1 = testClass("First", 1111111111)
    print(ex1.name)
    print(ex1.phone)

if __name__ == '__main__':
    Main()
     
