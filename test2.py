class PopUpWindow(tk.Toplevel):
    def __init__(self, master): 
        super().__init__(master)
        self.geometry("400x300")  # Change according to list of data
        self.popup_window = None  # Initialize popup_window

    def display_table(self, date, month, year): 
        self.title(f"Plan for {month} {date}, {year}")
        table_frame = Frame(self)
        table_frame.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=tk.W + tk.E)
        table = Table()
        table.display_tasks_table(date, month, year, table_frame)
        Button(table_frame, text="Edit", command=lambda: self.return_day_page(date, month, year), width=10).grid(row=2, column=0)

    def return_day_page(self, date, month, year): 
        if self.popup_window and self.popup_window.winfo_exists():
            self.popup_window.destroy()
