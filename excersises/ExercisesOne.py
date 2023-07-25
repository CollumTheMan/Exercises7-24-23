class Cart:
    def __init__(self):
    
       self.shopping_cart = {}
    def add_item(self, item, quantity, price):
        if item in self.shopping_cart:
            self.shopping_cart[item]["quantity"]+=quantity
        else:
            self.shopping_cart[item]={
                "quantity": quantity,
                "price":price
            }
    def delete_item(self, item):
        if item in self.shopping_cart:
            del self.shopping_cart[item]
    def show_items(self):
        print(self.shopping_cart)
    def checkout(self):
        total=0
        self.show_items()
        for k,v in self.shopping_cart.items():
            total+= v["quantity"]*v["price"]
        print("total is: " + str(total))
cart = Cart()
while True:
    action = input("what do you want to do? (buy/checkout/delete)")
    if action == "buy":

        item = input("What would you like to purchase?")
        quantity = int(input("quantity?"))
        price = int(input("price?"))
        cart.add_item(item, quantity, price)
        cart.show_items()
    elif action == "checkout":
        cart.checkout()
        break
    elif action == "delete":
        item = input("What would you like to delete?")
        cart.delete_item(item)
        cart.show_items()
    else:
        continue