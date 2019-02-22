def genfun(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

def Main():
    gen = genfun('hello')
    for char in gen:
        print(char)
    data = 'hello'
    print(list(data[i] for i in range(len(data)-1, -1, -1)))

if __name__ == '__main__':
    Main()
