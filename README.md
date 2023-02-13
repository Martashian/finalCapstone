# finalCapstone
HyperionDev Capstone Project IV - OOP

A stock-taking and inventory management program for Nike warehouses that reads a text file and allows the user to perform a range of functions on 'Shoe' objects generated from the file.

Menu
The following menu is shown to the user:

    r - Read data and save it to inventory list
    a - Add a new product to the inventory list
    va - View all products in the inventory list
    rs - Restock the lowest quantity shoe in the inventory list
    s - Search shoe using a shoe code
    v - Calculate the total value for each item
    h - Select the highest quantity shoe and put it on sale
    e - Exit program

Functions

Read data
If the user selects 'r', the data from the inventory.txt file is read and iterated through to make a list of shoe objects.

Capture shoes
If the user selects 'a', allows the user to capture data about a shoe and creates a new shoe object that is added to the inventory list and txt file. The user is asked for the following data:
Country
Product Code 
Product Name
Cost
Quantity


View all
If the user selects 'va', the shoes list is iterated through and printed as a tabulate table for ease of reading.

Restock
If the user selects 'rs', allows the user to increase the amount of stock of the lowest quantity shoe by a certain amount.

Search
If the user selects 's', allows the user to search for a shoe by its product code.

Value Per Shoe
If the user selects 'v', allows the user to see the value per shoe, calculated by the following:
Cost * quantity

Highest quantity shoe
If the user selects 'h', displays a message saying the shoes are on sale.

Exit
If the user selects 'e', exits the program.
