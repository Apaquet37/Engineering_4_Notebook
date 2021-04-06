#GPIO pins I2C
#Written by Abigail Paquette

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306 #import oled module

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_LSM303 #import accelerometer module
lsm303 = Adafruit_LSM303.LSM303() #create a LSM303 instance (accelerometer)

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) #my i2c address in 0x3d, someone else's might be different
disp.begin() 
disp.clear()
disp.display()
width = disp.width #setting the width of the screen
height = disp.height #setting the height of the screen
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2 #some variables to help with positioning text on the display
top = padding
bottom = height = padding
var = padding
font = ImageFont.load_default()


while True:
        accel, mag = lsm303.read() #get the accelerometer and magnometer (compass) values
        accel_x, accel_y, accel_z = accel #recieve the accelerometer values, store them and give them names
        x = round((accel_x/100),3) #the accelerometer values had to be scaled and rounded
        y = round((accel_y/100),3)
        z = round((accel_z/100),3) #if scaled correctly, z should be 9.8 (m/s^2)
        print('Accel X={0}, Accel Y={1}, Accel Z={2}'.format(accel_x, accel_y, accel_z)) #printing initial values
        print('NEW:  Accel X={0}, Accel Y={1}, Accel Z={2}'.format(x, y, z)) #printing scaled and rounded values
        draw.text((var, top), 'Accelerometer Data:', font=font, fill=255) #Title
        draw.text((var, top+15), 'x ={0}'.format(x), font=font, fill=255) #x value
        draw.text((var, top+30), 'y ={0}'.format(y), font=font, fill=255) #y value
        draw.text((var, top+45), 'z ={0}'.format(z), font=font, fill=255) #z value
        disp.image(image) #actually pushing this text to the display
        disp.display()

        time.sleep(.5) #a half second pause to give the user time to read the value
        draw.rectangle((17, 17, 50, 75), outline=0, fill=0) #draw a black rectangle over the changing values to "clear" the display
        disp.image(image)
        disp.display()
