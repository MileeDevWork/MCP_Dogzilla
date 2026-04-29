from Speech_Lib import Speech
from command_handler import CommandHandler

spe = Speech("/dev/ttyUSB0")

handler = CommandHandler(robot=your_robot_object)

print("Listening for voice commands...")

while True:
    cmd = spe.speech_read()
    
    if cmd != 999:
        print("Detected command ID:", cmd)
        
        spe.void_write(cmd)
        
        handler.handle(cmd)from Speech_Lib import Speech
from command_handler import CommandHandler

spe = Speech("/dev/ttyUSB0")

handler = CommandHandler(robot=your_robot_object)

print("Listening for voice commands...")

while True:
    cmd = spe.speech_read()
    
    if cmd != 999:
        print("Detected command ID:", cmd)
        
        spe.void_write(cmd)
        
        handler.handle(cmd)from Speech_Lib import Speech
from command_handler import CommandHandler

spe = Speech("/dev/ttyUSB0")

handler = CommandHandler(robot=your_robot_object)

print("Listening for voice commands...")

while True:
    cmd = spe.speech_read()
    
    if cmd != 999:
        print("Detected command ID:", cmd)
        
        spe.void_write(cmd)
        
        handler.handle(cmd)