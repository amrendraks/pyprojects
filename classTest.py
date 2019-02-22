class testClass:
    def __init__ (self, name, phone):
      self.name = name
      self.phone = phone

def Main():
    ex1 = testClass("selfInitialized", 1)
    #ex1.name = "Example 1"
    #ex1.phone = 11111111
    print ex1.name
    print ex1.phone

    #ex2 = testClass()
    #ex2.name = "Example 2"
    #ex2.phone = 222222222
    #print ex2.name
    #print ex2.phone

    
if __name__ == '__main__':
    Main()
