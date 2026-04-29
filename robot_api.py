import os
import requests
from dotenv import load_dotenv

load_dotenv()

ROBOT_IP = os.getenv("ROBOT_IP", "127.0.0.1")
CONTROL_URL = f"http://{ROBOT_IP}:9000/control"
TIMEOUT = 5


class RobotAPI:
    def __init__(self):
        print(f"[RobotAPI] Connected to {ROBOT_IP}")

    def _post(self, payload: dict) -> bool:
        try:
            resp = requests.post(
                CONTROL_URL,
                json=payload,
                timeout=TIMEOUT
            )
            if resp.status_code == 200:
                print(f"[RobotAPI] OK — {payload}")
                return True
            else:
                print(f"[RobotAPI] HTTP {resp.status_code} — {payload}")
                return False
        except requests.exceptions.ConnectionError:
            print(f"[RobotAPI] Connection error — robot unreachable at {ROBOT_IP}")
            return False
        except requests.exceptions.Timeout:
            print(f"[RobotAPI] Timeout — no response after {TIMEOUT}s")
            return False
        except Exception as e:
            print(f"[RobotAPI] Unexpected error: {e}")
            return False

    # ── Commands ────────────────────────────────────────────

    def dance(self) -> bool:
        """Cmd 52 — Dancing (Wave_Body)"""
        return self._post({"command": "behavior", "name": "Wave_Body"})

    # def go_to_point_a(self) -> bool:
    #     """Cmd 19 — Go to point A"""
    #     return self._post({"command": "go_to_point", "name": "A"})
