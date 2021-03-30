import serial
import time
import datetime

DWM=serial.Serial(port="/dev/tty.usbmodem0007601032201", baudrate=115200)
print("Connected to " +DWM.name)
DWM.write("\r\r".encode())
time.sleep(1)
DWM.write("lec\r\n".encode())
time.sleep(1)
while True:
    try:
        line=DWM.readline()
        print(line.decode())
        if (line):
            if len(line) >= 140:
                parse = line.decode().split(",")
                x_pos = parse[parse.index("POS") + 1]
                y_pos = parse[parse.index("POS") + 2]
                val = (x_pos, y_pos)
                mycursor = mydb.cursor()
                mycursor.execute(sql, val)
                mydb.commit()
                print(datetime.datetime.now().strftime("%H:%M:%S"), "(", x_pos, ", ", y_pos, ")")
            else:
                print("")
    except Exception as ex:
        print(ex)
        break
DWM.write("\r".encode())
DWM.close()