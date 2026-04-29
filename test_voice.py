from Speech_Lib import Speech
from command_handler import CommandHandler

spe = Speech("/dev/ttyUSB0")
handler = CommandHandler()

print("Listening for voice commands...")

while True:
    cmd = spe.speech_read()
    if cmd != 999:
        print(f"[SPEECH] Detected cmd: {cmd}")
        spe.void_write(cmd)   # phát âm thanh xác nhận
        handler.handle(cmd)
