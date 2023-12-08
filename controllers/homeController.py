import requests

class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self.frame.activity_description.config(text=self.model.activity.activity_description)
        self._bind()

    def _bind(self):
        self.frame.getActivity_btn.config(command=self.getActivity)
        self.frame.navigateCompleted_btn.config(command=self.navigateCompleted)

    def getActivity(self):
        response = requests.get("https://www.boredapi.com/api/activity/")
        data = response.json()
        self.model.activity.setActivity(data['activity'])
    
    def navigateCompleted(self):
        self.view.switch("completed")

    def update_view(self):   
        self.frame.activity_description.config(text=self.model.activity.activity_description)