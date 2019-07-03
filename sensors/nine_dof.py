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


def get_data(samples= 1):
    x = []
    y = []
    z = []

    yaw = []
    roll = []
    pitch = []
    
    for num in range(samples):
        x1,x2,x3 = sensor.read_linear_acceleration()
        euler = sensor.read_euler()

        x.append(x1)
        y.append(x2)
        z.append(x3)

        yaw.append(euler[0])
        pitch.append(euler[1])
        roll.append(euler[2])




    ans = {'x_accel':np.mean(x),
            'y_accel':np.mean(y),
            'z_accel':np.mean(z),
            'yaw':np.mean(yaw),
            'pitch':np.mean(pitch),
            'roll':np.mean(roll)
            }
    return ans


def init():
    sensor.begin()
    callib = load_callib()
    sensor.set_calibration(callib)

if __name__ == '__main__':
    init()
    while True:
        print(get_data(10))
