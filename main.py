import tkinter as tk
from tkinter import ttk
#from PIL import Image, ImageTk
#pip install pillow ?

def test():
    text_variable.set(text_variable.get() + "1")
    button1['state'] = tk.NORMAL
    print_entry_input()

def print_entry_input():
    ttk.Label(root, text=entry.get()).pack()



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
label3 = ttk.Label(root, text="ttk Label", compound='top', padding=20)
label3.pack()

button1 = tk.Button(root, text="Schließen", state=tk.DISABLED, command=root.destroy)
button1.pack()
text_variable = tk.StringVar()
text_variable.set("Text")
#IntVar, DoubleVar, BooleanVar
#print(text_variable.get())
button2 = ttk.Button(root, textvariable=text_variable, command=test)
button2.pack()
for item in button2.keys():
    print(item, ': ', button2[item])

entry = tk.Entry(root, width=40, justify="center")
entry.insert(0, "Tt")
entry.insert(1, "es")
entry.pack()

def clear_entry(test):
    entry.delete(0, tk.END)
entry.bind("<FocusIn>", clear_entry)

for item in entry.keys():
    print(item, ': ', entry[item])

root.mainloop()

print("Ende")