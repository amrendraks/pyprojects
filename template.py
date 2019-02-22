from string import Template
def Main():
    data = []
    data.append(dict(name="example1", phone=11111111111))
    data.append(dict(name="example2", phone=22222222222))

    temp = Template("My name is $name and phone number is $phone")

    for row in data:
        print(temp.substitute(row))

if __name__ == '__main__':
    Main()