from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter as tk

import requests

CURRENCY = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

CURRENCY_LIST_KEYS = list(CURRENCY.keys())

def show_rate_result(rate1, base1_name, rate2, base2_name, target_name):
    win = tk.Toplevel(root)
    win.title("Курс обмена")
    win.resizable(False, False)
    win.transient(root)
    win.grab_set()

    txt = tk.Text(win, wrap="word", borderwidth=0, highlightthickness=0,
                  width=20, height=3, font="Arial 20 bold")
    txt.pack()

    txt.insert("end", f"1 {base1_name} = {rate1:.2f} {target_name}\n")
    txt.insert("end", f"1 {base2_name} = {rate2:.2f} {target_name}\n")

    txt.config(state="disabled")

    btn = tk.Button(win, text="OK", width=10, command=win.destroy)
    btn.pack(pady=(0, 15))
    win.wait_window()

def config_translate(var, label):
    label.config(text=CURRENCY[var.get()])

def exchange():
    base1 = base1_var.get()
    base2 = base2_var.get()
    target = target_var.get()

    if not (base1 and base2 and target):
        messagebox.showwarning("Предупреждение", "Выберите валюту!")
        return

    if base1 == target or base2 == target:
        messagebox.showwarning("Предупреждение", "Базовая и целевая валюты не должны совпадать!")
        return

    try:
        # Запрос для первой базовой валюты
        response1 = requests.get(f'https://open.er-api.com/v6/latest/{base1}')
        response1.raise_for_status()
        data1 = response1.json()
        # Запрос для второй базовой валюты
        response2 = requests.get(f'https://open.er-api.com/v6/latest/{base2}')
        response2.raise_for_status()
        data2 = response2.json()

        if target not in data1['rates'] or target not in data2['rates']:
            messagebox.showerror("Ошибка", f"Валюта {target} не найдена")
            return

        rate1 = data1['rates'][target]
        rate2 = data2['rates'][target]

        base1_name = base1_combobox.get()
        base2_name = base2_combobox.get()
        target_name = target_combobox.get()

        show_rate_result(rate1, base1_name, rate2, base2_name, target_name)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка: {e}")

root = Tk()
root.title("Курсы обмена валют")

WIDTH, HEIGHT = 350, 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w - WIDTH) // 2
y = (screen_h - HEIGHT) // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
root.resizable(False, False)

# Единый стиль отступов
PAD_Y_LABEL = (10, 2)
PAD_Y_COMBO = (0, 5)
PAD_Y_TRANSLATE = (0, 20)

# Первая базовая валюта
Label(text="Базовая валюта").pack(pady=PAD_Y_LABEL)

base1_var = StringVar(value="")
base1_combobox = Combobox(
    width=25,
    values=CURRENCY_LIST_KEYS,
    state="readonly",
    textvariable=base1_var,
)
base1_combobox.bind("<<ComboboxSelected>>", lambda e: config_translate(base1_var, base1_label))
base1_combobox.pack(pady=PAD_Y_COMBO)

base1_label = Label(text="")
base1_label.pack(pady=PAD_Y_TRANSLATE)

# Вторая базовая валюта
Label(text="Вторая базовая валюта").pack(pady=PAD_Y_LABEL)

base2_var = StringVar(value="")
base2_combobox = Combobox(
    width=25,
    values=CURRENCY_LIST_KEYS,
    state="readonly",
    textvariable=base2_var,
)
base2_combobox.bind("<<ComboboxSelected>>", lambda e: config_translate(base2_var, base2_label))
base2_combobox.pack(pady=PAD_Y_COMBO)

base2_label = Label(text="")
base2_label.pack(pady=PAD_Y_TRANSLATE)

# Целевая валюта
Label(text="Целевая валюта").pack(pady=PAD_Y_LABEL)

target_var = StringVar(value="")
target_combobox = Combobox(
    width=25,
    values=CURRENCY_LIST_KEYS,
    state="readonly",
    textvariable=target_var,
)
target_combobox.bind("<<ComboboxSelected>>", lambda e: config_translate(target_var, target_label))
target_combobox.pack(pady=PAD_Y_COMBO)

target_label = Label(text="")
target_label.pack(pady=PAD_Y_TRANSLATE)


btn = Button(text="Получить курс обмена", bg="green",command=exchange)
btn.pack()

root.mainloop()
