from .base import ObservableModel

class Activity(ObservableModel):
    def __init__(self):
        super().__init__()
        self.activity_description = "Click the button to suggest an activity!"
        self.is_completed = False

    def setActivity(self, activity):
        self.activity_description = activity
        self.trigger_event("activity_changed")
    
    # def completeActivity(self):
    #     print("Model is completing activity? ...")
    #     self.is_completed = True
    #     self.trigger_event("activity_changed")

    
