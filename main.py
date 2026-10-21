from tkinter import *
from tkinter.ttk import Combobox

dict_currency = {
    "EUR": "Евро",
    "USD": "Американсий доллар",
    "RUS": "Российский рубль",
}

list_currency = list(dict_currency.keys())

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
base_currency_var = StringVar(value=list_currency[0])

base_currency_label = Label(text="Базовая валюта")
base_currency_label.pack(pady=PAD_Y_LABEL)

base_currency_combobox = Combobox(
    width=25,
    values=list_currency ,
    state="readonly",
    textvariable=base_currency_var,
)

base_currency_combobox.pack(pady=PAD_Y_COMBO)

base_currency_translate_label = Label(textvariable=base_currency_var)
base_currency_translate_label.pack(pady=PAD_Y_TRANSLATE)


# Вторая базовая валюта
two_currency_var = StringVar(value=list_currency[1])

two_base_currency_label = Label(text="Вторая базовая валюта")
two_base_currency_label.pack(pady=PAD_Y_LABEL)

two_base_currency_combobox = Combobox(
    width=25,
    values=list_currency,
    state="readonly",
    textvariable=two_currency_var,
)
two_base_currency_combobox.pack(pady=PAD_Y_COMBO)

two_base_translate_label = Label(textvariable=two_currency_var)
two_base_translate_label.pack(pady=PAD_Y_TRANSLATE)


# Целевая валюта
target_currency_var = StringVar(value=list_currency[2])

target_currency_label = Label(text="Целевая валюта")
target_currency_label.pack(pady=PAD_Y_LABEL)

target_currency_combobox = Combobox(
    width=25,
    values=list_currency,
    state="readonly",
    textvariable=target_currency_var,
)
target_currency_combobox.pack(pady=PAD_Y_COMBO)

target_currency_translate_label = Label(textvariable=target_currency_var)
target_currency_translate_label.pack(pady=PAD_Y_TRANSLATE)

# Кнопка
start_btn = Button(text="Получить курс обмена")
start_btn.pack(pady=15)

root.mainloop()
