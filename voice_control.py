from Speech_Lib import Speech
from command_handler import CommandHandler
import time

spe = Speech("/dev/ttyUSB0")
handler = CommandHandler()

print("Listening for voice commands...")

while True:
    start_process = time.time()
    cmd = spe.speech_read()

    if cmd != 999:

        if cmd in handler.command_map:
            label = handler.command_map[cmd][0]

            print(f"\n" + "="*30)
            print(f"[TESTCASE] Lệnh nhận diện: {label} (ID: {cmd})")

            spe.void_write(cmd)
            handler.handle(cmd)

            end_process = time.time()

            latency = (end_process - start_process) * 1000

            print(f"[METRIC] Thời gian nhận diện end-to-end(nhận diện -> thực thi): {latency:.2f}ms")
            print(f"[STATUS] Kết quả: Thành công")
            print("="*30 + "\n")
        else:
            print(f"[DEBUG] Nhận được ID {cmd} nhưng chưa định nghĩa trong Command Map.")
