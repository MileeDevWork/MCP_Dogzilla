import requests
import json

class CommandHandler:
    def __init__(self, robot, robot_ip="127.0.0.1"):
        self.robot = robot
        self.robot_ip = robot_ip
        self.api_url = f"http://{robot_ip}:9000/control"

    def call_dancing_api(self):
        try:
            payload = {
                "command": "behavior",
                "name": "Wave_Body"
            }
            headers = {'Content-Type': 'application/json'}
            
            response = requests.post(self.api_url, 
                                   data=json.dumps(payload), 
                                   headers=headers, 
                                   timeout=5)
            
            if response.status_code == 200:
                print("Dancing API called successfully")
                return True
            else:
                print(f"API error: {response.status_code}")
                return False
                
        except Exception as e:
            print("Error calling dancing API:", e)
            return False

    def handle(self, cmd):
        if cmd == 4:
            self.robot.forward()

        elif cmd == 6:
            self.robot.turn_left()

        elif cmd == 7:
            self.robot.turn_right()

        elif cmd == 19:
            self.robot.go_to_point("A")
            
        elif cmd == 52:
            self.call_dancing_api()

        else:
            print("Unknown command:", cmd)