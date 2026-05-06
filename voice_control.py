from Speech_Lib import Speech
from command_handler import CommandHandler

spe = Speech("/dev/ttyUSB0")
handler = CommandHandler()

print("Listening for voice commands...")

while True:
    cmd = spe.speech_read()
    if cmd != 999 and cmd in handler.command_map:
        print(f"[SPEECH] Detected cmd: {cmd}")
        spe.void_write(cmd)
        handler.handle(cmd)
