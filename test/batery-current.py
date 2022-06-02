from epevermodbus.driver import EpeverChargeController


controller = EpeverChargeController("/dev/ttyUSB0", 1)

parameterH = controller.get_battery_current_h()
parameterL = controller.get_battery_current_h()

print(parameterH)
print(parameterL)

value = parameterL | parameterH << 16

print(value/100)