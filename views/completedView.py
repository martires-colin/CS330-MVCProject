from tkinter import Frame, Label, Entry, Button


class CompletedView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="List of completed activities")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.returnHome_btn = Button(self, text="Return to home page")
        self.returnHome_btn.grid(row=5, column=1, sticky="w")