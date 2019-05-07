from time import time

class Sensor:
    def __init__(self, name, get_data):
        self.name = name
        self.get_data = get_data
        return
    
    
    
    
def get_available_sensors():
    s = ['gps', 'forces', 'accel', 'brake']
    return s


def save_observation(now, data):
    for key in data.keys():
        value = data.loc[key]
        #BROADCAST TO RABBITMQ TO SAVE

    return     

    
    

while True:
    
    now = time.time() 
    
    datas = []
    for s  in get_available_sensors():
        data = s.read_data()
        datas.append(data)
        
    for data in  datas:
        save_observation(now, data)
        
    
    