from .homeController import HomeController
from .completedController import CompletedController

class Controller:
    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.home_controller = HomeController(model, view)
        self.completed_controller = CompletedController(model, view)

    #     self.model.activity.add_event_listener(
    #         "activity_changed", self.auth_state_listener
    #     )

    # def auth_state_listener(self, data):
    #     if data.is_logged_in:
    #         self.home_controller.update_view()
    #         self.view.switch("home")
    #     else:
    #         self.view.switch("signin")

    def start(self):
        self.view.switch("home")

        self.view.start_mainloop()