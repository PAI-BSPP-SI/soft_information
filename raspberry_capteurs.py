import serial
import time
import datetime

DWM=serial.Serial(port="/dev/ttyACM0", baudrate=115200)
print("Connected to " +DWM.name)
DWM.write("\r\r".encode())
time.sleep(1)
DWM.write("lec\r".encode())
time.sleep(1)
while True:
    try:
        line=DWM.readline()
        print(line)
    except Exception as ex:
        print(ex)
        break
DWM.write("\r".encode())
DWM.close()