from adxl345 import ADXL345
import pandas as pd
import numpy as np
import time
import threading


s = False
callibration = {'x_accel':0,'y_accel':0, 'z_accel':0 }
    
def callibrate(secs = 5):
    print('callibrating Accelerometer')
    global callibration
    callibration = {'x_accel':0,'y_accel':0, 'z_accel':0 }
 

    vals = []
    start = time.monotonic()
    while time.monotonic() <= (start  + secs):
        vals.append(get_data(50, False))
        x = pd.DataFrame(vals)
        x =x.mean()
        callibration = x.to_dict()
    print("callibrated Accelerometer")
    return vals

def callibrate_async(secs = 5):
    t = threading.Thread(target = callibrate, args = (secs,))
    t.start()
    return


def raw_read():
    ans = s.get_axes(False)
    x = ans['x'] 
    y = ans['y'] 
    z = ans['z']
    return {'x_accel':x, 'y_accel':y, 'z_accel':z} 


def correct(x):
    global callibration
    x['x_accel'] =  x['x_accel'] - callibration['x_accel']
    x['y_accel'] =  x['y_accel'] - callibration['y_accel']
    x['z_accel'] =  x['z_accel'] - callibration['z_accel']
    return x

def get_data(samples = 1, remove_gravity = True):
    
    if samples == 1:
        x = raw_read()
        if remove_gravity:
            x = correct(x)
        return x
    
    xs = []
    ys = []
    zs = []

    amt = samples 
    for num in range(0, amt):
        ans = raw_read()
        x = ans['x_accel'] 
        y = ans['y_accel']
        z = ans['z_accel']
        
        xs.append(x)
        ys.append(y)
        zs.append(z)
    xs = np.mean(xs)
    ys = np.mean(ys)
    zs = np.mean(zs)
    final =  {'x_accel':xs, 'y_accel':ys, 'z_accel':zs} 
    if remove_gravity:
        final = correct(final)
    return final


def init():
    print("Initalizing Accelerometer")
    global s
    s = ADXL345()
    callibrate_async(5) 

    print("Accel initalized")
if __name__ == '__main__':

    while True:
        ans = get_data()
        x = ans['x'] 
        y = ans['y']
        z = ans['z']

        text = "{:,.4f} |  {:,.4f}  |  {:,.4f}".format(x, y, z)
        print(text)
