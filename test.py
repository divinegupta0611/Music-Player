import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Grid Example")

# Create labels
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label3 = tk.Label(root, text="Label 3", bg="blue", fg="white")

# Use grid to position the labels
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=0, column=1, padx=10, pady=10)
label3.grid(row=0, column=2, padx=10, pady=10)

# Run the application
root.mainloop()
