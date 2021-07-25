'''
Turn the shopping cart program from yesterday into an object-oriented program.
Create a class called cart that retains items and has methods to add, remove, and show.
'''

class Cart():
    def __init__(self, my_dict = {}):
        self.my_dict = my_dict

    def addGrocery(self, grocery):
        grocery = grocery.title()
        if grocery in self.my_dict:
            self.my_dict[grocery] += 1
        else:
            self.my_dict[grocery] = 1
        print(f'You just added "{grocery}" into your car!')
        print(f'Your shopping car consists of {self.my_dict}')

    def removeGrocery(self, grocery):
        grocery = grocery.title()
        if (grocery in self.my_dict) and (self.my_dict[grocery] > 1):
            self.my_dict[grocery] -= 1
        else:
            del self.my_dict[grocery]
        print(f'You just removed a(n) "{grocery}" from your cart!')
        print(f'Your shopping car consists of {self.my_dict}')

    def showGrocery(self):
        print(f'Your shopping cart consists of {self.my_dict}')

my_cart = Cart()
my_cart.addGrocery('apple')
my_cart.addGrocery('apple')
my_cart.addGrocery('BaNAnA')
my_cart.removeGrocery('APPLE')
my_cart.removeGrocery('APPLE')







'''
Write a Python class which has two methods get_String and print_String. get_String accepts
a string from the user and print_String print the string in upper case.
'''

class StringMagic():
    def __init__(self, input_string):
        self.input_string = input_string

    def get_String(self):
        return self.input_string

    def print_String(self):
        print(self.input_string.upper())

text = StringMagic('test test')
print(text.get_String())
text.print_String()