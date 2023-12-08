from tkinter import Frame, Label, Button

class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Feeling Bored?")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.activity_description = Label(self, text="")
        self.activity_description.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.getActivity_btn = Button(self, text="Generate Activity", width=15)
        self.getActivity_btn.grid(row=2, column=0, padx=5, pady=10)

        self.completeActivity_btn = Button(self, text="Complete Activity", width=15)
        self.completeActivity_btn.grid(row=2, column=1, padx=5, pady=10)

        self.navigateCompleted_btn = Button(self, text="Completed Activities")
        self.navigateCompleted_btn.grid(row=3, columnspan=2, column=0, padx=10, pady=10)

        self.iscompleted_alert = Label(self, text="")
        self.iscompleted_alert.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
