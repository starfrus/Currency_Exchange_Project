from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

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

        base1_name = CURRENCY[base1]
        base2_name = CURRENCY[base2]
        target_name = CURRENCY[target]

        messagebox.showinfo(
            "Курс обмена",
            f"Курс {rate1:.2f} {target_name} за 1 {base1_name}\n"
            ""
            f"Курс {rate2:.2f} {target_name} за 1 {base2_name}"
        )
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
base1_combobox.bind("<<ComboboxSelected>>", lambda e: config_translate(base1_var, base1_translate_label))
base1_combobox.pack(pady=PAD_Y_COMBO)

base1_translate_label = Label(text="")
base1_translate_label.pack(pady=PAD_Y_TRANSLATE)

# Вторая базовая валюта
Label(text="Вторая базовая валюта").pack(pady=PAD_Y_LABEL)

base2_var = StringVar(value="")
base2_combobox = Combobox(
    width=25,
    values=CURRENCY_LIST_KEYS,
    state="readonly",
    textvariable=base2_var,
)
base2_combobox.bind("<<ComboboxSelected>>", lambda e: config_translate(base2_var, base2_translate_label))
base2_combobox.pack(pady=PAD_Y_COMBO)

base2_translate_label = Label(text="")
base2_translate_label.pack(pady=PAD_Y_TRANSLATE)

# Целевая валюта
Label(text="Целевая валюта").pack(pady=PAD_Y_LABEL)

target_var = StringVar(value="")
target_combobox = Combobox(
    width=25,
    values=CURRENCY_LIST_KEYS,
    state="readonly",
    textvariable=target_var,
)
target_combobox.bind("<<ComboboxSelected>>", lambda e: config_translate(target_var, target_translate_label))
target_combobox.pack(pady=PAD_Y_COMBO)

target_translate_label = Label(text="")
target_translate_label.pack(pady=PAD_Y_TRANSLATE)

# Кнопка
start_btn = Button(text="Получить курс обмена", command=exchange)
start_btn.pack(pady=15)

root.mainloop()
