class Order:
    def __init__(self, fio, workplace, product, price, quantity):
        self.fio = fio
        self.workplace = workplace
        self.product = product
        self.price = float(price)
        self.quantity = int(quantity)

class OrderManager:
    def __init__(self):
        self.orders = {}
        self.count = 0
    
    def read_from_file(self, filename):
        self.orders = {}
        self.count = 0
        with open(filename, 'r', encoding='utf8') as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(', ')
                    if len(parts) == 5:
                        self.orders[self.count] = Order(*parts)
                        self.count += 1
    
    def update_file(self, filename, new_data):
        with open(filename, 'w', encoding='utf8') as file:
            for line in new_data:
                file.write(line + '\n')
        self.read_from_file(filename)
    
    def append_to_file(self, filename, new_data):
        with open(filename, 'a', encoding='utf8') as file:
            for line in new_data:
                file.write(line + '\n')
        self.read_from_file(filename)