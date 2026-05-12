import os
import requests
from dotenv import load_dotenv

load_dotenv()

ROBOT_IP = os.getenv("ROBOT_IP", "127.0.0.1")
CONTROL_URL = f"http://{ROBOT_IP}:9000/control"
GO_TO_POINT_URL = f"http://{ROBOT_IP}:8080/go_to_point"
CLEAR_PATH_URL = f"http://{ROBOT_IP}:8080/clear_path"
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

    def _go_to_point(self, point: str) -> bool:
        """Generic go-to-point helper — sends {"name": "<point>"} to GO_TO_POINT_URL"""
        try:
            resp = requests.post(
                GO_TO_POINT_URL,
                json={"name": point},
                timeout=TIMEOUT
            )
            if resp.status_code == 200:
                print(f"[RobotAPI] OK — go_to_point {point}")
                return True
            else:
                print(f"[RobotAPI] HTTP {resp.status_code} — go_to_point {point}")
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

    def go_to_point_a(self) -> bool:
        """Cmd 19 — Go to point A"""
        return self._go_to_point("A")

    def go_to_point_b(self) -> bool:
        """Cmd 20 — Go to point B"""
        return self._go_to_point("B")

    def go_to_point_c(self) -> bool:
        """Cmd 21 — Go to point C"""
        return self._go_to_point("C")

    def go_to_point_d(self) -> bool:
        """Cmd 22 — Go to point D"""
        return self._go_to_point("D")

    def stop(self) -> bool:
        """Cmd 2 — Stop (GET /clear_path)"""
        try:
            resp = requests.get(
                CLEAR_PATH_URL,
                timeout=TIMEOUT
            )
            if resp.status_code == 200:
                print(f"[RobotAPI] OK — stop (clear_path)")
                return True
            else:
                print(f"[RobotAPI] HTTP {resp.status_code} — stop (clear_path)")
                return False
        except requests.exceptions.ConnectionError:
            print(f"[RobotAPI] Connection error — robot unreachable at 100.95.128.237")
            return False
        except requests.exceptions.Timeout:
            print(f"[RobotAPI] Timeout — no response after {TIMEOUT}s")
            return False
        except Exception as e:
            print(f"[RobotAPI] Unexpected error: {e}")
            return False
