class CompletedController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["completed"]
        self._bind()

    def _bind(self):
        self.frame.returnHome_btn.config(command=self.returnHome)

    def returnHome(self):
        self.view.switch("home")
