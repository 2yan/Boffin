from sensors import gps, accel

import time




def begin():
    while True:
        t1 = time.time()
        moment  = accel.get_data()
        a = time.time() - t1

        t1 = time.time()
        pos = gps.get_data()
        b = time.time()



        print('accel', ' -' , a)
        print('gps  ', ' -' , b)


