import csv
import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def select_file():
    file_path = filedialog.askopenfilename(title="Выберите CSV-файл", filetypes=[("CSV-файлы", "*.csv")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def process_csv_file():
    try:
        file_path = file_entry.get()
        
        if not file_path:
            messagebox.showinfo("Информация", "Выберите файл.")
            return
        
        progress_bar['value'] = 0
        progress_label['text'] = "Обработка файла..."
        
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        
        if rows:
            oldest_bag = min(rows, key=lambda x: x['Дата изготовления'])
            
            # Генерируем QR-код для самого старого мешка
            data = (
                f"Номер: {oldest_bag['Номер']}\n"
                f"Наименование: {oldest_bag['Наименование продукции']}\n"
                f"Срок годности: {oldest_bag['Срок годности']}\n"
                f"Место на складе: {oldest_bag['Место на складе']}\n"
                f"Дата изготовления: {oldest_bag['Дата изготовления']}\n"
                f"Номер партии: {oldest_bag['Номер партии']}\n"
                f"Место выгрузки: {oldest_bag['Место выгрузки']}"
            )
            filename = "qr_code_oldest.png"
            generate_qr_code(data, filename)
            
            progress_bar['value'] = 50
            progress_label['text'] = "Генерация QR-кода..."
            
            # Удаляем строку с самым старым мешком из списка
            rows.remove(oldest_bag)
            
            # Записываем обновленный список обратно в CSV-файл
            fieldnames = rows[0].keys() if rows else []
            with open(file_path, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            
            progress_bar['value'] = 100
            progress_label['text'] = "Обработка завершена!"
            
            # Отображаем QR-код в отдельном окне
            qr_window = tk.Toplevel(root)
            qr_window.title("QR-код для самого старого мешка")
            qr_window.geometry("350x400")
            qr_window.configure(bg="#f7f7f7")
            
            qr_header_label = tk.Label(qr_window, text="QR-код для самого старого мешка", font=("Open Sans", 18), bg="#f7f7f7", fg="#333333")
            qr_header_label.pack(pady=10)
            
            qr_image = ImageTk.PhotoImage(Image.open(filename))
            qr_label = tk.Label(qr_window, image=qr_image, bg="#f7f7f7")
            qr_label.image = qr_image
            qr_label.pack(padx=10, pady=10)
            
            qr_footer_label = tk.Label(qr_window, text="Строка с самым старым мешком удалена из CSV-файла.", font=("Open Sans", 14), bg="#f7f7f7", fg="#666666")
            qr_footer_label.pack(pady=10)
        else:
            messagebox.showinfo("Информация", "Файл пуст.")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def main():
    global root, file_entry, progress_bar, progress_label
    root = tk.Tk()
    root.title("Приложение для генерации QR-кода")
    root.geometry("800x700")
    root.configure(bg="#f7f7f7")
    
    header_frame = tk.Frame(root, bg="#2196f3")
    header_frame.place(relx=0, rely=0, relwidth=1, height=50)
    
    header_label = tk.Label(header_frame, text="Приложение для генерации QR-кода", font=("Open Sans", 35), bg="#2196f3", fg="white")
    header_label.place(relx=0.5, rely=0.5, anchor="center")
    
    file_frame = tk.Frame(root, bg="#f7f7f7", highlightthickness=1, highlightbackground="#cccccc")
    file_frame.place(relx=0.5, rely=0.2, anchor="center", width=600, height=50)
    
    file_button = tk.Button(file_frame, text="Обзор", command=select_file, bg="#e0e0e0", fg="#666666", font=("Open Sans", 12), highlightthickness=0, width=10)
    file_button.pack(side=tk.LEFT)
    
    file_entry = tk.Entry(file_frame, width=50, font=("Open Sans", 14))
    file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    process_button = tk.Button(root, text="Сгенерировать QR-код", command=process_csv_file, bg="#4CAF50", fg="white", font=("Open Sans", 18))
    process_button.place(relx=0.5, rely=0.3, anchor="center")
    
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
    progress_bar.place(relx=0.5, rely=0.35, anchor="center")
    
    progress_label = tk.Label(root, text="", font=("Open Sans", 14), bg="#f7f7f7", fg="#666666")
    progress_label.place(relx=0.5, rely=0.4, anchor="center")
    
    info_label = tk.Label(root, text="Приложение генерирует QR-код для самого старого мешка в CSV-файле.", font=("Open Sans", 14), bg="#f7f7f7", fg="#666666")
    info_label.place(relx=0.5, rely=0.45, anchor="center")
    
    footer_frame = tk.Frame(root, bg="#2196f3")
    footer_frame.place(relx=0, rely=0.95, relwidth=1, height=50)
    
    footer_label = tk.Label(footer_frame, text="Приложение разработано для автоматизации процессов.", font=("Open Sans", 14), bg="#2196f3", fg="white")
    footer_label.place(relx=0.5, rely=0.5, anchor="center")
    
    root.mainloop()

if __name__ == "__main__":
    main()
