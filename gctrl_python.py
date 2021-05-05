import serial
import syslog
import time

port = '/dev/ttyUSB1'
file = 'owl.gcode'
step = 0.9

def portWrites():
    cnc = serial.Serial(port,9600,timeout=5)
    
    for i in range(len(rl)):
        #try:
        cnc.write((rl[i]).encode("ascii"))
        print((rl[i]).encode("ascii"))
        cnc_out = cnc.readline()
        print(cnc_out.strip())
        #except:
        #    print("unicode found!")
        
    return 0

def stream():
    return 0

def menu():
    print("1 - Select port:")
    print("2 - Open file:")
    print("3 - Print it!")
    print("4 - Move steppers with arrows and O/P for pen")
    print("5 - Go home X=0, Y=0, P=up")
    print("-------")
    print("curent port:", port)
    print("curent file:", file)
    #i = int(input())
    #return i
    
menu()

f = open(file)
rl = f.readlines()

portWrites()


print(rl[20])
a = rl[20].index("X")
b = rl[20].index("Y")
print(float(rl[20][a+1:b-1])*step)
print(round((float(rl[20][a+1:b-1])*step),2))
f.close()