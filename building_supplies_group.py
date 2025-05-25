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
        orders_list = []
        
        with open(filename, 'r', encoding='utf8') as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(', ')
                    if len(parts) == 5:
                        orders_list.append(Order(*parts))
        
        # Сортировка пузырьком по фамилии
        self.bubble_sort_by_surname(orders_list)
        
        for idx, order in enumerate(orders_list):
            self.orders[idx] = order
            self.count += 1
    
    def bubble_sort_by_surname(self, orders_list):
        n = len(orders_list)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # Сравниваем фамилии (первое слово в fio)
                surname1 = orders_list[j].fio.split()[0].lower()
                surname2 = orders_list[j + 1].fio.split()[0].lower()
                if surname1 > surname2:
                    # Меняем элементы местами
                    orders_list[j], orders_list[j + 1] = orders_list[j + 1], orders_list[j]
    
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