import reader
import processor
from display import Display



print("LOADING DATA")
data = reader.get_data()

print("SMOOTHING GPS")
data = processor.smooth_data(data)
print("FITTING")
data = processor.fit_to_universe(data)

print("REDUCING OBS")
data = processor.reduce_obs(data, 1000)

print("DRAWING")
d = Display()
img = d.draw_data(data)
img.save('result.png')
