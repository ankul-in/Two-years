#kata
#https://www.codewars.com/kata/586e6d4cb98de09e3800014f/train/python

class VendingMachine:
    items = [
        {'name': "Smarties", 'code': "A01", 'quantity': 10, 'price': 0.60},
        {'name': "Caramac Bar", 'code': "A02", 'quantity': 5, 'price': 0.60},
        {'name': "Dairy Milk", 'code': "A03", 'quantity': 1, 'price': 0.65},
        {'name': "Freddo", 'code': "A04", 'quantity': 1, 'price': 0.25}
    ]

    def __init__(self, items=None, money=0):
        self.items = items if items else VendingMachine.items.copy()
        self.money = money

    def vend(self, selection, item_money):
        item = next((item for item in self.items if item['code'] == selection), None)
        if not item:
            return f"Invalid selection! :Money in vending machine = {self.money:.2f}"

        if item['quantity'] <= 0:
            return f"{item['name']}: Out of stock!"

        change = round(item_money - item['price'], 2)

        if change < 0:
            return "Not enough money!"
        else:
            item['quantity'] -= 1
            if change == 0:
                return f"Vending {item['name']}"
            else:
                return f"Vending {item['name']} with {change:.2f} change."
            

#'Invalid selection! :Money in vending machine = 10.00' should equal 'Invalid selection! : Money in vending machine = 11.20'