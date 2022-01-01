from tkinter import *


class Gui:
    def __init__(self):
        self.gui = Tk()
        self.gui.geometry("900x700")
        self.gui.title("Runge Kutta Fourth Order Method Python Program")

        self.input_frame = Frame(self.gui)
        self.input_equation_entry = Entry(self.input_frame, width=40, font=("Default", 20))

    def _create_input_frame(self):
        self.label_y = Label(self.input_frame, text="y': ", font=("Default", 20))
        self.label_y.grid(column=0, row=0, pady=5)

        self.input_equation_entry.grid(column=1, row=0, pady=5)

    def _calculate(self):
        input_equation_string = self.input_equation_entry.get()

        # TODO
        # trzeba przekazać równanie do algorytmu

    def _create_start_button(self):
        start_button = Button(self.input_frame, text="Calculate", command=self._calculate, width=10,
                              font=("Default", 20))
        start_button.grid(column=0, row=1, pady=5, columnspan=2)
        self.input_frame.pack(pady=30)

    def _button_click(self, char):
        current = self.input_equation_entry.get()
        self.input_equation_entry.delete(0, END)
        self.input_equation_entry.insert(0, str(current) + str(char))

    def _backspace_click(self):
        current = self.input_equation_entry.get()
        if current == "":
            return
        else:
            self.input_equation_entry.delete(len(current) - 1)

    def _create_keyboard(self):
        keyboard = Frame(self.gui)
        keyboard_buttons = {}

        button_0 = Button(keyboard, text="0", padx=20, pady=20, command=lambda: self._button_click(0))
        button_1 = Button(keyboard, text="1", padx=20, pady=20, command=lambda: self._button_click(1))
        button_2 = Button(keyboard, text="2", padx=20, pady=20, command=lambda: self._button_click(2))
        button_3 = Button(keyboard, text="3", padx=20, pady=20, command=lambda: self._button_click(3))
        button_4 = Button(keyboard, text="4", padx=20, pady=20, command=lambda: self._button_click(4))
        button_5 = Button(keyboard, text="5", padx=20, pady=20, command=lambda: self._button_click(5))
        button_6 = Button(keyboard, text="6", padx=20, pady=20, command=lambda: self._button_click(6))
        button_7 = Button(keyboard, text="7", padx=20, pady=20, command=lambda: self._button_click(7))
        button_8 = Button(keyboard, text="8", padx=20, pady=20, command=lambda: self._button_click(8))
        button_9 = Button(keyboard, text="9", padx=20, pady=20, command=lambda: self._button_click(9))

        button_x = Button(keyboard, text="x", padx=20, pady=20, command=lambda: self._button_click("x"))
        button_y = Button(keyboard, text="y", padx=20, pady=20, command=lambda: self._button_click("x"))

        button_plus = Button(keyboard, text="+", padx=20, pady=20, command=lambda: self._button_click("+"))
        button_minus = Button(keyboard, text="-", padx=20, pady=20, command=lambda: self._button_click("-"))
        button_division = Button(keyboard, text="/", padx=20, pady=20, command=lambda: self._button_click("/"))
        button_multiplication = Button(keyboard, text="*", padx=20, pady=20, command=lambda: self._button_click("*"))
        button_sinus = Button(keyboard, text="sin", padx=20, pady=20,
                              command=lambda: self._button_click("sin"))  # tutaj mozna dodac otwieranie nawiasu
        button_cosinus = Button(keyboard, text="cos", padx=20, pady=20, command=lambda: self._button_click("cos"))
        button_open_bracket = Button(keyboard, text="(", padx=20, pady=20, command=lambda: self._button_click("("))
        button_close_bracket = Button(keyboard, text=")", padx=20, pady=20, command=lambda: self._button_click(")"))
        button_backspace = Button(keyboard, text="backspace", padx=20, pady=20, command=self._backspace_click)

        button_0.grid(column=0, row=0)
        button_1.grid(column=1, row=0)
        button_2.grid(column=2, row=0)
        button_3.grid(column=3, row=0)
        button_4.grid(column=4, row=0)
        button_5.grid(column=5, row=0)
        button_6.grid(column=6, row=0)
        button_7.grid(column=7, row=0)
        button_8.grid(column=8, row=0)
        button_9.grid(column=9, row=0)

        button_x.grid(column=0, row=1)
        button_y.grid(column=1, row=1)
        button_plus.grid(column=2, row=1)
        button_minus.grid(column=3, row=1)
        button_division.grid(column=4, row=1)
        button_multiplication.grid(column=5, row=1)
        button_sinus.grid(column=6, row=1)
        button_cosinus.grid(column=7, row=1)
        button_open_bracket.grid(column=8, row=1)
        button_close_bracket.grid(column=9, row=1)
        button_backspace.grid(column=10, row=0)

        keyboard.pack(side=BOTTOM)

    def run(self):
        self._create_input_frame()
        self._create_start_button()
        self._create_keyboard()
        self.gui.mainloop()
