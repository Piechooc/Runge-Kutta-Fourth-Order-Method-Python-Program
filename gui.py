from tkinter import *
from runge_kutta import RungeKutta
from Functions import Functions
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from pandas import DataFrame
from datetime import datetime
from FunctionBuilder import FunctionBuilder

#TODO
#skompilowac do exe
#obsluga klawiatury na dolne wiersze
#wyjątki
#usuwanie wykresu dla nowych danych
#opakowac w funkcje
#naprawić epsilony

FONT_SIZE = 12
FONT_STYLE = "Default"

class Gui:
    def __init__(self):
        self.gui = Tk()
        self.gui.geometry("1280x770")
        self.gui.title("Runge Kutta Fourth Order Method Python Program")

        self.input_frame = Frame(self.gui)
        self.input_equation_entry = Entry(self.input_frame, width=40, font=(FONT_STYLE, FONT_SIZE))
        self.input_t0 = Entry(self.input_frame, width=17, font=(FONT_STYLE, FONT_SIZE))
        self.input_tn = Entry(self.input_frame, width=18, font=(FONT_STYLE, FONT_SIZE))
        self.input_x0 = Entry(self.input_frame, width=17, font=(FONT_STYLE, FONT_SIZE))

        self.function = None
        self.label_epsilon = None
        self.label_n = None
        self.file_to_save = None
        self.is_custom = False

        self.n = 2

    def _create_input_frame(self):
        label_y = Label(self.input_frame, text="x'= ", font=(FONT_STYLE, FONT_SIZE))
        label_x0 = Label(self.input_frame,text="x\u2080= " ,font=(FONT_STYLE, FONT_SIZE))
        label_t0 = Label(self.input_frame,text="t\u2080= ",font=(FONT_STYLE, FONT_SIZE))
        label_tn = Label(self.input_frame,text="t\u2099= ",font=(FONT_STYLE, FONT_SIZE))

        label_y.grid(column=1, row=0, pady=5, padx=10,sticky=E)
        label_t0.grid(column=1, row=1, pady=5, padx=10,sticky=E)
        label_x0.grid(column=1, row=2, pady=5, padx=10,sticky=W)


        self.input_equation_entry.grid(column=2, row=0, pady=5)
        self.input_t0.grid(column=2, row=1, pady=5, sticky=W)
        self.input_x0.grid(column=2, row=2, pady=5,sticky=W)


        label_tn.grid(column=2,row=1, pady=5)
        self.input_tn.grid(column=2, row=1, pady=5,sticky=E)


    def _create_start_button(self):
        start_button = Button(self.input_frame, text="calculate", command=self._calculate, width=17,
                              font=(FONT_STYLE, FONT_SIZE))
        start_button.grid(column=2, row=2, pady=5,sticky=E)


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

        button_t = Button(keyboard, text="t", padx=20, pady=20, command=lambda: self._button_click("t"))
        button_xt = Button(keyboard, text="x(t)", padx=20, pady=20, command=lambda: self._button_click("x(t)"))

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
        button_more_steps = Button(keyboard, text="next step",padx=20, pady=20, command=self._update_chart)

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
        button_backspace.grid(column=10, row=0)

        button_t.grid(column=0, row=1)
        button_xt.grid(column=1, row=1)
        button_plus.grid(column=2, row=1)
        button_minus.grid(column=3, row=1)
        button_division.grid(column=4, row=1)
        button_multiplication.grid(column=5, row=1)
        button_sinus.grid(column=6, row=1)
        button_cosinus.grid(column=7, row=1)
        button_open_bracket.grid(column=8, row=1)
        button_close_bracket.grid(column=9, row=1)
        button_more_steps.grid(column=10, row=1)


        keyboard.pack(side=BOTTOM)

    def _update_chart(self):
        self.n *= 2
        self.figure.clear()
        self.label_n.destroy()
        ax = self.figure.add_subplot(111)

        if self.is_custom:
            data = RungeKutta.runge_kutta_custom(float(self.input_t0.get()), float(self.input_x0.get()),
                                                 float(self.input_tn.get()), self.n,
                                                 FunctionBuilder(self.input_equation_entry.get()).function)
            epsilon = 0

        else:
            self.label_epsilon.destroy()
            data, solution, epsilon = RungeKutta.runge_kutta(float(self.input_t0.get()), float(self.input_x0.get()),
                                                             float(self.input_tn.get()), self.n, self.function[0],
                                                             self.function[1])

            df_solution = DataFrame(solution, columns=['exact_t', 'exact_x'])
            df_solution = df_solution[['exact_t', 'exact_x']].groupby('exact_t').sum()
            df_solution.plot(kind='line', legend=True, ax=ax, color='r', marker=',', fontsize=10)


        df = DataFrame(data,columns=['t','x(t)'])
        df = df[['t','x(t)']].groupby('t').sum()
        df.plot(kind='line', legend=True, ax=ax, color='b',marker='o', fontsize=10)



        ax.set_title('Solution plot')
        self._show_statistics(epsilon)
        self.chart_type.draw_idle()

    def _create_chart(self, data, solution):
        self.figure = plt.Figure(figsize=(7, 4), dpi=80)
        ax = self.figure.add_subplot(111)
        self.chart_type = FigureCanvasTkAgg(self.figure, self.gui)
        self.chart_type.get_tk_widget().pack(side=BOTTOM)

        toolbar = NavigationToolbar2Tk(self.chart_type,self.gui)
        toolbar.update()
        toolbar.pack(side=BOTTOM, fill=Y)

        df = DataFrame(data,columns=['t','x(t)'])
        self.file_to_save = df
        df = df[['t','x(t)']].groupby('t').sum()
        df.plot(kind='line', legend=True, ax=ax, color='b',marker='o', fontsize=10)

        df_solution = DataFrame(solution,columns=['exact_t','exact_x'])
        df_solution = df_solution[['exact_t','exact_x']].groupby('exact_t').sum()
        df_solution.plot(kind='line', legend=True, ax=ax, color='r',marker=',', fontsize=10)



        ax.set_title('Solution plot')

    def _create_checkboxes(self):
        var = StringVar(self.input_frame, "0")
        label_functions = Label(self.input_frame,text="Functions: ",pady=5,font=(FONT_STYLE, FONT_SIZE))
        label_functions.grid(column=0,row=0,sticky=W)

        checkboxes = {"x' = -2 * x * e\u1D57" : "1","x' = (t - 3/t + 2) * (1/2)" : "2","x' = (x\u00B2 + t\u00B2)/(t*x)" : "3"}

        cnt = 1
        for (text, value) in checkboxes.items():
            Radiobutton(self.input_frame, text=text, variable=var,
                        value=value,font=(FONT_STYLE, FONT_SIZE),command=lambda:self._handle_checkboxes(var)).grid(column=0,row=cnt, ipady=5, sticky=W)
            cnt += 1

        Radiobutton(self.input_frame, text="custom", variable=var,
                    value="4", font=(FONT_STYLE, FONT_SIZE), command=lambda: self._handle_checkboxes(var)).grid(
            column=0, row=cnt, ipady=5, sticky=W)


    def _handle_checkboxes(self,var):
        options = [["-2 * x * e**t",0,1,1],["(t - 3/t + 2) * (1/2)",1,2,0],["(x**2 + t**2)/(t*x)",1,2,-1]] #f,t0,tn,x0
        self.input_equation_entry.delete(0,END)
        self.input_x0.delete(0,END)
        self.input_t0.delete(0,END)
        self.input_tn.delete(0,END)

        ind = int(var.get()) - 1

        if ind == 3:
            self.is_custom = True
            return

        self.input_equation_entry.insert(0,options[ind][0])
        self.input_t0.insert(0,options[ind][1])
        self.input_tn.insert(0,options[ind][2])
        self.input_x0.insert(0,options[ind][3])

        functions = {0: (Functions.f1, Functions.f1_solution),1: (Functions.f2, Functions.f2_solution),
                     2: (Functions.f3, Functions.f3_solution)}
        self.function = functions[ind]


    def return_parameters(self):
        return self.input_equation_entry.get(),self.input_t0.get(),self.input_tn.get(),self.input_x0.get()


    def _show_statistics(self,epsilon):
        self.label_n = Label(self.gui,text=f"steps: {str(self.n)}",font=(FONT_STYLE, FONT_SIZE))
        self.label_epsilon = Label(self.gui,text=f"epsilon: {str(epsilon)}",font=(FONT_STYLE, FONT_SIZE))

        self.label_n.pack()
        self.label_epsilon.pack()

    def _calculate(self):
        if self.is_custom:
            data = RungeKutta.runge_kutta_custom(float(self.input_t0.get()), float(self.input_x0.get()),
                                                float(self.input_tn.get()), self.n,
                                          FunctionBuilder(self.input_equation_entry.get()).function)
            self._create_custom_chart(data)

        else:
            data, solution,epsilon = RungeKutta.runge_kutta(float(self.input_t0.get()), float(self.input_x0.get()),
                                                     float(self.input_tn.get()), self.n, self.function[0], self.function[1])
            self.label_epsilon = Label(self.gui, text=f"epsilon: {str(epsilon)}", font=(FONT_STYLE, FONT_SIZE))
            self.label_epsilon.pack()
            self._create_chart(data, solution)

        self.label_n = Label(self.gui, text=f"steps: {str(self.n)}", font=(FONT_STYLE, FONT_SIZE))
        self.label_n.pack()

    def _create_custom_chart(self,data):
        self.figure = plt.Figure(figsize=(7, 4), dpi=80)
        ax = self.figure.add_subplot(111)
        self.chart_type = FigureCanvasTkAgg(self.figure, self.gui)
        self.chart_type.get_tk_widget().pack(side=BOTTOM)

        toolbar = NavigationToolbar2Tk(self.chart_type,self.gui)
        toolbar.update()
        toolbar.pack(side=BOTTOM, fill=Y)

        df = DataFrame(data,columns=['t','x(t)'])
        self.file_to_save = df
        df = df[['t','x(t)']].groupby('t').sum()
        df.plot(kind='line', legend=True, ax=ax, color='b',marker='o', fontsize=10)

        ax.set_title('Solution plot')

    def _create_save_button(self):
        save_button = Button(self.input_frame, text="save", command=self._save, width=17,
                              font=(FONT_STYLE, FONT_SIZE))
        save_button.grid(column=2,row=3,pady=5,sticky=E)

    def _save(self):
        self.file_to_save.to_csv("data " + str(datetime.now().strftime("%H_%M_%S") + ".txt"), encoding='utf-8', index=False, sep=';')

    def run(self):
        self._create_input_frame()
        self._create_start_button()
        self._create_keyboard()
        self._create_checkboxes()
        self._create_save_button()
        self.input_frame.pack(pady=15)
        self.gui.mainloop()
