# import tkinter as tk

# def on_canvas_click(event, canvas_number):
#     print(f"Canvas {canvas_number} clicked at ({event.x}, {event.y})")

# root = tk.Tk()
# root.title("Multiple Canvases")

# frame = tk.Frame(root)
# frame.pack()

# # Create the first canvas
# canvas1 = tk.Canvas(frame, width=200, height=150, bg="white")
# canvas1.pack(side=tk.LEFT)
# canvas1.bind("<Button-1>", lambda event: on_canvas_click(event, 1))

# # Create the second canvas
# canvas2 = tk.Canvas(frame, width=200, height=150, bg="white")
# canvas2.pack(side=tk.LEFT)
# canvas2.bind("<Button-1>", lambda event: on_canvas_click(event, 2))

# root.mainloop()





import tkinter as tk
from tkinter import *
import calendar

window = tk.Tk()
window.title("Task Manager")
window.geometry("785x500")

current_day = "Mon"
current_date = 14
current_month = 11
current_year = 2023

#calendar with 42 blocks
# class Planner():
#     def __init__(self):
#         self.calendar_frame = Frame(window)
#         self.calendar_frame.grid(row = 0, column = 0, rowspan = 7, columnspan = 7, sticky = tk.W + tk.E)
#         day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
#         for i, day in enumerate(day_labels):
#             Label(self.calendar_frame, text = day, width = 12, height = 2, relief = "flat", borderwidth = 0,  bg="white", highlightthickness=0).grid(row = 0, column = i, sticky = tk.E)

#         row = 1
#         column = day_labels.index(current_day)
#         num_days = calendar.monthcalendar(current_year, current_month)
#         for i in range(42): 
#             text = i+1
#             if text > 31:
#                 text = (i - 31) + 1
#             else: 
#                 # canvas = tk.Canvas(self.calendar_frame, width = 9, height = 3, bg="white")
#                 canvas = tk.Canvas(self.calendar_frame, width = 105, height = 85, bg="white", borderwidth = 0)
#                 canvas.grid(row = row, column = column)
#                 canvas.bind("<Button-1>", lambda event: self.on_canvas_click(event, text))

#             column += 1
#             if column == 7: 
#                 row += 1
#                 column = 0

class Planner():
    def __init__(self):
        self.calendar_frame = Frame(window)
        self.calendar_frame.grid(row = 0, column = 0, rowspan = 7, columnspan = 7, sticky = tk.W + tk.E)
        day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(day_labels):
            Label(self.calendar_frame, text = day, width = 12, height = 2, relief = "flat", borderwidth = 0,  bg="white", highlightthickness=0).grid(row = 0, column = i, sticky = tk.E)

        row = 1
        # column = day_labels.index(current_day)
        column = 0

        num_days = calendar.monthcalendar(current_year, current_month) #problem deal with this to display correct date 
        for i in range(42): 
            text = i+1
            if text > 35:
                text = (i - 35) + 1 
            else: 
                # canvas = tk.Canvas(self.calendar_frame, width = 9, height = 3, bg="white")
                bg = "white"
                if column == 0 or column == 6: 
                    bg = "grey"
                canvas = tk.Canvas(self.calendar_frame, width = 105, height = 85, bg=bg, borderwidth = 0)
                canvas.grid(row = row, column = column, sticky="nsew")
                canvas.bind("<Button-1>", lambda event: self.on_canvas_click(event, text))
                #display date on canvas + tasks + special day 
            column += 1
            if column == 7: 
                row += 1
                column = 0
                
    def on_canvas_click(self, event, date):
        print(date)


    def display_info(self, event):
        #check database if the user added sth in a cell if not = add, if so = edit/delete
        pass
        
Planner()      
window.mainloop()


