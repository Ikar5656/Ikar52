import csv
import tkinter as tk
from tkinter import messagebox, filedialog

class CSVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение для заполнения CSV-файла")
        self.csv_path = "products.csv"
        self.headers = ["Номер", "Наименование продукции", "Срок годности", "Место на складе", "Дата изготовления", "Номер партии", "Место выгрузки"]
        
        # Настройка цвета фона окна
        self.root.configure(bg="#f0f0f0")
        
        # Создание основной рамки
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(padx=20, pady=20)
        
        # Создание полей ввода
        self.create_widgets()
        
        # Проверка наличия файла и создание его при необходимости
        try:
            with open(self.csv_path, 'r') as file:
                pass
        except FileNotFoundError:
            self.write_to_csv({}, mode='w')
    
    def create_widgets(self):
        # Создание заголовка
        tk.Label(self.main_frame, text="Приложение для заполнения CSV-файла", font=("Arial", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Номер
        tk.Label(self.main_frame, text="Номер:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        self.number_entry = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.number_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Наименование продукции
        tk.Label(self.main_frame, text="Наименование продукции:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)
        self.product_name_entry = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.product_name_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Срок годности
        tk.Label(self.main_frame, text="Срок годности:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, padx=5, pady=5)
        self.shelf_life_entry = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.shelf_life_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Место на складе
        tk.Label(self.main_frame, text="Место на складе:", font=("Arial", 12), bg="#f0f0f0").grid(row=4, column=0, padx=5, pady=5)
        self.storage_place_entry = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.storage_place_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Дата изготовления
        tk.Label(self.main_frame, text="Дата изготовления (ГГГГ-ММ-ДД):", font=("Arial", 12), bg="#f0f0f0").grid(row=5, column=0, padx=5, pady=5)
        self.manufacture_date_entry = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.manufacture_date_entry.grid(row=5, column=1, padx=5, pady=5)
        
        # Номер партии
        tk.Label(self.main_frame, text="Номер партии:", font=("Arial", 12), bg="#f0f0f0").grid(row=6, column=0, padx=5, pady=5)
        self.batch_number_entry = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.batch_number_entry.grid(row=6, column=1, padx=5, pady=5)
        
        # Место выгрузки
        tk.Label(self.main_frame, text="Место выгрузки:", font=("Arial", 12), bg="#f0f0f0").grid(row=7, column=0, padx=5, pady=5)
        self.unload_place_entry = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.unload_place_entry.grid(row=7, column=1, padx=5, pady=5)
        
        # Путь к CSV-файлу
        tk.Label(self.main_frame, text="CSV-файл:", font=("Arial", 12), bg="#f0f0f0").grid(row=8, column=0, padx=5, pady=5)
        self.csv_path_entry = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.csv_path_entry.insert(0, self.csv_path)
        self.csv_path_entry.grid(row=8, column=1, padx=5, pady=5)
        
        # Кнопка для выбора CSV-файла
        tk.Button(self.main_frame, text="Выбрать файл", command=self.select_csv_file, font=("Arial", 12), bg="#007bff", fg="white").grid(row=8, column=2, padx=5, pady=5)
        
        # Кнопка для сохранения данных
        tk.Button(self.main_frame, text="Сохранить", command=self.save_data, font=("Arial", 12), bg="#007bff", fg="white").grid(row=9, column=0, columnspan=3, padx=5, pady=(20, 10))
        
        # Кнопка для очистки полей
        tk.Button(self.main_frame, text="Очистить", command=self.clear_fields, font=("Arial", 12), bg="#dc3545", fg="white").grid(row=10, column=0, columnspan=3, padx=5, pady=(0, 20))
    
    def select_csv_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV-файлы", "*.csv")])
        if path:
            self.csv_path_entry.delete(0, tk.END)
            self.csv_path_entry.insert(0, path)
            self.csv_path = path
    
    def write_to_csv(self, data, mode='a'):
        with open(self.csv_path, mode=mode, encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            
            if mode == 'w':
                writer.writeheader()  # Запись заголовков
            
            writer.writerow(data)
    
    def save_data(self):
        user_data = {
            "Номер": self.number_entry.get(),
            "Наименование продукции": self.product_name_entry.get(),
            "Срок годности": self.shelf_life_entry.get(),
            "Место на складе": self.storage_place_entry.get(),
            "Дата изготовления": self.manufacture_date_entry.get(),
            "Номер партии": self.batch_number_entry.get(),
            "Место выгрузки": self.unload_place_entry.get()
        }
        
        self.csv_path = self.csv_path_entry.get()
        
        # Проверка наличия файла и создание его при необходимости
        try:
            with open(self.csv_path, 'r') as file:
                pass
        except FileNotFoundError:
            self.write_to_csv({}, mode='w')
        
        self.write_to_csv(user_data)
        
        messagebox.showinfo("Успешно", "Данные сохранены в CSV-файл.")
    
    def clear_fields(self):
        self.number_entry.delete(0, tk.END)
        self.product_name_entry.delete(0, tk.END)
        self.shelf_life_entry.delete(0, tk.END)
        self.storage_place_entry.delete(0, tk.END)
        self.manufacture_date_entry.delete(0, tk.END)
        self.batch_number_entry.delete(0, tk.END)
        self.unload_place_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVApp(root)
    root.mainloop()
