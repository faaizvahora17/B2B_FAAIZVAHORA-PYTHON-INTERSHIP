import os
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt


def format_size(size_bytes):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(size_bytes)

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def get_folder_size(folder_path):
    total_size = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            try:
                total_size += os.path.getsize(os.path.join(root, file))
            except:
                pass

    return total_size


def analyze_folder():

    folder_path = filedialog.askdirectory()

    if not folder_path:
        return

    text_box.delete(1.0, tk.END)

    total = get_folder_size(folder_path)

    text_box.insert(tk.END,
                    f"\t\t\t\t\t\t\t\t\t\tFolder:-\t{folder_path}\n\n")
    text_box.insert(tk.END,
                    f"\t\t\t\t\t\t\t\t\t\tTotal Folder Size:- {format_size(total)}\n")

    text_box.insert(tk.END,"\n"+"-" * 180+"\n")

    text_box.insert(tk.END,"\t\t\t\t\t\tFOLDER/FILE")
    text_box.insert(tk.END,"\t\t\t\t\tFILE-NAME")
    text_box.insert(tk.END,"\t\t\t\t\t\tSIZES")

    text_box.insert(tk.END,"\n"+"-" * 180+"\n")
    

    subfolder_sizes = {}

    for item in os.listdir(folder_path):

        item_path = os.path.join(folder_path,item)

        if os.path.isdir(item_path):

            size = get_folder_size(item_path)
            subfolder_sizes[item] = size

            text_box.insert(
                tk.END,
                f"\t\t\t\t\t\t<FOLDER>\t\t\t\t{item}\t\t\t\t\t\t\t{format_size(size)}\n"
            )

        elif os.path.isfile(item_path):

            size = os.path.getsize(item_path)

            text_box.insert(
                tk.END,
                f"\t\t\t\t\t\t<FILE>\t\t\t\t{item}\t\t\t\t\t\t\t{format_size(size)}\n"
            )

    text_box.insert(tk.END,"\n"+"-" * 180+"\n")

    text_box.insert(tk.END,"\t\t\t\t\t\t\t\t\t\t\t\tThankyou")

    text_box.insert(tk.END,"\n"+"-" * 180+"\n")


    # Pie Chart
    # if subfolder_sizes:

        # plt.figure(figsize=(7,7))

        # plt.pie(
        #     subfolder_sizes.values(),
        #     labels=subfolder_sizes.keys(),
        #     autopct="%1.1f%%"
        # )

        # plt.title("Subfolder Size Distribution")
        # plt.show()



# GUI Window

root = tk.Tk()

root.title("Folder Size Analyzer")
root.geometry("1000x1200")


title = tk.Label(
    root,
    text="Folder Size Analyzer",
    font=("Arial",20,"bold","italic")
)

title.pack(pady=10)


button = tk.Button(
    root,
    text="Select Folder",
    command=analyze_folder,
    font=("Arial",14),
    width=20,
    bg="red"
)

button.pack(pady=10)


text_box = tk.Text(
    root,
    fg="white",
    height=100,
    width=200,
    bg="blue"
)

text_box.pack(padx=10,pady=10)


root.mainloop()