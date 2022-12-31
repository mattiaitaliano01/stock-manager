# import tabulate after installed it
from tabulate import tabulate

#========The beginning of the class==========
# defining the Shoe class
class Shoe:

    # initialise all the parameters
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # returns the cost of the shoe
    def get_cost(self):
        return self.cost
        
    # returns the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # returns the string representation of the class    
    def __str__(self):
        return f"{self.country} - {self.code} - {self.product} - {self.cost} - {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    # open the file inventory.txt and read the data
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                data = line.split(",")
                # create a object for each line by split the parameters
                shoe = Shoe(data[0], data[1], data[2], data[3], data[4].strip("\n"))
                # append the object to the list
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("\nFile not found")

# allow a user to capture data
# about a shoe and use this data to create a shoe object
def capture_shoes():
    # get data from user
    print("\nAdd a new shoe to the list:")
    country = input("\nEnter a Country: ").lower().capitalize()
    code = input("Enter a Code: ") .upper()
    product = input("Enter a Product: ").lower().capitalize()
    # loop until they don't enter an int
    while True:
        try:
            cost = int(input("Enter a Cost: ").lower().capitalize())
            quantity = int(input("Enter a Quantity: ").lower().capitalize())
            break
        except ValueError:
            print("\nInvalid Input. Enter a proper number!\n")
    # setup an object
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    with open("inventory.txt", "w") as file:
        # add an empty text variable
        document = ""
        for shoe in shoe_list:
            data = shoe.__str__().split(" - ")
            string = ",".join(data)
            # add each loop a new line on the text to write
            document += f"{string}\n"
        file.write(document)
        print(f"\nAdded the following element:\n")
        shoe_added = [shoe_list[0].__str__().split(" - "), data]
        # display in a grid
        print(tabulate(shoe_added, headers="firstrow", tablefmt="grid"))

def view_all():
    # create a list that contain data
    shoe_view = []
    # loop into the list and split the str data
    for shoe in shoe_list:
        data = shoe.__str__().split(" - ")
        shoe_view.append(data)
    print("\n")
    # display list thanks to tabulate module
    print(tabulate(shoe_view, headers="firstrow", tablefmt="grid"))

# find the lowest quantity object and give the opportunity
# to add quantity in stock
def re_stock():
    # initialize a variable with hight value
    stock = 999999999
    # loop into the shoe_list to calculate the lesser quantity
    for count, shoe in enumerate(shoe_list):
        # do not consider the first row
        if count > 0:
            if stock >= int(shoe.quantity):
                stock = int(shoe.quantity)
                element = shoe
    # get the user's choice            
    choice = input(f"\nThe {element.product} has {stock} unit left. Do you want to re-stock it (Y/N)? ").lower().strip()
    if choice == 'y':
        # loop until new_quantity isn't int
        while True:
            try:
                new_quantity = int(input("\nHow many units do you want to add? "))
                # add the new value to the previous
                stock += new_quantity
                element.quantity = stock
                break
            except ValueError:
                print("\nEnter a valid digit!")
        # open the inventory text file and re-write it
        with open("inventory.txt", "w") as file:
            # add an empty text variable
            document = ""
            for shoe in shoe_list:
                data = shoe.__str__().split(" - ")
                string = ",".join(data)
                # add each loop a new line on the text to write
                document += f"{string}\n"
            file.write(document)
        print(f"\nAdded {new_quantity} to the stock, now {element.product} has a total of {stock} units left.")
    else:
        print("\nYou didn't add any units to the stock.")

# search for a shoe from the list
# using the shoe code
def search_shoe():
    # get choice from user
    choice = input("\nEnter the Code of the product you're looking for: ").upper()
    element = None
    # loop within the shoe list and check if 
    # the code correspond to the choice
    for shoe in shoe_list:
        data = shoe.__str__().split(" - ")
        if data[1] == choice:
            element = shoe
    if element == None:
        print(f"\nThere is no {choice}.")
    else:
        print("\n")
        id_picked = [shoe_list[0].__str__().split(" - "), element.__str__().split(" - ")]
        # display in a grid
        print(tabulate(id_picked, headers="firstrow", tablefmt="grid"))

def value_per_item():
    # initialize the headers and the table itself
    worth_stock = [["Product", "Code", "Cost", "Quantity", "Total Value"]]
    # loop into the showlist
    for count, shoe in enumerate(shoe_list):
        # exclude the first row
        if count > 0:
            data = shoe.__str__().split(" - ")
            # construct the table to display and multiply values
            shoe_data = [data[2], data[1], data[3], data[4], int(data[3])*int(data[4])]
            worth_stock.append(shoe_data)
    # display in a grid
    print(tabulate(worth_stock, headers="firstrow", tablefmt="grid"))


def highest_qty():
    # initialize the check's variable
    stock = -1
    # loop into the shoe_list to calculate the higher quantity
    for count, shoe in enumerate(shoe_list):
        # do not consider the first row
        if count > 0:
            # assign each loop the element to the greatest item's quantity
            if stock <= int(shoe.quantity):
                stock = int(shoe.quantity)
                element = shoe
    # display the result and put on sale
    print(f"\n{element.product} (Code: {element.code}) will be on Sale. Unit available: {element.quantity}")

#==========Main Menu=============
print("Welcome in the inventory!")
read_shoes_data()
# loop until end
while True:
    selection = input(f"""

Enter the following to make your choice:

a  - Add new shoe to the stock's list
va - View the table of all the stock
rs - View the lowest quantity and add more pieces
s  - Search for ID
v  - Display total value
h  - Display highest quantity and put on sale
e  - Exit the program
: """).strip().lower()

    if selection == 'a':
        capture_shoes()
    elif selection == "va":
        view_all()
    elif selection == "rs":
        re_stock()
    elif selection == 's':
        search_shoe()
    elif selection == 'v':
        value_per_item()
    elif selection == 'h':
        highest_qty()
    elif selection == 'e':
        print("\nSee you soon!")
        break
    else:
        print("\nInvalid Input!\nTry Again.")