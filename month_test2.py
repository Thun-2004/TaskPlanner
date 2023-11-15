import tkinter as tk
import calendar

class CalendarWidget(tk.Frame):
    def __init__(self, parent, year, month, **kwargs):
        super().__init__(parent, **kwargs)

        self.cal_frame = tk.Frame(self)
        self.cal_frame.pack(side="top", fill="x")

        self.redraw(year, month)

    def redraw(self, year, month):
        '''Redraws the calendar for the given year and month'''
        for child in self.cal_frame.winfo_children():
            child.destroy()

        # day of the week headings
        for col, day in enumerate(("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")):
            label = tk.Label(self.cal_frame, text=day)
            label.grid(row=0, column=col, sticky="nsew")

        # buttons for each day
        cal = calendar.monthcalendar(year, month)
        for row, week in enumerate(cal):
            for col, day in enumerate(week):
                text = "" if day == 0 else day
                state = "normal" if day > 0 else "disabled"
                cell = tk.Button(self.cal_frame, text=text, state=state, command=lambda day=day: self.set_day(day))
                cell.grid(row=row+1, column=col, sticky="nsew")

    def set_day(self, num):
        print(f"you selected day {num}")
        
root = tk.Tk()
c = CalendarWidget(root, year=2022, month=4, bd=2, relief="groove")
c.pack(padx=4, pady=4)

root.mainloop()