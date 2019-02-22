import argparse

def add(num1, num2):
    return(num1 + num2)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-num1', help="Enter two number", type=int)
    parser.add_argument('-num2', help="Enter two number", type=int)
    args = parser.parse_args()
    res = add(args.num1, args.num2)

    print("Sum of both numbers are :"+ res)

if __name__ == '__main__':
    Main()

