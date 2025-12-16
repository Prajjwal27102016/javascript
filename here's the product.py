import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1_str = entry_num1.get()
        num2_str = entry_num2.get()
        
        num1 = float(num1_str)
        num2 = float(num2_str)
        
        product = num1 * num2
        
        result_label.config(text=f"Product: {product:.2f}") 
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")
        result_label.config(text="Product: Error")

root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x200")

tk.Label(root, text="First Number:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_num1 = tk.Entry(root, width=15)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Second Number:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_num2 = tk.Entry(root, width=15)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(
    root, 
    text="Calculate Product", 
    command=calculate_product,
    bg='lightblue'
)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Product: ", font=('Arial', 12, 'bold'))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()