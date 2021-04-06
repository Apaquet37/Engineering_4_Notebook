#GPIO pins I2C
#Written by Abigail Paquette

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Import the LSM303 module.
import Adafruit_LSM303
# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
top = 2
var = 2
font = ImageFont.load_default()
#draw.rectangle((0,0,width,height), outline=0, fill=0)

while True:
	draw = ImageDraw.Draw(image)
	# Read the X, Y, Z axis acceleration values and print them.
	accel, mag = lsm303.read()
	# Grab the X, Y, Z components from the reading and print them out.
	accel_x, accel_y, accel_z = accel
	x = round((accel_x/100),3)
	y = round((accel_y/100),3)
	z = round((accel_z/100),3)
	print('Accel X={0}, Accel Y={1}, Accel Z={2}'.format(accel_x, accel_y, accel_z))
	print('NEW:  Accel X={0}, Accel Y={1}, Accel Z={2}'.format(x, y, z))
	draw.text((var, top), 'Accel Data:', font=font, fill=255)
	draw.text((var, top+16), 'x ={0}'.format(x), font=font, fill=255)
	draw.text((var, top+30), 'y ={0}'.format(y), font=font, fill=255)
	draw.text((var, top+45), 'z ={0}'.format(z), font=font, fill=255)
	disp.image(image)
	disp.display()
	# Wait half a second and repeat.
	time.sleep(0.5)
	disp.clear()
	print("cleared")
	draw.rectangle((100, 12, 55, 50), outline=0, fill=0)
