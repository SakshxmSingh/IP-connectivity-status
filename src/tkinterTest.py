import tkinter as tk
from tkinter import ttk

def create_table(root):
    # Creating a Table Frame
    table_frame = ttk.Frame(root)
    table_frame.pack()

    # Creating Table Headers
    headers = ['Column 1', 'Column 2', 'Column 3']
    for col, header in enumerate(headers):
        label = ttk.Label(table_frame, text=header, relief=tk.RIDGE)
        label.grid(row=0, column=col, sticky=tk.NSEW)

    # Creating Table Data
    data = [
        ['Data 1', 'Data 2', 'Data 3'],
        ['Data 4', 'Data 5', 'Data 6'],
        ['Data 7', 'Data 8', 'Data 9']
    ]

    for row, row_data in enumerate(data):
        for col, cell_data in enumerate(row_data):
            label = ttk.Label(table_frame, text=cell_data, relief=tk.RIDGE)
            label.grid(row=row + 1, column=col, sticky=tk.NSEW)

    # Configuring Grid Weights
    table_frame.columnconfigure((0, 1, 2), weight=1)
    table_frame.rowconfigure(tuple(range(len(data) + 1)), weight=1)

# Creating the Main Window
root = tk.Tk()
root.title("Table Window")
root.geometry("500x500")

# Creating the Table
create_table(root)

# Running the Main Loop
root.mainloop()
