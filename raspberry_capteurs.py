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
        if(line):
            parse=line.decode().split(",")
            x_pos=parse[parse.index("POS")+1]
            y_pos=parse[parse.index("POS")+2]
            val = (x_pos,y_pos)
            print(datetime.datetime.now().strftime("%H:%M:%S"),"(",x_pos,", ",y_pos,")")
    except Exception as ex:
        print(ex)
        break
DWM.write("\r".encode())
DWM.close()