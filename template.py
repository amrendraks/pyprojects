from string import Template

def Main():
    data = []
    data.append(dict(item = "coke", qty = 2, price = 10))
    data.append(dict(item = "chew", qty = 5, price = 5))

    temp = Template("Total price of $item = $qty x $price")

    for tlist in data:
        print temp.substitute(tlist)

if __name__ == '__main__': 
    Main()