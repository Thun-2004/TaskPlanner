import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import calendar
from datetime import datetime
import pickle
from abc import ABC, abstractmethod
from config import today, current_year, current_month, current_date, current_day, category_list, time_slot, notify_me
from fileHandling import FileHandling

global num_current_year
global num_current_month
global str_current_month
global num_current_date
global str_current_day
global planner
global file_handler
file_handler = FileHandling()
file_handler.initialize() #add default data to file for first time

num_current_year = current_year
num_current_date = current_date
str_current_month = current_month
num_current_month = datetime.strptime(str_current_month, '%B').month
num_current_date = current_date
str_current_day = current_day

class Planner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Planner")
        self.geometry("900x650")
        self.resizable(width = False, height = False)
        global month
        month = datetime.now().month

        Button(self, text = "+", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 310, y = 5)
        Button(self, text = "Day", width = 3, borderwidth = 0, highlightthickness = 0, command = lambda : self.call_page("Day")).place(x = 380, y = 5)
        Button(self, text = "Week", width = 3, borderwidth = 0, highlightthickness = 0, command = lambda : self.call_page("Week")).place(x = 450, y = 5)
        Button(self, text = "Month", width = 3, borderwidth = 0, highlightthickness = 0, command = lambda : self.call_page("Month")).place(x = 520, y = 5)
        Button(self, text = "<", width = 1, borderwidth = 0, highlightthickness = 0, command = lambda : self.switch(-1)).place(x = 740, y = 30)
        Button(self, text = "Today", width = 3, borderwidth = 0, highlightthickness = 0, command = self.get_current_page).place(x = 780, y = 30)
        Button(self, text = ">", width = 1, borderwidth = 0, highlightthickness = 0, command = lambda : self.switch(1)).place(x = 840, y = 30)
        
        self.date_label = Label(self, text = self.update_date(), font = ("Arial", 30, "bold"))
        self.date_label.place(x = 10, y = 60)
        self.day_label = Label(self, text = current_day, font = ("Arial", 20), borderwidth = 0)
        self.day_label.place(x = 12, y = 97)
        
    
        self.current_page = "Day"
        self.month_page = Month(self)
        self.day_page = Day(self)
        
    def show_page(self, page):
        page.tkraise() 
    
    def call_page(self, page):
        current_date = num_current_date
        current_month = str_current_month
        current_year = num_current_year
        if page == "Day":
            self.current_page = "Day"
            self.date_label.config(text = f"{current_month} {current_date}, {current_year}") #prob: replace with update
            self.day_label.config(text = current_day)
            self.show_page(self.day_page)
        elif page == "Week":
            pass
            # self.show_page(self.week_page)
        elif page == "Month": 
            self.current_page = "Month"
            self.date_label.config(text = f"{current_month} {current_year}")
            self.day_label.config(text = "")
            self.show_page(self.month_page)
            Month.setup_calendar(self.month_page)

    def update_date(self): 
        return f"{current_month} {current_date}, {current_year}"

    def get_current_page(self):
        global current_year
        global current_date
        global current_month
        global current_day
        current_year = int(today.strftime("%Y"))
        current_month = today.strftime("%B")
        current_date = int(today.strftime("%d"))  
        current_day = today.strftime("%A")
        if self.current_page == "Day": 
            self.date_label.config(text = self.update_date())
            self.day_label.config(text = current_day)
            Day.setup_table_frame(self.day_page)
        elif self.current_page == "Week":
            pass
        else: 
            current_month = datetime.now().strftime("%B")
            self.date_label.config(text = f"{current_month} {current_year}")
            self.day_label.config(text = "")
            Month.setup_calendar(self.month_page)
        
    def change_day(self,date, num_month, year): #month should be num
        global current_date
        global current_year
        global current_day
        current_date = date
        current_year = year
        #change month tp real month not number
        current_day = calendar.day_name[calendar.weekday(current_year, num_month, current_date)]
        self.date_label.config(text = self.update_date())
        self.day_label.config(text = current_day)
    
    def switch(self, direction): #current date/year = string 
        global current_date
        global current_month
        global current_day
        global month 
        #october jump to december/ when decrease = october again 
        if self.current_page == "Day":
            if direction > 0: 
                if current_date >= calendar.monthrange(current_year, month)[1]: 
                    current_date = 1
                    month += 1
                    current_month = calendar.month_name[month]
                    current_day = calendar.day_name[calendar.weekday(current_year, month, current_date)]
                else: 
                    current_date += 1
                    current_day = calendar.day_name[calendar.weekday(current_year, month, current_date)]
            else:  
                if current_date == 1: 
                    month -= 1
                    lastmonth = 12 if month == 1 else month 
                    current_date = calendar.monthrange(current_year, lastmonth)[1] #prev month 
                    current_month = calendar.month_name[lastmonth]
                    current_day = calendar.day_name[calendar.weekday(current_year, lastmonth, current_date)]
                else: 
                    current_date -= 1
                    current_day = calendar.day_name[calendar.weekday(current_year, month, current_date)]

            self.date_label.config(text = self.update_date())
            self.day_label.config(text = current_day)
            # Day(self)
            Day.setup_table_frame(self.day_page)

        elif self.current_page == "Week": 
            pass
            #call next page
        elif self.current_page == "Month":
            if direction > 0:
                if 1 <= month <= 11: 
                    month += 1
            elif direction < 0:   
                if 2 <= month <= 12: 
                    month -= 1
            
            current_month = calendar.month_name[month]
            self.date_label.config(text = f"{current_month} {current_year}")
            self.day_label.config(text = "")
            Month.setup_calendar(self.month_page)
        else: 
            pass        
        

class PlannerView(tk.Frame, ABC): 
    def __init__(self, master):
        super().__init__(master)
        self.place(x = 0, y = 120, width = 900, height = 570) #set up frame with specific location
        # self.file_handler = FileHandling()
        # self.file_handler.initialize() #add default data to file for first time
    
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
        self.file_handler = file_handler
        self.leftframe = tk.Frame(self, bg="#D9D9D9")
        self.leftframe.place(x = 10, y = 10, width = 500, height = 420)
        columns = ('Time', 'Note')#note@time
        self.tree = ttk.Treeview(self.leftframe, columns=columns, show = "headings", height=40)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15), rowheigth=20)
        #problem: table heading not change width 
        self.tree.column(0,anchor='center', stretch=tk.NO, width=150)
        self.tree.heading("Time", text="Time")
        self.tree.column(1,anchor='center', stretch=tk.NO, width=320)
        self.tree.heading("Note", text="Note")
        self.content = [] #keep track of content in table)
        ids = self.file_handler.get_daytask_ids(current_date, current_month, current_year)
        if len(ids) > 0:
            for i in range(len(ids)):
                self.add_row_table(current_date, current_month, current_year, self.tree, i)
        
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
        self.rightframe.place(x = 500, y = 10, width = 380, height = 420)
        Button(self.rightframe, text="Add", font = ("Arial", 15), width = 5, height = 2, borderwidth=0, highlightthickness=0, pady = 0, background="#ABBBF0").place(x = 20, y = 20)
        inputframe = tk.Frame(self.rightframe, bg="#ABBBF0")
        inputframe.place(x = 20, y = 50, width = 345, height = 260)
        
        Label(inputframe, text = "Note", font = ("Arial", 15)).place(x = 0, y = 12)
        self.note = tk.Entry(inputframe, width=25) 
        self.note.place(x = 90, y = 10)
        
        Label(inputframe, text = "Category", font = ("Arial", 15)).place(x = 0, y = 42)
        self.category = Collapsible_list.create(self, frame=inputframe, width = 15, datalist=category_list, x = 90, y = 40, canType=True)
        
        Label(inputframe, text = "Time period (From - To)", font = ("Arial", 15)).place(x = 0, y = 70)
        self.start_time = Collapsible_list.create(self, frame=inputframe, width = 7, datalist=time_slot, x = 90, y = 100)
        self.end_time = Collapsible_list.create(self, frame=inputframe, width = 7, datalist=time_slot, x = 200, y = 100)
        
        Label(inputframe, text = "Location", font = ("Arial", 15)).place(x = 0, y = 130)
        self.location = tk.Entry(inputframe, width=25)
        self.location.place(x = 90, y = 130)
        
        Label(inputframe, text = "Notify me", font = ("Arial", 15)).place(x = 0, y = 160)
        self.notify = Collapsible_list.create(self, frame=inputframe, width = 7, datalist=notify_me, x = 90, y = 160)
        
        Button(inputframe, text="Add", font=("Arial", 15), command = self.save_data,  width = 5, borderwidth=0, highlightthickness=0, pady = 10, background="#ABBBF0").place(x = 190, y = 200)
        Button(inputframe, text="Edit", font=("Arial", 15), command = self.edit_data,  width = 5, borderwidth=0, highlightthickness=0, pady = 10, background="#ABBBF0").place(x = 100, y = 200)
        Button(inputframe, text="Delete", font=("Arial", 15), command = self.delete_data,  width = 5, borderwidth=0, highlightthickness=0, pady = 10, background="#ABBBF0").place(x = 10, y = 200)
        
    #content to keep tracke element inside table
    #see where to insert new data
    #delete and edit elements in self.content too
    def add_row_table(self, date, month, year, table, index):
        tasks = self.file_handler.get_day_tasks(date, month, year)
        value = list(tasks[index].values())[0]
        self.content.append(value.get('start') + "-" + value.get('end') + " " + value.get('note') + "@" + value.get('location'))
        ind = 0
        if tasks != None:
            # value = list(tasks[index].values())[0]
            for i in range(len(self.content)):
                if float(self.content[i][:5]) < float(value.get('start')[:4]): 
                    ind = i + 1
            #add info to self.content
            table.insert('', ind, values=(self.content[-1].split(" ")[0], self.content[-1].split(" ")[1]))
        else: 
            table.insert('', tk.END, values=(self.content[-1].split(" ")[0], self.content[-1].split(" ")[1]))

    def edit_row_table(self, time_period, note_info): 
        if self.tree.selection() != (): #incase user click on a blank area of the table
            selected_item = self.tree.selection()[0]
            self.tree.item(selected_item, text="", values = (time_period, note_info))
            #edit self.content
            for i in self.content:
                if i.split(" ")[0] == time_period:
                    self.content[self.content.index(i)] = time_period + " " + note_info
                    break

    def delete_data(self):
        if self.tree.selection()!= (): 
            deleted = self.tree.selection()[0]
            time_period, note_info = self.tree.item(deleted, 'values')
            self.content.remove(time_period + " " + note_info)
            self.tree.delete(deleted)
            print(self.content)
            self.file_handler.delete_data(current_date, current_month, current_year, self.task_id)
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
        if values:  #incase user click on a blank area of the table 
            time_period, note_info = values
            tasks = self.file_handler.get_day_tasks(current_date, current_month, current_year)
            print(tasks)
            self.task_id = ""
            temp_note = ""
            temp_category = ""
            temp_location = ""
            temp_start = ""
            temp_end = ""
            temp_notify = ""
            ids = self.file_handler.get_daytask_ids(current_date, current_month, current_year)
            for i, task in enumerate(tasks): 
                if task[str(ids[i])].get('start') + "-" + task[str(ids[i])].get('end') == time_period and task[str(ids[i])].get('note') + "@" + task[str(ids[i])].get('location') == note_info: 
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
        if self.tree.selection() != ():
            self.file_handler.edit_data(current_date, current_month, current_year, self.task_id, self.note.get(), self.category.get(), self.location.get(), self.start_time.get(), self.end_time.get(), self.notify.get())
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
        elif self.time_to_number(self.start_t) > self.time_to_number(self.end_t): 
            messagebox.showerror("Error", "Start time cannot be later than end time")
        elif self.time_to_number(self.start_t) == self.time_to_number(self.end_t): 
            messagebox.showerror("Error", "Start time cannot be the same as end time")
        elif self.category_info.isspace() or self.location_info.isspace(): 
            messagebox.showerror("Error", "Can't least answer fields as blank") 
        else:
            data = self.file_handler.save_data(int(current_year), current_month, current_date, "data3.pickle", self.note_info, self.category_info, self.location_info, self.start_t, self.end_t, self.notify_info)
            self.file_handler.sort_data_by_time(current_date, current_month, current_year)
            self.content = sorted(self.content, key = lambda x: float(x[:5]))
            self.add_row_table(current_date, current_month, current_year, self.tree, -1)
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

class Table: 
    def display_tasks_table(self,date, month, year, table_frame):
        global file_handler
        columns = ('Time', 'Note')#note@time
        self.tree = ttk.Treeview(table_frame, columns=columns, show = "headings", height=13)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15), rowheigth=20)
        self.tree.column(0,anchor='center', stretch=tk.NO, width=150)
        self.tree.heading("Time", text="Time")
        self.tree.column(1,anchor='center', stretch=tk.NO, width=234)
        self.tree.heading("Note", text="Note")
        self.content = []
        
        #why task & id == None
        print("id task from table")
        ids = file_handler.get_daytask_ids(date, month, year)
        if len(ids) > 0:
            for i in range(len(ids)):
                print(ids[i])
                self.add_row_table(date, month, year, self.tree, i)
     
        self.tree.grid(row=0, column=0, sticky='nsew')
        # add a scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command= self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
    def add_row_table(self, date, month, year, table, index):
        global file_handler
        tasks = file_handler.get_day_tasks(date, month, year)
        value = list(tasks[index].values())[0]
        self.content.append(value.get('start') + "-" + value.get('end') + " " + value.get('note') + "@" + value.get('location'))
        ind = 0
        if tasks != None:
            for i in range(len(self.content)):
                if float(self.content[i][:5]) < float(value.get('start')[:4]): 
                    ind = i + 1
            table.insert('', ind, values=(self.content[-1].split(" ")[0], self.content[-1].split(" ")[1]))
        else: 
            table.insert('', tk.END, values=(self.content[-1].split(" ")[0], self.content[-1].split(" ")[1]))
        
        
class Month(PlannerView): 
    def __init__(self, master):
        super().__init__(master)
        self.initialize_ui()
        current_year = int(today.strftime("%Y"))
        current_date = int(today.strftime("%d"))  
        # self.planner.change_day(current_date, num_month, current_year)

    def initialize_ui(self): 
        self.setup_calendar()
        
    def setup_calendar(self): 
        # self.planner = planner
        self.file_handler = file_handler
        self.calendar_frame = Frame(self)
        self.calendar_frame.place(x = 0, y = 10, width = 900, height = 570)
        day_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(day_labels):
            day = Label(self.calendar_frame, text = day, width = 20, height = 2, relief = "flat", borderwidth = 0,  bg="white", highlightthickness=0)
            day.place(x = i*120, y = 0)
        day = day_labels.index(current_day[:3])

        #prep data 
        num_month = datetime.strptime(current_month, '%B').month
        num_days_prev = calendar.monthcalendar(2023, num_month - 1) if num_month != 1 else calendar.monthcalendar(2022, 12)
        num_days_current = calendar.monthcalendar(2023, num_month)
        num_days_next = calendar.monthcalendar(2023, num_month + 1) if num_month != 12 else calendar.monthcalendar(2024, 1)
        
        count_prev = num_days_current[0].count(0)
        end = []
        for row in range(len(num_days_current)): 
            for col in range(len(num_days_current[row])): 
                if num_days_current[row][col] == 0 and row == 0: 
                    num_days_current[row][col] = num_days_prev[len(num_days_prev) - 1][col]
                elif num_days_current[row][col] == 0: 
                    num_days_current[row][col] = num_days_next[0][col]
                    end.append((row, col))
        if end == []:
            num_days_current.append(num_days_next[0])
        elif len(num_days_current) < 6: 
            num_days_current.append(num_days_next[1])
    
        #display calendar
        column_x = 0
        row_y = 32
        for row in range(len(num_days_current)): 
            for col in range(len(num_days_current[row])): 
                num_month = datetime.strptime(current_month, '%B').month
                prev_month = num_month - 1 if num_month != 1 else 12
                next_month = num_month + 1 if num_month != 12 else 1
                bg = "white"
                if column_x == 525 or column_x == 630: 
                    bg = "#c8c8c8"
                canvas = tk.Canvas(self.calendar_frame, width = 130, height = 80, bg=bg, borderwidth = 0)
                canvas.place(x=127*col, y=row_y)
                #indicate that it's today
                if num_days_current[row][col] == num_current_date and current_month == str_current_month and current_year == 2023: 
                    canvas.create_oval(100, 8, 122, 28, outline="#F87A5F",fill="#F87A5F")
                canvas.create_text(120, 10, text=str(num_days_current[row][col]), font=("Arial", 15, "bold"), anchor="ne")
                
                #change month
                if (row+1)*(col+1) <= count_prev: #2
                    num_month = prev_month
                for i in end: 
                    if (row, col) == i: 
                        num_month = next_month
                self.display_cellinfo(canvas, num_days_current[row][col], calendar.month_name[num_month], current_year)                
                canvas.bind("<Button-1>", lambda event, date=num_days_current[row][col], month=num_month, year=current_year: self.on_canvas_click(event, date, month, year))
                column_x += 105
                if column_x > 700:
                    row_y += 80
                    column_x = 0 
    
    def on_canvas_click(self, event, date, month, year): #display info as messagebox
        print(f"Clicked on {date} {month} {year}")
        x, y = event.x, event.y
        if 110 <= x <= 130 and 0 <= y <= 30:
            self.return_day_page(date, month, year)
            # self.planner.update_date() #prob: update date not working

        else: 
            child_window = PopUpWindow(self)
            child_window.display_table(date, month, year)

    def display_cellinfo(self, canvas, date, month, year): #display info on canvas
        tasks = self.file_handler.get_day_tasks(date, month, year)
        
        if tasks != None:
            for i, task in enumerate(tasks):
                note = list(task.values())[0].get('note')
                start = list(task.values())[0].get('start')
                canvas.create_text(50, 50 + i*12, text= f"- {note} {start}", font=("Arial", 10))
                if i == 1:
                    break
    def return_day_page(self,date, month, year): 
        # global planner
        # self.planner.change_day(date, 11, year)
        # self.planner.call_page("Day")
        pass
      
    
    def save_data(self): 
        pass

class PopUpWindow(tk.Toplevel):
    def __init__(self, master): 
        super().__init__(master)
        self.geometry("400x260") #change according to list of data
        # self.planner = planner
        
    def display_table(self, date, month, year): 
        self.title(f"Plan for {month} {date}, {year}")
        table_frame = Frame(self)
        table_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = tk.W + tk.E)
        table = Table()
        table.display_tasks_table(date, month, year, table_frame)
       
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
 