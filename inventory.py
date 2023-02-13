
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity


    # Returns a string representation of a class
    def __str__(self):
        return f'In {self.country}, {self.code} {self.product} costs {self.cost}. We have {self.quantity} in stock.'


# Empty list that will be used to store a list of shoes objects
shoe_list = []

# This function opens file intentory.txt and reads data to then create a shoes object and append it into the shoes list
# Creating an object and appending it to the shoe_list. 
# Uses try and except to handle errors.
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                shoe = line.replace("\n", "").split(",")
                try:
                    shoe = Shoe(shoe[0], shoe[1], shoe[2], shoe[3], shoe[4])
                    shoe_list.append(shoe)
                except IndexError:
                    print("An error occurred. Please make sure the information is accurate. ")
                    quit()
    except FileNotFoundError:
        print("File not found. Please try again. ")
        quit() 


# This function allows the user to capture data about a shoe and use this data to create a shoe object and append this object to the shoe list
# Adds the new shoe object to the inventory text file
def capture_shoes():
    new_country = input("Enter the country this product is stocked in: ")
    new_code = input("Enter the product's code: ")
    new_product = input("Enter the name of the product: ")
    new_cost = float(input("Enter the cost of the product: "))
    new_quantity = int(input("Enter the quantity in stock: "))

    shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)

    with open("inventory.txt", "a") as file:
        file.writelines(f"\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}")
    
    shoe_list.append(shoe)
    print("Product has been added. ")



def view_all():
    read_shoes_data()
    shoes = []
    for shoe in shoe_list:
        shoes.append(shoe.__dict__)
    
    print(shoes)

# This function will finde the shoe object with the lowest quantity and ask the user if they want to add this quantity of shoes and then update it. It also updates the file for this shoe
def re_stock():
    shoe_quantity = []
    for shoe in shoe_list:
        shoe_quantity.append(shoe.get_quantity())
    lowest_stock_quantity = min(shoe_quantity)
    for shoe in shoe_list:
        if lowest_stock_quantity == shoe.quantity:
            global lowest_stock_index
            lowest_stock_index = shoe_list.index(shoe)
    # Stores the product with the lowest quantity to a global variable
    global lowest_quantity_product
    lowest_quantity_product = shoe_list[lowest_stock_index]

    print(f"{lowest_quantity_product.product} has the least stock \
({lowest_quantity_product.quantity}). Would you like to restock it? (y/n)")
    restock_response = input("Enter your selection here: ").lower()\
        .replace(" ", "")
    if restock_response == "y" or restock_response == "yes":
        while True:
            try:
                restock_amount = int(input("Please enter the amount you \
would like to restock:"))
                new_stock = (lowest_quantity_product.quantity + restock_amount)
                shoes_data_string = ""
                with open("inventory.txt", "r") as shoes_data:
                    for line in shoes_data:
                        shoes_data_string += line
                    shoes_data_string = shoes_data_string.split("\n")
                    restocked_shoe = shoes_data_string[lowest_stock_index + 1]
                    restocked_shoe = restocked_shoe.split(",")
                    restocked_shoe[4] = str(new_stock)
                    restocked_shoe = ",".join(restocked_shoe)
                    shoes_data_string[lowest_stock_index + 1] = restocked_shoe
                    shoes_data_string = "\n".join(shoes_data_string)
                with open("inventory.txt", "w") as shoes_data:
                    shoes_data.writelines(shoes_data_string)
                print(f"{lowest_quantity_product.product} has been \
successfully restocked. New stock is {new_stock}. ")
            except ValueError:
                print("You can only enter an integer. Please try again.")
                continue
            else:
                break
    elif restock_response == "n" or restock_response == "no":
        print("Returning to menu...")
    else:
        print("Response not recognised. Please try again.")

# This function searches for a shoe from the list using the shoe code and returns this object so that it will be printed
def search_shoe():
    searched_shoe = None
    shoe_search = input("Please enter the product code of the shoe \
you would like to search: ").upper().replace(" ", "")
    for shoe in shoe_list:
        if shoe.code == shoe_search:
            searched_shoe = shoe
    if searched_shoe is None:
        print(f"Sorry, a shoe with the product code {shoe_search} could \
not be found. Please try again. ")
        search_shoe()
    else:
        print(searched_shoe)

# This function calculates the total value for each item
def value_per_item():
    for shoe in shoe_list:
        value_shoe = shoe.get_cost() * shoe.get_quantity()
        shoe.value_per_item = value_shoe
        shoes_dict_list = []
        for shoe in shoe_list:
            shoes_dict_list.append(shoe.__dict__)

        print(shoes_dict_list)


# This function determines the product with the highest quantity and prints the shoe as being for sale
def highest_qty():
    shoe_quantity = []
    for shoe in shoe_list:
        shoe_quantity.append(shoe.get_quantity())
    highest_stock_quantity = max(shoe_quantity)
    for shoe in shoe_list:
        if highest_stock_quantity == shoe.quantity:
            global highest_stock_index
            highest_stock_index = shoe_list.index(shoe)

    global highest_quantity_product
    highest_quantity_product = shoe_list[highest_stock_index]

    print(f"{highest_stock_index.product} is currently on sale for a limited time only! ")



# This function displays a menu that executes the functions above depending on user choice
def menu():
    print("Nike warehouse inventory management program. ")
    menu = ""
    while menu != "e":
        read_shoes_data()
        print("-" * 44)
        
        menu = input('''Please select one of the following:

    r - Read data and save it to inventory list
    a - Add a new product to the inventory list
    va - View all products in the inventory list
    rs - Restock the lowest quantity shoe in the inventory list
    s - Search shoe using a shoe code
    v - Calculate the total value for each item
    h - Select the highest quantity shoe and put it on sale
    e - Exit program
    
    ''').lower()

        if menu == "r":
            read_shoes_data()
        elif menu == "a":
            capture_shoes()
        elif menu == "va":
            view_all()
        elif menu == "rs":
            re_stock()
        elif menu == "s":
            search_shoe()
        elif menu == "v":
            value_per_item()
        elif menu == "h":
            highest_qty()
        elif menu == "e":
            print("You exited the program successsfully. Goodbye! ")
            quit()
        else: 
            print("Wrong choice. Please try again. ")
            continue
        

menu()