import random
import string
import tkinter as tk
from tkinter import ttk
import pyperclip

def parameter_password():
    entry.delete(0, 'end')  # стирает сгенерированный пароль из окна ввода
    length = var_1.get()  # длина пароля
    count = count_checkmarks()  
    password = generator_pass(length, count)
    return password

def count_checkmarks():  # функция, подсчитывающая количество checkbox
    count = 0
    if checkbox_upper.get():
        count += 1
    if checkbox_lower.get():
        count += 1
    if checkbox_digits.get():
        count += 1
    if checkbox_symbols.get():
        count += 1
    return count

def generator_pass(length, count):  # основная функция, которая генерирует пароль по заданным параметрам
    password = ''
    lower = string.ascii_lowercase  
    upper = string.ascii_uppercase  
    digits = string.digits  
    symbols = string.punctuation  
  
    if count == 1:
        if checkbox_upper.get():
            for i in range(0, length):
                password += random.choice(upper)
            return password
        elif checkbox_lower.get():
            for i in range(0, length):
                password += random.choice(lower)
            return password
        elif checkbox_digits.get():
            for i in range(0, length):
                password += random.choice(digits)
            return password
        elif checkbox_symbols.get():
            for i in range(0, length):
                password += random.choice(symbols)
            return password

    if count == 2:
        if checkbox_upper.get() and checkbox_lower.get():
            password += random.choice(lower)  # оставляем минимум одну букву в нижнем регистре
            password += random.choice(upper)  # оставляем минимум одну букву в верхнем регистре
            for i in range(0, length - count):  # length - count - из длины убираем два символа, кторые точно должны быть в пароле
                password += random.choice(upper + lower)
            return password
        elif checkbox_upper.get() and checkbox_digits.get():
            password += random.choice(upper)
            password += random.choice(digits)
            for i in range(0, length - count):
                password += random.choice(upper + digits)
            return password
        elif checkbox_upper.get() and checkbox_symbols.get():
            password += random.choice(upper)
            password += random.choice(symbols)
            for i in range(0, length - count):
                password += random.choice(upper + symbols)
            return password
        elif checkbox_lower.get() and checkbox_digits.get():
            password += random.choice(lower)
            password += random.choice(digits)
            for i in range(0, length - count):
                password += random.choice(lower + digits)
            return password
        elif checkbox_lower.get() and checkbox_symbols.get():
            password += random.choice(lower)
            password += random.choice(symbols)
            for i in range(0, length - count):
                password += random.choice(lower + symbols)
            return password
        elif checkbox_digits.get() and checkbox_symbols.get():
            password += random.choice(digits)
            password += random.choice(symbols)
            for i in range(0, length - count):
                password += random.choice(digits + symbols)
            return password

    if count == 3:
        if checkbox_upper.get() and checkbox_lower.get() and checkbox_digits.get():
            password += random.choice(upper)
            password += random.choice(lower)
            password += random.choice(digits)
            for i in range(0, length - count):
                password += random.choice(upper + lower + digits)
            return password
        elif checkbox_upper.get() and checkbox_lower.get() and checkbox_symbols.get():
            password += random.choice(upper)
            password += random.choice(lower)
            password += random.choice(symbols)
            for i in range(0, length - count):
                password += random.choice(upper + lower + symbols)
            return password
        elif checkbox_upper.get() and checkbox_digits.get() and checkbox_symbols.get():
            password += random.choice(upper)
            password += random.choice(digits)
            password += random.choice(symbols)
            for i in range(0, length - count):
                password += random.choice(upper + digits + symbols)
            return password
        elif checkbox_lower.get() and checkbox_digits.get() and checkbox_symbols.get():
            password += random.choice(lower)
            password += random.choice(digits)
            password += random.choice(symbols)
            for i in range(0, length - count):
                password += random.choice(lower + digits + symbols)
            return password

    if count == 4:
        if checkbox_upper.get() and checkbox_lower.get() and checkbox_digits.get() and checkbox_symbols.get():
            password += random.choice(upper)
            password += random.choice(lower)
            password += random.choice(digits)
            password += random.choice(symbols)
            for i in range(0, length - count):
                password += random.choice(upper + lower + digits + symbols)
            return password

def button_generate_password():  # функция генерации пароля в окно ввода
    password_1 = parameter_password()
    entry.insert(0, password_1)

def copy_your_password():  # функция копирования пароля в буфер обмена
    copy_password = entry.get()
    pyperclip.copy(copy_password)

# Создание окна
root = tk.Tk()
var_1 = tk.IntVar()

# Название окна
root.title = ('Генератор случайных паролей')

# Добавление ярлыка для отображения текста и поля для вывода пароля
Password = tk.Label(root, text = 'Пароль:')
Password.grid(row = 0, column = 0)
entry = tk.Entry(root)
entry.grid(row = 0, column = 1)

# Добавление ярлыка (Label) для отображения длины пароля
label = tk.Label(root, text = 'Длина пароля:')
label.grid(row = 1, column = 0)

# Кнопка копирования пароля
copy_button = tk.Button(root, text = 'Скопировать пароль', command = copy_your_password)
copy_button.grid(row = 0, column= 3)

# Кнопка генерации пароля
generate_button = tk.Button(root, text = 'Сгенерировать пароль', command = button_generate_password)
generate_button.grid(row = 0, column = 2)

# Создание выпадающего списка для выбора пользователя
combo_length_of_password = ttk.Combobox(root, textvariable = var_1)
combo_length_of_password['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                      20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                     30, 'Введите длину')
combo_length_of_password.current(0)
combo_length_of_password.grid(row = 1, column = 1)

# Создание флажка на выбор пользователя параметров генерируемого пароля
# Галочка для Верхнего регистра букв
checkbox_upper = tk.BooleanVar()

check_upper = tk.Checkbutton(root, text ='Использовать заглавные буквы', var = checkbox_upper)
check_upper.grid(row = 2, column = 0)

# Галочка для нижнего регистра букв
checkbox_lower = tk.BooleanVar()

check_lower = tk.Checkbutton(root, text ='Использовать строчные буквы', var = checkbox_lower)
check_lower.grid(row = 3, column = 0)

# Галочка для цифр
checkbox_digits = tk.BooleanVar()

check_digits = tk.Checkbutton(root, text ='Использовать цифры              ', var = checkbox_digits)
check_digits.grid(row = 2, column = 1)

# Галочка для спец.символов
checkbox_symbols = tk.BooleanVar()

check_symbols = tk.Checkbutton(root, text ='Использовать спец.символы', var = checkbox_symbols)
check_symbols.grid(row = 3, column = 1)

# Запуск окна
root.mainloop()
