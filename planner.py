import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import calendar
from datetime import datetime
import pickle
from abc import ABC, abstractmethod
from config import *
from fileHandling import FileHandling

#fix prepare data for table 
#list : fix table(load and display data to table)
#add/edit/delete function workd
#change next day works

class Planner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Planner")
        self.geometry("785x500")
        self.resizable(width = False, height = False)
    
        Button(self,text = "+", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 270, y = 5)
        Button(self,text = "Day", width = 3, borderwidth = 0, highlightthickness = 0, command=self.call_day).place(x = 340, y = 5)
        Button(self,text = "Week", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 410, y = 5)
        Button(self,text = "Month", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 480, y = 5)
        Button(self, text = "<", width = 1, borderwidth = 0, highlightthickness = 0).place(x = 630, y = 20)
        Button(self, text = "Today", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 670, y = 20)
        Button(self, text = ">", width = 1, borderwidth = 0, highlightthickness = 0).place(x = 730, y = 20)
        
        self.today = datetime.now()
        self.date = self.today.strftime("%B %d, %Y")
        Label(self, text = self.date, font = ("Arial", 25, "bold")).place(x = 10, y = 45)
        Label(self, text = self.today.strftime("%A"), font = ("Arial", 20)).place(x = 10, y = 72)
        
        #default setting
        if current_page == "Day":
            self.dayframe = Day(self)
        
    def call_day(self):
        self.dayframe = Day(self)  # Create Day frame   
        global current_page
        current_page = "Day"

class PlannerView(tk.Frame, ABC): 
    def __init__(self, master):
        super().__init__(master)
        self.place(x = 0, y = 100, width = 785, height = 490) #set up frame with specific location
    
    @abstractmethod
    def display(self): 
        pass
    
    @abstractmethod
    def save_data(self): 
        pass
        
class Day(PlannerView): 
    def __init__(self, master): 
        super().__init__(master)
        # self.place(x = 0, y = 100, width = 785, height = 490) #set up frame iwht specific location 
        self.display()
        
    def display(self):
        tableframe = tk.Frame(self, bg="grey")
        tableframe.place(x = 0, y = 10, width = 445, height = 900)
        
        #problem table : load data to table 
        leftframe = tk.Frame(self, bg="#D9D9D9")
        leftframe.place(x = 10, y = 10, width = 420, height = 900)
        columns = ('Time', 'Note')#note@time
        tree = ttk.Treeview(leftframe, columns=columns, show = "headings")
        tree.heading("Time", text="Time")
        tree.heading("Note", text="Note")
        
        #problme here: load data failed cuz file has no data yet 
        contact = []
        file_handler = FileHandling()
        tasks = file_handler.get_day_task("17", "10", "2023")
        count = 0
        for task in tasks: 
            count += 1
            contact.append((task[str(count)]['start'] + " - " + task[str(count)]['end'], task[str(count)]['note'] + "@" + task[str(count)]['location']))
        
        for task in tasks:
            tree.insert('', tk.END, values=contact)
            
        #adjust here 
        tree.bind('<<TreeviewSelect>>', self.item_selected)
        tree.grid(row=0, column=0, sticky='nsew')
        # add a scrollbar
        scrollbar = ttk.Scrollbar(leftframe, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        #input frame
        rightframe = tk.Frame(self, bg="#D9D9D9")
        rightframe.place(x = 444, y = 10, width = 340, height = 900)
        Button(rightframe, text="add", font = ("Arial", 15), width = 5, height = 2, borderwidth=0, highlightthickness=0, pady = 0, background="#ABBBF0").place(x = 20, y = 20)
        inputframe = tk.Frame(rightframe, bg="#ABBBF0")
        inputframe.place(x = 20, y = 50, width = 300, height = 260)
        
        Label(inputframe, text = "Note", font = ("Arial", 15)).place(x = 0, y = 12)
        self.note = tk.Entry(inputframe, borderwidth = 1) #20 15 15
        self.note.place(x = 90, y = 10)
        
        Label(inputframe, text = "Category", font = ("Arial", 15)).place(x = 0, y = 42)
        self.category = Collapsible_list.create(self, frame=inputframe, width = 15, datalist=category_list, x = 90, y = 40, canType=True)
        
        Label(inputframe, text = "Time period (From - To)", font = ("Arial", 15)).place(x = 0, y = 70)
        self.start_time = Collapsible_list.create(self, frame=inputframe, width = 7, datalist=time_slot, x = 90, y = 100)
        self.end_time = Collapsible_list.create(self, frame=inputframe, width = 7, datalist=time_slot, x = 200, y = 100)
        
        Label(inputframe, text = "Location", font = ("Arial", 15)).place(x = 0, y = 130)
        self.location = tk.Entry(inputframe, width = 15, borderwidth = 1)
        self.location.place(x = 90, y = 130)
        
        Label(inputframe, text = "Notify me", font = ("Arial", 15)).place(x = 0, y = 160)
        self.notify = Collapsible_list.create(self, frame=inputframe, width = 7, datalist=notify_me, x = 90, y = 160)
        
        Button(inputframe, text="Save", font=("Arial", 15), command = self.save_data,  width = 5, borderwidth=0, highlightthickness=0, pady = 10, background="#ABBBF0").place(x = 190, y = 200)
                 
    #help add if condition : if the time_slot has already existed, then show msgbox whether to replace or not
    def item_selected(self, event, tree):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            showinfo(title="Information", message=",".join(record))
            
    
    def save_data(self): 
        self.note_info = self.note.get()
        self.category_info= self.category.get()
        self.notify_info = self.notify.get()
        self.start_t = self.start_time.get()
        self.end_t = self.end_time.get()
        self.location_info = self.location.get()
        file_handler = FileHandling()
        data = file_handler.FileHandling.save_data("data.pickle", self.note_info, self.category_info, self.location_info, self.start_t, self.end_t, self.notify_info)
        self.clear()
    
    def clear(self): #clear combobox
        self.note.delete(0, 'end')
        self.category.set('')
        self.location.delete(0, 'end')
        self.start_time.set('')
        self.end_time.set('')
        self.notify.set('')
        
class Collapsible_list: 
    def create(self, frame, width, datalist, row=None, column=None, x=None, y=None, canType = False):
        data = tk.StringVar()
        data_combobox = ttk.Combobox(frame, width=width, textvariable=data)
        data_combobox['value'] = datalist
        if canType == False: 
            data_combobox['state'] = 'readonly'
        data_combobox.place(x=x, y=y)
        return data

class InvalidValueError(Exception): 
    pass

if __name__ == "__main__":
    planner = Planner()
    planner.mainloop()
    