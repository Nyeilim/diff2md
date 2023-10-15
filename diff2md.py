import tkinter as tk
from tkinter import ttk
from uicontrol import *
from entity.component import *

# create main window
root = tk.Tk()
root.title("Text Correction")

# create text box
text_box = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# set layout
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# button style
style = ttk.Style()
style.configure("TButton", padding=5, font=("Arial", 12))

# passed param
comp = Component()

# create button
next_button = ttk.Button(root, text="Next", command=lambda: next_step(comp), style="TButton")
next_button.grid(row=1, column=0, padx=10, pady=10)

process_button = ttk.Button(root, text="Process", command=lambda: process_text(comp), style="TButton")
process_button.grid(row=1, column=0, padx=10, pady=10)
process_button.grid_remove()  # hide after creating, then only see 'next' button when opening

# capsule
comp.text_box = text_box
comp.next_button = next_button
comp.process_button = process_button

# run
root.mainloop()
