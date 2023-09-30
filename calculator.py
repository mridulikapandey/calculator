import tkinter as tk

# Function to update the display
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to perform arithmetic operations
def arithmetic_operation():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget to display the numbers and results
entry = tk.Entry(window, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operations
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, padx=20, pady=20, font=("Arial", 16), command=arithmetic_operation).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, font=("Arial", 16), command=lambda btn=button: button_click(btn)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI application
window.mainloop()
