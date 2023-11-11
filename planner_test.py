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
        self.file_handler = FileHandling()
        self.file_handler.initialize() #add default data to file for first time
    
    @abstractmethod
    def initialize_ui(self): 
        pass
    
    @abstractmethod
    def save_data(self): 
        pass
        
class Day(PlannerView):
    def __init__(self, master):
        super().__init__(master)
        self.initialize_ui()

    def initialize_ui(self): 
        self.setup_table_frame()
        self.setup_input_frame()
        
    def setup_table_frame(self):
        self.leftframe = tk.Frame(self, bg="#D9D9D9")
        self.leftframe.place(x = 10, y = 10, width = 460, height = 900)
        columns = ('Time', 'Note')#note@time
        self.tree = ttk.Treeview(self.leftframe, columns=columns, show = "headings")
        
        #problem: table heading not change width 
        self.tree.column(0,anchor='center', stretch=tk.NO, width=200)
        self.tree.heading("Time", text="Time")
        self.tree.column(1,anchor='center', stretch=tk.NO)
        self.tree.heading("Note", text="Note")
        
        # tasks = self.file_handler.get_day_tasks(11, "November", 2023)
        # if tasks != None:
        #     for i in range(len(tasks)):
        #         self.add_row_table(11, "November", 2023, self.tree, i)
                
        ids = self.file_handler.get_daytask_ids(11, "November", 2023)
        if len(ids) > 0:
            for i in range(len(ids)):
                self.add_row_table(11, "November", 2023, self.tree, i)
            
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        self.tree.bind('<ButtonRelease-1>', self.onclick_to_edit)
        
        self.tree.grid(row=0, column=0, sticky='nsew')
        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.leftframe, orient=tk.VERTICAL, command= self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
    def setup_input_frame(self): 
        #input frame
        self.rightframe = tk.Frame(self, bg="#D9D9D9")
        self.rightframe.place(x = 444, y = 10, width = 340, height = 900)
        Button(self.rightframe, text="add", font = ("Arial", 15), width = 5, height = 2, borderwidth=0, highlightthickness=0, pady = 0, background="#ABBBF0").place(x = 20, y = 20)
        inputframe = tk.Frame(self.rightframe, bg="#ABBBF0")
        inputframe.place(x = 20, y = 50, width = 300, height = 260)
        
        Label(inputframe, text = "Note", font = ("Arial", 15)).place(x = 0, y = 12)
        self.note = tk.Entry(inputframe, borderwidth = 1) 
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
        Button(inputframe, text="Edit", font=("Arial", 15), command = self.edit_data,  width = 5, borderwidth=0, highlightthickness=0, pady = 10, background="#ABBBF0").place(x = 100, y = 200)
        Button(inputframe, text="Delete", font=("Arial", 15), command = self.delete_data,  width = 5, borderwidth=0, highlightthickness=0, pady = 10, background="#ABBBF0").place(x = 10, y = 200)

    def add_row_table(self, date, month, year, table, index):
        tasks = self.file_handler.get_day_tasks(date, month, year)
        if tasks != None:   
            table.insert('', tk.END, values=(tasks[index][str(len(tasks))]['start'] + " - " + tasks[index][str(len(tasks))]['end'], tasks[index][str(len(tasks))]['note'] + "@" + tasks[index][str(len(tasks))]['location']))
    # def add_row_table(self, date, month, year, table, id):
    #     tasks = self.file_handler.get_day_tasks(date, month, year)
    #     for task in tasks:   
    #         for key, value in task.items():
    #             if key == str(id):
    #                 table.insert('', tk.END, values=(task[key].get('start') + " - " + task[key].get('end'), task[key].get('note') + "@" + task[key].get('location')))
            
    def edit_row_table(self, time_period, note_info): 
        selected_item = self.tree.selection()[0]
        self.tree.item(selected_item, text="", values = (time_period, note_info))
    
    def delete_data(self):
        deleted = self.tree.selection()[0]
        self.tree.delete(deleted)
        self.file_handler.delete_data(2023, "November", 11, self.task_id)
        self.clear()
        
    #problem add if condition : if the time_slot has already existed, then show msgbox whether to replace or not
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            showinfo(title="Information", message=",".join(record))
    
    #return all info and change data on treeview and pickle when click edit 
    def onclick_to_edit(self, event): 
        #when user click on cell -> return time-period and note_info from table
        #match with self.data with task_id n return all info to display on input boxes
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, 'values')
        if values: 
            values = values #problem: what if value = None
        time_period, note_info = values
        tasks = self.file_handler.get_day_tasks(11, "November", 2023)
        print(tasks)
        self.task_id = ""
        temp_note = ""
        temp_category = ""
        temp_location = ""
        temp_start = ""
        temp_end = ""
        temp_notify = ""
        #problem when [{}, {....}]
        ids = self.file_handler.get_daytask_ids(11, "November", 2023)
        for i, task in enumerate(tasks): 
            if task[str(ids[i])].get('start') + " - " + task[str(ids[i])].get('end') == time_period and task[str(ids[i])].get('note') + "@" + task[str(ids[i])].get('location') == note_info: 
                self.task_id = str(ids[i])
                temp_note = task[str(ids[i])].get('note')
                temp_category = task[str(ids[i])].get('category')
                temp_location = task[str(ids[i])].get('location')
                temp_start = task[str(ids[i])].get('start')
                temp_end = task[str(ids[i])].get('end')
                temp_notify = task[str(ids[i])].get('notify_me')
                break
        #return old info from task_id 
        self.note.insert(0, temp_note)
        self.category.set(temp_category)
        self.location.insert(0, temp_location)
        self.start_time.set(temp_start)
        self.end_time.set(temp_end)
        self.notify.set(temp_notify)
        
    #when edit is clicked -> save data to pickle with the same id , change data on treeview
    def edit_data(self): 
        #problem: task_id shouldn't be self
        self.file_handler.edit_data(2023, "November", 11, self.task_id, self.note.get(), self.category.get(), self.location.get(), self.start_time.get(), self.end_time.get(), self.notify.get())
        time_period = self.start_time.get() + " - " + self.end_time.get()
        note_info = self.note.get() + "@" + self.location.get()
        self.edit_row_table(time_period, note_info)
        self.clear()
    
    def save_data(self): 
        self.note_info = self.note.get() 
        self.category_info= self.category.get() 
        self.notify_info = self.notify.get()
        self.start_t = self.start_time.get()
        self.end_t = self.end_time.get()
        self.location_info = self.location.get()
        if self.note_info == "" or self.category_info == "" or self.notify_info == "" or self.start_t == "" or self.end_t == "" or self.location_info == "":
            messagebox.showerror("Error", "Please fill in all the information")
        #problem: limit range of time not done
        elif self.time_to_number(self.start_t) > self.time_to_number(self.end_t): 
            messagebox.showerror("Error", "Start time cannot be later than end time")
        elif self.time_to_number(self.start_t) == self.time_to_number(self.end_t): 
            messagebox.showerror("Error", "Start time cannot be the same as end time")
        elif self.category_info.isspace() or self.location_info.isspace(): 
            messagebox.showerror("Error", "Can't least answer fields as blank") 
        else:
            data = self.file_handler.save_data(int(current_year), current_month, 11, "data3.pickle", self.note_info, self.category_info, self.location_info, self.start_t, self.end_t, self.notify_info)
            # info = self.file_handler.load_data("data3.pickle")
            # print(info)
            self.add_row_table(11, "November", 2023, self.tree, -1)
            self.clear()
            
    def clear(self): #clear combobox
        self.note.delete(0, 'end')
        self.category.set('')
        self.location.delete(0, 'end')
        self.start_time.set('')
        self.end_time.set('')
        self.notify.set('')
        
    def time_to_number(self, time): 
        return float(time[:len(time)-2])
        
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
    