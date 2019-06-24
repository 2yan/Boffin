import time
import board
import busio
import adafruit_gps
import serial
import threading


update_rate = .1 #IN SECONDS
val = False
thread = False
gps = False

def init():
    global update_rate
    uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)
    gps = adafruit_gps.GPS(uart, debug=False)
    gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    gps.send_command('PMTK220,{}'.format(int(update_rate*1000)).encode())
    return gps

def get_gps():
    global gps
    if not gps:
        print("Initalizing")
        gps = init()
    return gps

def __get_data():
    gps = get_gps()
    if not gps.has_fix:
        return False
    return (gps.latitude, gps.longitude)


def runner():
    global val
    global update_rate

    last = time.monotonic()
    while True:
        gps = get_gps()
        gps.update()
        current = time.monotonic()
        if current - last >= update_rate: 
            val = __get_data()
    return 


def start_thread():
    global thread
    thread = threading.Thread(target = runner)
    thread.start()


def get_data():
    global val
    return val

def write_cords(x,y):
    with open("outfile.txt", 'a') as f:
        f.write("{},{}\n".format(x,y))

start_thread()

