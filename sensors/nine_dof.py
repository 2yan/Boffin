
from Adafruit_BNO055 import BNO055

def get_sensor():
    x = BNO055.BNO055(serial_port= '/dev/ttyAMA0', rst=18)
    return x

