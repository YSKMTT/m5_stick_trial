import serial
import numpy as np
from matplotlib import pyplot as plt


t = np.zeros(100)
y = np.zeros(100)

plt.ion()
plt.figure()
(li,) = plt.plot(t, y)
# plt.ylim(0, 5)
plt.xlabel("time[s]")
plt.ylabel("Z accelaration[G]")


ser = serial.Serial("COM7", 115200, timeout=0.1)
ser.readline()


# ser.write("*".encode())
# data = ser.readline().strip().rsplit()
i = 0
while True:
    ser.write("*".encode())
    val_m5 = ser.readline()
    # val_decoded = int(repr(val_m5.decode())[1:-5])
    val_decoded = val_m5.strip().decode("utf-8")
    if val_decoded == "":
        pass
    else:
        i = i + 0.1
        t = np.append(t, i)
        y = np.append(y, float(val_decoded))
        li.set_xdata(t)
        li.set_ydata(y)
        print(val_decoded)
        plt.xlim(min(t), max(t))
        plt.ylim(min(y), max(y))
        plt.draw()
        plt.pause(0.05)
    # if i%100==0:
    # t = np.append(t, i)
    # t = np.delete(t, 0)
    # y = np.append(y, float(val_m5))
    # y = np.delete(y, 0)
    # li.set_xdata(t)
    # li.set_ydata(y)


ser.close()
