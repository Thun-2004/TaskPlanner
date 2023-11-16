import tkinter as tk

class ClickHandler:
    def __init__(self, root):
        self.root = root
        self.click_count = 0

        self.button = tk.Button(root, text="Click Me", command=self.handle_click)
        self.button.pack()

        self.button.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        self.click_count += 1

        # Schedule a function to run after a short delay (e.g., 200 milliseconds)
        self.root.after(200, self.check_click_count)

    def handle_click(self):
        if self.click_count == 1:
            print("Single click")
        elif self.click_count == 2:
            print("Double click")

    def check_click_count(self):
        # Reset click count after a short delay
        self.click_count = 0

if __name__ == "__main__":
    root = tk.Tk()
    click_handler = ClickHandler(root)
    root.mainloop()
