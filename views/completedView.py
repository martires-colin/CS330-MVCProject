from tkinter import Frame, Label, Entry, Button


class CompletedView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="List of completed activities")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Display list of completed activities here
        # self.activity_description = Label(self, text="")
        # self.activity_description.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.returnHome_btn = Button(self, text="Return to home page")
        self.returnHome_btn.grid(row=2, column=0, padx=10, pady=10)
