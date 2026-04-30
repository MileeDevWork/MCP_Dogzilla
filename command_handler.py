from robot_api import RobotAPI

IGNORED_CMDS = {0}


class CommandHandler:
    def __init__(self):
        self.api = RobotAPI()
        self.command_map = {
            52: ("Dancing",      self.api.dance),
            # 19: ("Go to point A", self.api.go_to_point_a),
        }

    def handle(self, cmd: int):
        if cmd in IGNORED_CMDS:
            return
        if cmd in self.command_map:
            label, action = self.command_map[cmd]
            print(f"[CMD] {label}")
            action()
