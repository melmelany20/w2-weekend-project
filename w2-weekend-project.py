# Shopping Cart Example Below

# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    
    def __init__ (self):
        self.items = {}
        
    def show_items(self):
        print(self.items)
        
    def delete_item(self, item, quantity):
        self.items[item]['quantity'] = int(self.items[item]['quantity']) - int(quantity)
        
    def add_item_new(self, item, price, quantity):
        self.items[item] = {
            'price': price,
            'quantity': quantity
        }
    
    def add_item_existing(self, item, quantity):
        self.items[item]['quantity'] = int(self.items[item]['quantity'] + quantity)
        

cart1 = Cart()


def get_user_input():
    confirm = input("Do you want to: [S]how / [A]dd / [D]elete / [Q]uit?")
    return confirm

def add_cart(shopping_cart, item):
    if item == 'R' or item == 'r':
        pass
    elif item not in cart1.items:
        while True:
            try:
                price = float(input("How much does this item cost? Please enter to 2 decimal points. Ex: 10.00, 4.99 "))
                break
            except:
                print("Please enter price to two decimal points. Ex: 10.99 or 5.00")
        quantity = int(input("How many are you adding?: "))
        cart1.add_item_new(item, price, quantity)
        cart1.show_items()
    elif item in cart1.items:
        quantity = int(input("How many are you adding?: "))
        cart1.add_item_existing(item, quantity)
        cart1.show_items()
    
def del_from_cart(shopping_cart, item):
    if item == 'R' or item == 'r':
        pass
    elif item in cart1.items:
        quantity = input("How many do you want to remove?")
        if int(quantity) > int(cart1.items[item]['quantity']):
            print("Invalid quantity - exceeds number in shopping cart.")
            cart1.show_items()
        elif int(quantity) <= int(cart1.items[item]['quantity']):
            cart1.delete_item(item, quantity)
            cart1.show_items()
    else:
        print("Item not in cart")
        cart1.show_items()
        
def driver():
    print("Welcome to your shopping cart. What would you like to do?")
    while True:
        user_input = get_user_input()
        if user_input == 'D' or user_input == 'd':
            user_delete_option = input("What item are you deleting? Or type [R] to return to main menu. ")
            del_from_cart(cart1.items, user_delete_option)
        elif user_input == 'A' or user_input == 'a':
            user_add_option = input("What item are you adding? Or type [R] to return to main menu. ")
            add_cart(cart1.items, user_add_option)
        elif user_input == 'S' or user_input == 's':
            cart1.show_items()
        elif user_input == 'Q' or user_input == 'q':
            break
        else:
            print("Enter a valid option.")
        
driver()