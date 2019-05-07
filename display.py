import numpy as np
from PIL import Image, ImageDraw
import pandas as pd


def get_theta(m):
    return np.arcsin(m)


def get_x(theta,magnitude, start_x ):
    size = np.cos(theta) * magnitude
    end_x = start_x + size
    return end_x


def get_y(theta, magnitude, start_y):
    size = np.tan(theta) * magnitude
    end_y = start_y + size
    return end_y
    
def get_perp_point(x1,y1, x2, y2, magnitude):
    m = (y2 -y1)/(x2 - x1)
    new_slope = -(1/m)

    start_x = (x1 + x2)/2
    start_y= (y2 - y1)/2
    theta = get_theta(new_slope)

    end_x = get_x(theta, magnitude, start_x)
    end_y = get_y(theta, magnitude, start_y)   
    return end_x, end_y


    
class Display():
    
    def __init__(self, x = 1000, y = 1000, background = (255,255,255)):
        self.x = x
        self.y = y
        self.background = background
        
    def get_img(self):
        x = self.x
        y = self.y
        background = self.background
        return Image.new('RGB', (x, y), color = background)    
    
    def draw_lines(self, x, y, img, color = (0,0,0)):
        
        data = pd.DataFrame(index = range(len(x)))
        
        data['x'] = x
        data['y'] = y
        

        draw = ImageDraw.Draw(img)
        
        cords = []
        for i in range(len(data['x'])):
            cord = (data.iloc[i]['x'], data.iloc[i]['y'])
            cords.append(cord)
            
        cords = list(cords)
        
        draw.line(cords, fill =color, width = 2)
        draw.line(((0,0), (2,2)), fill =color, width = 2)
        

        return img
    

        
    
    
    def draw_data(self, data):
        img = self.get_img()       
        data['x'] = data['x'] * img.size[0]
        data['y'] = data['y'] * img.size[1]
                 
        
        

        img = self.draw_lines(data['x'], data['y'], img)
    
        draw = ImageDraw.Draw(img, "RGBA")
        
        
        for thing in ['accel', 'brake']:
            if thing == 'accel':
                color = (11, 102, 35, 250)
            if thing == 'brake':
                color = (194, 24, 7, 250)
                
                
            full_shape = []
                
            for index in data.index[1:]:
                row1 = data.loc[index -1]
                row2 = data.loc[index]
                
                x1 = row1['x']
                y1 = row1['y']
                
                x2 = row2['x'] 
                y2 = row2['y']
                
                size = row2[thing] * img.size[0] * .001
                
                
                dx = x2 - x1
                dy = y2 - y1
                
                
                normal = ( -dy * size, dx* size)

                
                shape = [((x1+x2)/2, (y1+y2)/2)]
                point_x = shape[0][0] + normal[0]
                point_y = shape[0][1] + normal[1]
                full_shape.append((point_x, point_y))
            
            full_shape.extend(reversed(list(zip(data['x'], data['y']))))
            
            draw.polygon(list(full_shape), fill =color)

        img = self.draw_lines(data['x'], data['y'], img)
    
        img = self.add_padding(1.1, img)
        
        
        return img


    def add_padding(self,percent, old_img):
        old_size = old_img.size
        
        new_size = (int(1000 * percent), int(1000 * percent))
                
        new_img = Image.new("RGB", new_size, color  = self.background)   ## luckily, this is already black!
        
        pos_x = (new_size[0]-old_size[0])/2
        pos_y = (new_size[1]-old_size[1])/2
        new_img.paste(old_img, (int(pos_x),  int(pos_y) ))

        return new_img



if __name__ == '__main__':
    d = Display()