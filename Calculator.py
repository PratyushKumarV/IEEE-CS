import tkinter as tk


def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(text=f"Result: {result}")


def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    result_label.config(text=f"Result: {result}")


def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    result_label.config(text=f"Result: {result}")


def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 == 0:
        result_label.config(text="Cannot divide by zero!")
    else:
        result = num1 / num2
        result_label.config(text=f"Result: {result}")


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create input fields
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Create buttons
add_button = tk.Button(root, text="Add", command=add)
add_button.pack(side=tk.LEFT)
multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.pack(side=tk.LEFT)
subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.pack(side=tk.LEFT)
divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.pack(side=tk.LEFT)

# Create result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
