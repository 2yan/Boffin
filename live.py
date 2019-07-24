from sensors import nine_dof,clock

import fusion
f = fusion.Fusion(lambda x,y: x-y)

nine_dof.init()


while True:
    accel, gyro, mag, _ =  nine_dof.get_data(True)
    time = clock.get_data()['time'] 
    f.update(accel, gyro, mag, time)
    print(f.heading)
