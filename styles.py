from tkinter import ttk
from config import BACKGROUND_COLOR  # Import the background color constant from config


def configure_styles():
    # Create a ttk.Style instance to manage styles for the tkinter widgets
    style = ttk.Style()
    
    # Configure the background color for frames
    style.configure('TFrame', background=BACKGROUND_COLOR)
    
    # Configure the background color for labels
    style.configure('TLabel', background=BACKGROUND_COLOR)
    
    # Configure the background color for entry widgets
    style.configure('TEntry', background=BACKGROUND_COLOR)
