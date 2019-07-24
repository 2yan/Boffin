import nine_dof
import pandas as pd 
import numpy as np

nine_dof.init()

x = nine_dof.sensor

while True:
    t = []
    for num in range(100):
        t.append(x.read_linear_acceleration())
    print(np.mean(np.array(t), axis = 0))
