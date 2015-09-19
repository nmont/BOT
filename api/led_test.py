__author__ = 'ben'

import smbus

# Open up i2c com with pwm driver
bus = smbus.SMBus(0)

DEVICE_ADDRESS = 0x15      # 7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

# Write a single register
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x80)

# Write an array of registers
ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)

# set R led_id low start address to 0
# set R led_id high start address to 0
# set G led_id low start address to 0
# set G led_id high start address to 0
# set B led_id low start address to 0
# set B led_id high start address to 0

# set R led_id low end address to color[0] & 0x0FF
# set R led_id high end address to (color[0] >> 8) & 0x0F

# set G led_id low end address to color[1] & 0x0FF
# set G led_id high end address to (color[1] >> 8) & 0x0F

# set B led_id low end address to color[2] & 0x0FF
# set B led_id high end address to (color[2] >> 8) & 0x0F

# close i2c com