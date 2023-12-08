import requests
from mongodb.mongodb_config import *

class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self.frame.activity_description.config(text=self.model.activity.activity_description)
        self._bind()

    def _bind(self):
        self.frame.getActivity_btn.config(command=self.getActivity)
        self.frame.completeActivity_btn.config(command=self.completeActivity)
        self.frame.navigateCompleted_btn.config(command=self.navigateCompleted)

    def getActivity(self):
        response = requests.get("https://www.boredapi.com/api/activity/")
        data = response.json()
        self.model.activity.setActivity(data['activity'])

    def completeActivity(self):
        if not self.model.activity.is_completed:
            self.model.activity.completeActivity()
            post = {
                "activity_description": self.model.activity.activity_description,
            }
            print(post)
            completed_activities.insert_one(post)
        else:
            print("Activity already completed")

    def navigateCompleted(self):
        self.view.switch("completed")

    def update_view(self):   
        self.frame.activity_description.config(text=self.model.activity.activity_description)