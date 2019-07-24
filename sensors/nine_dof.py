import numpy as np

from Adafruit_BNO055 import BNO055

def get_sensor():
    x = BNO055.BNO055(serial_port= '/dev/ttyAMA0', rst=18)
    return x


def save_callib(c):
    with open('9dof.callib', 'w') as f:
        for num in c:
            f.write(str(num) + '\n')
    return 


def load_callib():
    c = []
    with open('9dof.callib', 'r') as f:
        text = f.read()
    text = text.split('\n')
    for number in text:
        try:
            c.append(int(number))
        except Exception as e:
            pass
    return c

sensor = get_sensor()


def get_data(live = False):
    accel= sensor.read_accelerometer()
    gyro = sensor.read_gyroscope()
    mag = sensor.read_magnetometer()
    lin_accel = sensor.read_linear_acceleration()
    if live:
        return accel, gyro, mag, lin_accel
    dims = 'xyz'
    
    maps= {'accel':accel, 
            'gyro':gyro,
            'mag':mag,
            'lin_accel':lin_accel}
    final = {}

    for key in maps.keys():
        final[key + '_x'] = maps[key][0]
        final[key + '_y'] = maps[key][1]
        final[key + '_z'] = maps[key][2]

    return final 


def init():
    sensor.begin()
    callib = load_callib()
    sensor.set_calibration(callib)

if __name__ == '__main__':
    init()
    while True:
        print(get_data(10))
