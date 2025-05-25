from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import sys
from building_supplies_group import OrderManager

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("building_supplies.ui", self)
        
        self.order_manager = OrderManager()
        
        # Подключение кнопок
        self.load_data_button.clicked.connect(self.load_data)
        self.update_data_button.clicked.connect(self.update_data)
        self.clear_data_button.clicked.connect(self.clear_data)
    
    def load_data(self):
        """Загрузка данных из файла"""
        self.order_manager.read_from_file("orders.txt")
        self.update_table()
        QMessageBox.information(self, "Успех", "Данные успешно загружены!")
    
    def update_data(self):
        """Обновление данных из файла"""
        if self.order_manager.count == 0:
            QMessageBox.warning(self, "Предупреждение", "Нет данных для обновления! Сначала загрузите данные.")
            return
        
        self.order_manager.read_from_file("orders.txt")
        self.update_table()
        QMessageBox.information(self, "Успех", "Данные успешно обновлены!")
    
    def clear_data(self):
        """Очистка таблицы"""
        self.order_manager = OrderManager()
        self.orders_table.setRowCount(0)
        QMessageBox.information(self, "Успех", "Таблица очищена!")
    
    def update_table(self):
        """Обновление данных в таблице"""
        self.orders_table.setRowCount(self.order_manager.count)
        
        for row in self.order_manager.orders:
            order = self.order_manager.orders[row]
            self.orders_table.setItem(row, 0, QTableWidgetItem(order.fio))
            self.orders_table.setItem(row, 1, QTableWidgetItem(order.workplace))
            self.orders_table.setItem(row, 2, QTableWidgetItem(order.product))
            self.orders_table.setItem(row, 3, QTableWidgetItem(f"{order.price:.2f}"))
            self.orders_table.setItem(row, 4, QTableWidgetItem(str(order.quantity)))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()