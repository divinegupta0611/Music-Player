import requests
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
import pygame
import os

#create main window
root = tk.Tk()
root.title("Tkinter frame example")
root.geometry("400x500")

# Blocking resizable
root.resizable(width="False",height="False")

# Set the background color to white
root.configure(bg="white")

# Create a Label with the text "Music Player"
label = tk.Label(root, text="Music Player", font=("Helvetica", 24, "bold"), fg="black", bg="white")
label.pack(pady=10)  # Add vertical padding


# Function to handle search
def search():
    query = search_entry.get()  # Get the text from the entry
    if query:
        messagebox.showinfo("Search Result", f"Searching for: {query}")
    else:
        messagebox.showwarning("Input Error", "Please enter a search query!")

# Create a Frame for the search bar
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

# Create an Entry widget for search input
search_entry = tk.Entry(search_frame, width=30, font=("Helvetica", 12))
search_entry.pack(side="left", padx=5)

# Create a Button to trigger the search
search_button = tk.Button(search_frame, text="Search", command=search, font=("Helvetica", 10, "bold"), fg="black")
search_button.pack(side="left", padx=5)

# Create a Frame to display three independent labels
labels_frame = tk.Frame(root, bg="white")
labels_frame.pack(pady=(5, 0), anchor="w")  # Reduce top padding, no bottom padding

# Add three labels in a single row
tk.Label(labels_frame, text="Label 1", bg="lightblue", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=(5, 0), sticky="w")
tk.Label(labels_frame, text="Label 2", bg="lightgreen", font=("Helvetica", 12)).grid(row=0, column=1, padx=10, pady=(5, 0), sticky="w")
tk.Label(labels_frame, text="Label 3", bg="lightcoral", font=("Helvetica", 12)).grid(row=0, column=2, padx=10, pady=(5, 0), sticky="w")

# Create a Frame for the labels and scrollbar
list_frame = tk.Frame(root)
list_frame.pack(fill="both", expand=True, pady=10)

# Create a Listbox widget to display labels
label_listbox = tk.Listbox(list_frame, font=("Helvetica", 12), bg="lightyellow", height=10)
label_listbox.pack(side="left", fill="both", expand=True, padx=5)

# Create a Scrollbar linked to the Listbox
scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=label_listbox.yview)
scrollbar.pack(side="right", fill="y", padx=5)

# Configure the Listbox to work with the scrollbar
label_listbox.config(yscrollcommand=scrollbar.set)

# Add 10 labels as items in the Listbox
for i in range(1, 31):
    label_listbox.insert(tk.END, f"Label {i}")

root.mainloop()
