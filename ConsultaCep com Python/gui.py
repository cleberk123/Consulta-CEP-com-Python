import tkinter as tk
from tkinter import font
from cepUtil import ConsultaCep

class Janela:
    def __init__(self):
      self.consulta_cep = ConsultaCep()

    def janela(self) -> None:
        root = tk.Tk()
        main_title = tk.Label(root, text='Consulta CEP', bg='#fff', font=('Helvetica', 12, 'bold'))
        main_title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        stringvar = tk.StringVar()
        entry = tk.Entry(root, bd=5, relief='flat', textvariable=stringvar, highlightthickness=1)

        entry.grid(row=1, column=1, pady=10)

        label_result = tk.Label(root, text='Sem resultado ainda', justify='left',font=('Helvetica', 10, 'bold'), bg='#fff')
        label_result.grid(row=2, column=0, columnspan=3)

        button = tk.Button(root, text='Consultar')
        button.grid(row=1, column=2, sticky='we')
        button.configure(command=lambda: self.consulta_cep.consulta_cep(stringvar, label_result))

        root.title('Consulta CEP')
        root.config(background='#fff', padx=20, pady=20)
        root.mainloop()

main = Janela()
main.janela()