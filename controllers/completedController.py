from mongodb.mongodb_config import *

class CompletedController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["completed"]
        self.getCompletedActivities()
        self._bind()

    def _bind(self):
        self.frame.returnHome_btn.config(command=self.returnHome)

    def returnHome(self):
        self.view.switch("home")

    def getCompletedActivities(self):
        completed_activities_list = []
        cursor = completed_activities.find({})
        for document in cursor:
            completed_activities_list.append(document["activity_description"])
        completed_activities_list.reverse()    
        self.frame.completed_activities_var.set(value=completed_activities_list)