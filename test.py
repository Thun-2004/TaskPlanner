
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

# data = [
#             {
#                 '1' : {
#                     'note' : "note", 
#                     'category' : "category",
#                     'location' : "location",
#                     'start' : "start_t",
#                     'end' : "end_t",
#                     'notify_me' : "notify_result"
#                 }
#             }, 
#             {
#                 '2' : {
#                     'note' : "note2", 
#                     'category' : "category2",
#                     'location' : "location2",
#                     'start' : "01.00AM",
#                     'end' : "02.00AM",
#                     'notify_me' : "notify_result2"
#                 }
#             }
# ]

#sort start time 
#reassign id according to start time 
#save date 

data = [         
    {
        '1' : {
            'note' : "note", 
            'category' : "category",
            'location' : "location",
            'start' : "11.00AM",
            'end' : "end_t",
            'notify_me' : "notify_result"
        },
        '2' : {
            'note' : "note", 
            'category' : "category",
            'location' : "location",
            'start' : "01.00AM",
            'end' : "end_t",
            'notify_me' : "notify_result"
        }
    }
]

sorted_data = []
times = []
for i in data:
    for info in i.values(): 
        times.append(float(info.get('start')[:4]))
times = sorted(times)
for i in data: 
    for info in i.values(): 
        for n, time in enumerate(times): 
            if float(info.get('start')[:4]) == time:
                found = {str(n + 1) : info}
                sorted_data.insert(n, found)
# for i in sorted_data:
    #key: list(i.keys())[0]
    #value: i.get(list(i.keys())[0]).get('note')
    # print(list(i.keys())[0])         
                
# print(sorted_data)

# from datetime import datetime

# current_month = datetime.now().month
# print(current_month)
import calendar
from datetime import datetime
y = 2023
m = 11
ans = calendar.monthrange(y, m)[1]
month = datetime.now().month
current_day = calendar.day_name[calendar.weekday(y, m, 11)]


content = {"01.00AM - 01.30AM ggggg@gg", "00.00AM - 01.30AM ggggg@gg"}
content = sorted(content, key=lambda x: float(x[:5]))


# print(content)
# print(calendar.month_name[11])

num_days_prev = calendar.monthcalendar(2023, 10)
num_days_current = calendar.monthcalendar(2023, 11)
num_days_next = calendar.monthcalendar(2023, 12)

# print(num_days_prev)
# print(num_days_current)
# print(num_days_next)

current_month = calendar.monthcalendar(2024, 1)
# 

# from fileHandling import FileHandling
from planner_test2 import file_handler
tasks = file_handler.get_day_tasks(16, "November", 2023)
data = file_handler.get_data()
print(tasks)
print(data)