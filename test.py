import time
import pyfirmata

board = pyfirmata.Arduino("/dev/ttyACM0")
print("Communication Successfully started")
led = 13
while True:
    board.digital[led].write(1)
    time.sleep(1)
    board.digital[led].write(0)
    time.sleep(1)