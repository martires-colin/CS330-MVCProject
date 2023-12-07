from tkinter import Frame, Label, Button

class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Feeling Bored?")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.activity_description = Label(self, text="")
        self.activity_description.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.getActivity_btn = Button(self, text="Nah, give me something different")
        self.getActivity_btn.grid(row=2, column=0, padx=10, pady=10)

        self.navigateCompleted_btn = Button(self, text="Completed Activities")
        self.navigateCompleted_btn.grid(row=3, column=0, padx=10, pady=10)