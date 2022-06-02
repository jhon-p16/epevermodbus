#!/usr/bin/env python3
import time
import minimalmodbus

# SETUP CS >> port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

instrument.serial.baudrate = 115200
instrument.serial.timeout = 1
instrument.mode = minimalmodbus.MODE_RTU

# print(instrument) #debug all properties

# instrument.write_register (0x9067, 1, 0, 6) # set 12V battery rated voltage 
# instrument.write_register (0x9001, 26, 0, 6) # set 26AH battery current capacity
# battery_rated_voltage = instrument.read_register(0x9067, 0, 3, signed=True)
# print(battery_rated_voltage)


def get_battery_current():
    currentL = instrument.read_register(0x331B, 0, 4, signed=True)
    currentH = instrument.read_register(0x331C, 0, 4, signed=True)
    value = currentL | currentH << 16
    print(value/100)

def toggle_load(state):
    instrument.write_bit(0x2, state, 5) 

# load >> ON
get_battery_current()
toggle_load(1)
time.sleep(5)

get_battery_current()
# load >> OFF
toggle_load(0)

