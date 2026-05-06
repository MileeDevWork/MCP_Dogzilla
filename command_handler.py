from robot_api import RobotAPI

IGNORED_CMDS = {0}


class CommandHandler:
    def __init__(self):
        self.api = RobotAPI()
        self.command_map = {
            52: ("Dancing",        self.api.dance),
            19: ("Go to point A",  self.api.go_to_point_a),
            20: ("Go to point B",  self.api.go_to_point_b),
            21: ("Go to point C",  self.api.go_to_point_c),
            22: ("Go to point D",  self.api.go_to_point_d),
        }

    def handle(self, cmd: int):
        if cmd in IGNORED_CMDS:
            return
        if cmd in self.command_map:
            label, action = self.command_map[cmd]
            print(f"[CMD] {label}")
            action()
