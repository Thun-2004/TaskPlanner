
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# root = tk.Tk()
# root.title('Treeview demo')
# root.geometry('620x200')

# # define columns
# columns = ('first_name', 'last_name', 'email')

# tree = ttk.Treeview(root, columns=columns, show='headings')

# # define headings
# tree.heading('first_name', text='First Name')
# tree.heading('last_name', text='Last Name')
# tree.heading('email', text='Email')

# # generate sample data
# contacts = []
# for n in range(1, 100):
#     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# # add data to the treeview
# for contact in contacts:
#     tree.insert('', tk.END, values=contact)


# def item_selected(event):
#     for selected_item in tree.selection():
#         item = tree.item(selected_item)
#         record = item['values']
#         # show a message
#         showinfo(title='Information', message=','.join(record))


# tree.bind('<<TreeviewSelect>>', item_selected)

# tree.grid(row=0, column=0, sticky='nsew')

# # add a scrollbar
# scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky='ns')

# # run the app
# root.mainloop()

from fileHandling import FileHandling
import pickle

filehandler = FileHandling()
# filehandler.initialize()
# filehandler.save_data(2024, "January", 1, "data3.pickle", "Sleep", "None", "Home", "12.00AM", "12.30AM", "Yes")
info = filehandler.load_data("data3.pickle")
print(info)
# print(filehandler.get_data())

# data = [{'1': {'note': 'Walk', 'category': 'Exercise', 'location': 'Park', 'start': '01.30AM', 'end': '02.30AM', 'notify_me': 'No'}}]
# print(data[-1][str(len(data))]['start'])

