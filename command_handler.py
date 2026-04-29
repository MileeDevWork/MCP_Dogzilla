from robot_api import RobotAPI


class CommandHandler:
    def __init__(self):
        self.api = RobotAPI()
        self.command_map = {
            # 19: ("Go to point A", self.api.go_to_point_a),
            52: ("Dancing",       self.api.dance),
        }

    def handle(self, cmd: int):
        if cmd in self.command_map:
            label, action = self.command_map[cmd]
            print(f"[CMD] {label}")
            action()
        else:
            print(f"[CMD] Unknown command: {cmd}")
