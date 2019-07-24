from sensors import nine_dof,clock, gps

import fusion
f = fusion.Fusion(lambda x,y: x-y)

clock.init()
gps.init()
nine_dof.init()


while True:
    accel, gyro, mag, linear =  nine_dof.get_data(True)
    time = clock.get_data()['time'] 
    f.update(accel, gyro, mag, time)
    lat_long = gps.get_data()
    print(f.heading - 15, end = ' --- ')
    print(lat_long)
    
