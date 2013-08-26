import serial 
import time
import os
x=1
os.system('clear')

print "WELCOME TO ENERGY MONITORING SYSTEM"
print "SYSTEM DEVELOPED ON PYTHON"

a=0
count=1
avge=0.0
while True:
    time.sleep(3)
    ser=serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    s=ser.read(32)
    print "THE CURRENT POWER USAGE iS(in WATTS)"
    line=ser.readline()
    a=a+float(line)
    avge=a/count
    count=count+1
    print line
    print "The sum of your power consumption is"
    print a
    print "The average value of your power consumption is"
    print avge
    ser.close()
