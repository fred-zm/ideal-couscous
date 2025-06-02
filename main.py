import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Test Titel")
root.geometry("400x400")
root.minsize(width=250, height=250)
root.maxsize(width=600, height=600)
#root.resizable(width=False, height=False)
root.geometry()
label1 = tk.Label(root, text="Test", bg='light blue')
label1.pack(side='top', expand=True, fill='y')
label2 = tk.Label(root, text="TEstTESTTEST", bg='red')
label2.pack()
label3 = ttk.Label(root, text="ttk Label")
label3.pack()
button1 = tk.Button(root, text="Schließen", command=root.destroy)
button1.pack()
button2 = ttk.Button(root, text="ttk Button")
button2.pack()
root.mainloop()

print("Ende")