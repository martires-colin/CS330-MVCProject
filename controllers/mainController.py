from .homeController import HomeController
from .completedController import CompletedController

class Controller:
    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.home_controller = HomeController(model, view)
        self.completed_controller = CompletedController(model, view)

        self.model.activity.add_event_listener(
            "activity_changed", self.activity_changed_listener
        )
        self.model.activity.add_event_listener(
            "activity_completed", self.activity_completed_listener
        )

    def activity_changed_listener(self, data):
        self.home_controller.update_view()

    def activity_completed_listener(self, data):
        self.completed_controller.getCompletedActivities()

    def start(self):
        self.view.switch("home")
        self.view.start_mainloop()