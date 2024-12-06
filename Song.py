import tkinter as tk
from PIL import Image, ImageTk  # Import the required classes

# Create main window
root = tk.Tk()
root.title("Music Player")
root.geometry("400x500")

# Blocking resizable
root.resizable(width="False", height="False")

# Set the background color to white
root.configure(bg="white")

# Create a Frame to hold the image (with padding on the left and right)
image_frame = tk.Frame(root, bg="white")  # Set the frame background color if needed
image_frame.pack(pady=(0, 20))  # Add padding at the bottom, no padding at the top

# Load an image using Pillow (correct the path)
image_path = r"C:\Users\gupta\Desktop\Music-Player\image.jpg"  # Use raw string for the path
image = Image.open(image_path)  # Open the image

# Resize the image to 400x300
image = image.resize((400, 390))  # Resize image to 400x300 pixels

# Convert it to PhotoImage format for Tkinter
photo = ImageTk.PhotoImage(image)

# Create a Label to display the image and place it inside the frame
image_label = tk.Label(image_frame, image=photo, bg="white")  # Ensure label background matches frame
image_label.pack(padx=20)  # Add horizontal padding (space) around the image, no top/bottom padding

# Start the Tkinter event loop
root.mainloop()
