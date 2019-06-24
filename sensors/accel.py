from adxl345 import ADXL345
import pandas as pd
import numpy as np


print("Initalizing Accelerometer")
s = ADXL345()



def raw_read():
    ans = s.get_axes(False)
    x = ans['x']
    y = ans['y']
    z = ans['z']
    return {'x_accel':x, 'y_accel':y, 'z_accel':z} 



def get_data(samples = 1):
    if samples == 1:
        return raw_read()
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
    return {'x_accel':xs, 'y_accel':ys, 'z_accel':zs} 


     
    

if __name__ == '__main__':

    while True:
        ans = get_data()
        x = ans['x'] 
        y = ans['y']
        z = ans['z']

        text = "{:,.4f} |  {:,.4f}  |  {:,.4f}".format(x, y, z)
        print(text)
