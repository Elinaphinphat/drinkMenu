class Order:
    def __init__(self):
        self.__items = [] 
# __init__ is used as a constructor which creates an empty order object.

# -------------
    def add_item(self, drink):
        self.__items.append(drink) # This is used to add drinks into the Order.

    def get_items(self):
        return self.__items # This will return the list of drinks in the order.
# -------------

    def get_total(self):
        total = sum(drink.price for drink in self.__items)
        return total
    # This will calculate and sum up the drink prices.

    def get_num_items(self):
        num_items = len(self.__items)
        return f"Item Total: {num_items}"
    # This will return the total number of drinks in the receipt.

    def get_receipt(self):
        receipt = "\n".join([str(item) for item in self.__items])
        return f"Receipt:\n{receipt}\nTotal: ${self.get_total():.2f}"
    # Returns a receipt in a specific formatted order into the console.

    def remove_item(Self, index):
        if 0 <= index < len(self.__items):
            self.__items.pop(index)
    # Removes items from the order using index.

    def __str__(self):
        return f'Order(items={self.__items})'
    # Returns a list of all items.