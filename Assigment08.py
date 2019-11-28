# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KBosworth,11/25/2019,Created Product object
# KBosworth,11/27/2019,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
import sys # include to check to see if file exists or not

class Product(object):
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    # --Fields--
    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price
    # -- Properties --
    # ProductName
    @property  # DON'T USE NAME for this directive!
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # ProductPrice
    @property  # DON'T USE NAME for this directive!
    def product_price(self):  # (getter or accessor)
        return str(self.__product_price)

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value):  # (setter or mutator)
        self.__product_price = value
    # -- Methods --
    def to_string(self):
        return self.self.__str__()

    def __str__(self):
        return self.product_name + ', $' + self.product_price

# End of class
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        ReadFileDataToList(file_name, list_of_rows): -> (a list of product objects)
        WriteListDataToFile(file_name, list_of_rows)
        AddEntry(value1, value2, lstOfProductObjects):
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kbosworth,11/25/2019,Created Class
        KBosworth,11/27/2019,Modified code to complete assignment 8
    """
    def ReadFileDataToList(file_name, list_of_rows):
        """
            Desc - Reads data from a file into a list of dictionary rows
            :param file_name: (string) with name of file:
            :param list_of_rows: (list) you want filled with file data:
            :return: lstOfProductObjects (list) of dictionary rows
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Product": data[0].strip(), "Price": data[1].strip()}
            lstOfProductObjects.append(row)
        file.close()
        return lstOfProductObjects

    @staticmethod
    def WriteListDataToFile(file_name, list_of_rows):
        """
        Desc - Writes data from a list into a file
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want to use data from:
        :return: nothing
        """
        objFile = open(strFileName, "w")
        for dicRow in lstOfProductObjects:  # Write each row of data to the file
            objFile.write(dicRow["Product"] + "," + dicRow["Price"] + "\n")
        objFile.close()

    @staticmethod
    def AddEntry(value1, value2, lstOfProductObjects):
        """
        Desc - Adds an item input by the user into the table
        :param value1: (string) the new product:
        :param value2: (string) the new price:
        :param lstOfProductObjects: (list) list that was added to:
        :return: lstOfProductObjects (list) of dictionary rows
        """
        dicRow = {"Product": value1, "Price": value2}  # Create a new dictionary row
        lstOfProductObjects.append(dicRow)  # Add the new row to the list/table
        IO.ShowCurrentItemsInList(lstOfProductObjects)
        FileProcessor.WriteListDataToFile(strFileName, lstOfProductObjects)
        return (lstOfProductObjects)
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Accepts inputs from user to populate or manipulate a list of products:
    methods:
        OutputMenuItems():
        InputMenuChoice():
        ShowCurrentItemsInList(list_of_rows):
        EnterNewEntry():
    changelog: (When,Who,What)
        Kbosworth,11/25/2019,Created Class
        Kbosworth,11/27/2019,Modified code to complete assignment 8
    """
    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current items products are: *******")
        for row in list_of_rows:
            print(row["Product"] + "," + row["Price"])
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def EnterNewEntry():
        """ Receives new product and product from user
        :return: strings
        """
        strProduct = str(input("What is the product? - ")).strip()  # Get product from user
        strPrice = str(input("What is the Price? ex. X.XX - ")).strip() # Get product1 from user
        if strPrice.isnumeric() == True:
            print("Please input a number for the price.") ### this isn't working. fix.....
            print()  # Add an extra line for looks
            print()  # Add an extra line for looks
        return strProduct,strPrice
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
try:
    FileProcessor.ReadFileDataToList(strFileName, lstOfProductObjects)  # read file data
except:
    print("No file found or error reading the file.")
    sys.exit(1) # if no file is found, exit program

# Show user a menu of options
while(True):
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Get user's menu option choice
    # Show user current data in the list of product objects
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        continue  # to show the menu

    # Let user add data to the list of product objects
    elif(strChoice.strip() == '2'):
        product, price = IO.EnterNewEntry()
        objP1 = Product(product,price)
        print("This product will be added to the file: ", objP1)
        FileProcessor.AddEntry(objP1.product_name, str("$" + objP1.product_price), lstOfProductObjects)
        continue  # to show the menu

    # Exit the program
    elif (strChoice == '3'):
        break   # and Exit

    else: # need a catch all
        print("That option is not valid. Please select 1-3")
        continue
# Main Body of Script  ---------------------------------------------------- #