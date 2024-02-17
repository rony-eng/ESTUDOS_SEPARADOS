import tkinter as tk

class Calculadora(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.buttons = {}
        for i in range(10):
            self.buttons[str(i)] = tk.Button(self, text=str(i), command=lambda x=i: self.add_to_entry(x))
            self.buttons[str(i)].pack(side=tk.LEFT)

        self.buttons["+"] = tk.Button(self, text="+", command=lambda: self.add_to_entry("+"))
        self.buttons["+"].pack(side=tk.LEFT)

        self.buttons["-"] = tk.Button(self, text="-", command=lambda: self.add_to_entry("-"))
        self.buttons["-"].pack(side=tk.LEFT)

        self.buttons["*"] = tk.Button(self, text="*", command=lambda: self.add_to_entry("*"))
        self.buttons["*"].pack(side=tk.LEFT)

        self.buttons["/"] = tk.Button(self, text="/", command=lambda: self.add_to_entry("/"))
        self.buttons["/"].pack(side=tk.LEFT)

        self.buttons["="] = tk.Button(self, text="=", command=self.calcular)
        self.buttons["="].pack(side=tk.LEFT)

    def add_to_entry(self, text):
        self.entry.insert(tk.END, text)

    def calcular(self):
        expressao = self.entry.get()
        try:
            resultado = eval(expressao)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk)
        except: # esta except está errada - posteriormente tem que corrigi
            resultado = eval(expressao)