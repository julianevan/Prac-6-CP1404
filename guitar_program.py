from guitars import Guitar
def main():
    Guitar_list = []
    print("My Guitars!")
    name = str(input("Name:"))
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Price:"))
        new_guitar = Guitar(name, year, cost)
        print("{} ({}) : ${} added".format(name, year, cost))
        Guitar_list.append(new_guitar)
        name = str(input("Name:"))
    else:
        for i, guitar in enumerate(Guitar_list):
            is_vintage_text = ""
            if guitar.is_vintage():
                is_vintage_text = "(vintage)"
            print("Guitar {0}: {1:>30} ({2}), worth ${3:10,.2f}{4}".format(i + 1, guitar.name, guitar.year, guitar.cost, is_vintage_text))
main()