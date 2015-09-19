__author__ = 'ben'

import smbus

def light_up_led(led_id, color):
    # Open up i2c com with pwm driver
    bus = smbus.SMBus(0)

    DEVICE_ADDRESS = 0x15      # 7 bit address (will be left shifted to add the read write bit)
    DEVICE_REG_MODE1 = 0x00
    DEVICE_REG_MODE2 = 0x01
    DEVICE_REG_LEDOUT0 = hex(6 + 4 * led_id)
    DEVICE_REG_LEDOUT1 = hex(10 + 4 * led_id)
    DEVICE_REG_LEDOUT2 = hex(14 + 4 * led_id)

    # Write a single register
    bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x00)
    bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE2, 0x00)

    # Write an array of registers
    led_low_values = [0x00, 0x00]
    led_high_values = [color[0] & 0xff, (color[0] >> 8) & 0x0F]

    bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, led_low_values)
    bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0 + 2, led_high_values)

    led_low_values = [0x00, 0x00]
    led_high_values = [color[1] & 0xff, (color[1] >> 8) & 0x0F]

    bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT1, led_low_values)
    bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT1 + 2, led_high_values)

    led_low_values = [0x00, 0x00]
    led_high_values = [color[2] & 0xff, (color[2] >> 8) & 0x0F]

    bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT2, led_low_values)
    bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT2 + 2, led_high_values)

    # close i2c com