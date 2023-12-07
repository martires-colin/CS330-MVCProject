class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        self.frame.getActivity_btn.config(command=self.getActivity)
        self.frame.navigateCompleted_btn.config(command=self.navigateCompleted)

    def getActivity(self):
        print("Controller is getting activity from boredapi ...")
        self.model.activity.setActivity("Test activity")
    
    def navigateCompleted(self):
        print("Switching to completed view ...")
        self.view.switch("completed")

    def update_view(self):   
        self.frame.activity_description.config(text="Test activity")