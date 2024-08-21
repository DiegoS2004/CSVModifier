import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, MULTIPLE
import pandas as pd

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        global data
        data = pd.read_csv(file_path)
        for column in data.columns:
            listbox.insert(tk.END, column)
        messagebox.showinfo("Information", "File loaded successfully!")

def remove_columns():
    selected_indices = listbox.curselection()
    selected_columns = [listbox.get(i) for i in selected_indices]
    global data
    data.drop(columns=selected_columns, inplace=True)
    listbox.delete(0, tk.END)
    for column in data.columns:
        listbox.insert(tk.END, column)
    messagebox.showinfo("Information", "Columns removed successfully!")

def save_file():
    output_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if output_path:
        data.to_csv(output_path, index=False)
        messagebox.showinfo("Information", "File saved successfully!")

app = tk.Tk()
app.title("CSV Column Remover")

load_button = tk.Button(app, text="Load CSV", command=load_file)
load_button.pack(pady=10)

listbox = Listbox(app, selectmode=MULTIPLE, width=50, height=15)
listbox.pack(pady=10)

remove_button = tk.Button(app, text="Remove Selected Columns", command=remove_columns)
remove_button.pack(pady=10)

save_button = tk.Button(app, text="Save CSV", command=save_file)
save_button.pack(pady=10)

app.mainloop()