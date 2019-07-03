import numpy as np

from Adafruit_BNO055 import BNO055

def get_sensor():
    x = BNO055.BNO055(serial_port= '/dev/ttyAMA0', rst=18)
    return x

sensor = get_sensor()


def get_data(samples= 1):
    x = []
    y = []
    z = []

    for num in range(samples):
        x1,x2,x3 = sensor.read_linear_acceleration()
        x.append(x1)
        y.append(x2)
        z.append(x3)


    ans = {'x_accel':np.mean(x),
            'y_accel':np.mean(y),
            'z_accel':np.mean(z)}
    return ans


def init():
    sensor.begin()
if __name__ == '__main__':
    init()
    while True:
        print(get_data(10))
