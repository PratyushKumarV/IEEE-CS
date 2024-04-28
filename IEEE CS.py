import tkinter as tk


def show_input():
    input_text = entry.get()
    label.config(text="Input: " + input_text)


# Create the main application window
root = tk.Tk()
root.title("Input Example")

# Create a label and entry widget for input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to show input
button = tk.Button(root, text="Show Input", command=show_input)
button.pack(pady=5)

# Create a label to display input
label = tk.Label(root, text="")
label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
