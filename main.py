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

# # Create a canvas and a scrollbar
# canvas = tk.Canvas(root)
# scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="y")

# # Configure the canvas to work with the scrollbar
# canvas.configure(yscrollcommand=scrollbar.set)
# canvas.pack(side="left", fill="both", expand=True)

# # Create a frame inside the canvas
# scrollable_frame = tk.Frame(canvas)

# # Add the frame to the canvas using a window
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# # Update the scroll region
# def on_frame_configure(event):
#     canvas.configure(scrollregion=canvas.bbox("all"))

# scrollable_frame.bind("<Configure>", on_frame_configure)

root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title("Scrollable Frame Example")
# root.geometry("400x300")

# # Create a canvas and a scrollbar
# canvas = tk.Canvas(root)
# scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="y")

# # Configure the canvas to work with the scrollbar
# canvas.configure(yscrollcommand=scrollbar.set)
# canvas.pack(side="left", fill="both", expand=True)

# # Create a frame inside the canvas
# scrollable_frame = tk.Frame(canvas)

# # Add the frame to the canvas using a window
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# # Populate the scrollable frame with widgets
# for i in range(30):
#     tk.Label(scrollable_frame, text=f"Item {i+1}").pack()

# # Update the scroll region
# def on_frame_configure(event):
#     canvas.configure(scrollregion=canvas.bbox("all"))

# scrollable_frame.bind("<Configure>", on_frame_configure)

# root.mainloop()
