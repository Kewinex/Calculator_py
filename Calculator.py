import tkinter as tk

window = tk.Tk()
window.resizable(False, False)
window.title("Kewculator")

label_1 = tk.Label(window, text="First number").grid(row=0, padx=10)
label_2 = tk.Label(window, text="Second number").grid(row=1, padx=10)
label_r = tk.Label(window, text="Result: ").grid(row=3, column=0, pady=10)

entry_1 = tk.Entry(window)
entry_2 = tk.Entry(window)

entry_1.grid(row=0, column=1, pady=5, padx=10)
entry_2.grid(row=1, column=1, pady=5, padx=10)

def calculate():
    number_1 = entry_1.get()
    number_2 = entry_2.get()   
    result = tk.Label(window, text=number_1+number_2).grid(row=3, column=1, pady=10)  

tk.Button(window, text='Add these two numbers', command=calculate).grid(row=2, column=0, columnspan=2, pady=10, padx=10)

window.mainloop()