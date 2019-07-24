import reader
import fusion
from tqdm import tqdm


F = fusion.Fusion(lambda x,y: x-y)
data = reader.load_raw_data()
data = data.sort_values('time')


mag = data[['mag_x', 'mag_y', 'mag_z']]
accel = data[['accel_x', 'accel_y', 'accel_z']]
gyro = data[['gyro_x', 'gyro_y', 'gyro_z']]

for index in tqdm(data.index):
    m = list(mag.loc[index].values)
    a = list(accel.loc[index].values)
    g = list(gyro.loc[index].values)
    time = data.loc[index, 'time'] 
    F.update(a, g, m, time)
    heading = F.heading
    data.loc[index, 'heading'] = heading

data.to_csv('processed.csv', index = False)



