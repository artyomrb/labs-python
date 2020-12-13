import tkinter as tk


# метод добавления цифры в окошко


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)

def add_operation(operation):
    value = calc.get()
    if value[-1]  in '-+/*':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)

def calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))

def clear():
    calc.delete(0,tk.END)
    calc.insert(0,0)

# метод добавления кнопок цифр


def make_digit(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def make_oper(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=lambda: add_operation(operation))


def make_calc(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=calculate)


def make_clear(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=clear)


win = tk.Tk()
win.geometry(f"240x270+100+200")
win['bg'] = '#FFC373'
win.title('Калькулятор')

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0,'0')
calc.grid(row=0, column=0, columnspan=4, stick='we',padx=5)

make_digit('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_oper('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_oper('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_oper('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_oper('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
