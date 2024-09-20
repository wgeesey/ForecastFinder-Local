from tkinter import ttk
from config import BACKGROUND_COLOR


def configure_styles():
    style = ttk.Style()
    style.configure('TFrame', background=BACKGROUND_COLOR)
    style.configure('TLabel', background=BACKGROUND_COLOR)
    style.configure('TEntry', background=BACKGROUND_COLOR)
