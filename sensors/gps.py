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

def get_gps():
    global gps
    if not gps:
        print("Initalizing GPS")
        gps = init_gps()
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
            _val = __get_data()
            if _val:
                val = _val
    return 





def get_data():
    global val
    return {'lat':val[0], 'long':val[1]}

def write_cords(x,y):
    with open("outfile.txt", 'a') as f:
        f.write("{},{}\n".format(x,y))

def init_gps():
    global update_rate
    uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)
    gps = adafruit_gps.GPS(uart, debug=False)
    gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    gps.send_command('PMTK220,{}'.format(int(update_rate*1000)).encode())
    return gps

def init():
    data = __get_data()

    global thread
    thread = threading.Thread(target = runner)
    thread.start()
    while True:
        data = __get_data()
        if data:
            print("GPS initalized")
            return

        
