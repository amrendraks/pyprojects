import argparse
class ArgClass:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
    nums = parser.parse_args()
    print(nums.accumulate(nums.integers))

if __name__ == '__main__':
    Main()
