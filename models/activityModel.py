from .base import ObservableModel

class Activity(ObservableModel):
    def __init__(self):
        super().__init__()
        self.activity = None
        self.is_completed = False

    def setActivity(self, activity):
        print("Model is receiving activity ...")
        self.activity = activity
        self.trigger_event("activity_changed")
    
    def completeActivity(self):
        print("Model is completing activity? ...")
        self.is_completed = True
        self.trigger_event("activity_changed")

    
