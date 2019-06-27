import reader
import processor
from display import Display




data = reader.get_data()

data = processor.reduce_obs(data, 1000)
data = processor.smooth_data(data)
data = processor.fit_to_universe(data)


d = Display()

img = d.draw_data(data)
img.save('result.png')
