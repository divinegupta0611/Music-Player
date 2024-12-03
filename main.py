import requests
from tkinter import Tk
import tkinter as tk
import pygame
import os

#create main window
root = tk.Tk()
root.title("Tkinter frame example")
root.geometry("400x500")

# Blocking resizable
root.resizable(width="False",height="False")

# Create a Label with the text "Music Player"
label = tk.Label(root, text="Music Player", font=("Helvetica", 24, "bold"), fg="black")
label.pack(pady=10)  # Add vertical padding

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
