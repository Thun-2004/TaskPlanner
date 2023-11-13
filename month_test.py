import tkinter as tk
from tkinter import *
import calendar

window = tk.Tk()
window.title("Task Manager")
window.geometry("785x500")


#calendar with 42 blocks
class Planner():
    def __init__(self):
        #prev menubar 
        # menubar = tk.Menu()
        # day = tk.Menu(menubar, tearoff=False)
        # menubar.add_cascade(menu=day, label="Day")
        # week = tk.Menu(menubar, tearoff=False)
        # menubar.add_cascade(menu=week, label="Week")
        # month = tk.Menu(menubar, tearoff=False)
        # menubar.add_cascade(menu=month, label="Month")
        # window.config(menu=menubar)
    
        #menubar
        menu = Frame(window)
        menu.grid(row = 0, column = 2, rowspan = 1, columnspan = 7, sticky= tk.W+tk.E )
        Button(menu,text = "+", width = 3).grid(row = 1, column = 0)
        Button(menu,text = "Day", width = 3).grid(row = 1, column = 1)
        Button(menu,text = "Week", width = 3).grid(row = 1, column = 2)
        Button(menu,text = "Month", width = 3).grid(row = 1, column = 3)

        Button(menu, text = "<", width = 2, borderwidth = 0).grid(row = 1, column = 5, sticky = tk.E)
        Button(menu, text = "Today", width = 3, borderwidth = 0).grid(row = 1, column = 6, sticky = tk.E)
        Button(menu, text = ">", width = 2, borderwidth = 0).grid(row = 1, column = 7, sticky = tk.E)
        
        #calendar
        current_date = "August" + " 2023 " + "BCE"
        Label(window, text = current_date, font=("Arial", 25, "bold")).grid(row = 1, column = 0, rowspan = 2, columnspan = 7, padx = 3, sticky = tk.W)
        calendar_frame = Frame(window)
        calendar_frame.grid(row = 4, column = 0, rowspan = 6, columnspan = 7, sticky= tk.W+tk.E )

        #calendar day labels
        day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(day_labels):
            Label(calendar_frame, text = day, width = 7, height = 2, relief = "flat", borderwidth = 0, highlightthickness=0).grid(row = 3, column = i, sticky = tk.E)

        row = 4 
        column = 0
        days = calendar.monthcalendar(2023, 8)
        for i in range(42): 
            #fucking text problem
            text=i+1
            if text > 31:
                text = (i - 31) + 1
            if i == 11:
                Button(calendar_frame,text=str(text) + "\n-Trip with homies\n-Mountain bike", width = 9, height = 3, relief = "flat", borderwidth = 0, highlightthickness=0, anchor="ne", bg= "#D9D9D9", command = self.display_info).grid(row = row, column = column)
            else:
                Button(calendar_frame, text=text, width = 9, height = 3, relief = "flat", borderwidth = 0, highlightthickness=0, anchor="ne", bg= "#D9D9D9", command = self.display_info).grid(row = row, column = column)
            #button display info and add info
            column += 1
            if column == 7:
                row += 1
                column = 0
        canvas = tk.Canvas(calendar_frame, width = 200, height = 100)
        canvas.create_rectangle(50, 50, 200, 150, outline="black", fill="red")

        
    def display_info(self, event):
        #check database if the user added sth in a cell if not = add, if so = edit/delete
        pass
        
Planner()      
window.mainloop()