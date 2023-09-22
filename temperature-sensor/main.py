import machine, onewire, ds18x20, time

ds_pin = machine.Pin(18)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print("Found DS devices: ", roms)

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        celsius = ds_sensor.read_temp(rom)

        print(f"Temp (°F): {round((celsius * 1.8)+32, 2)}")
    time.sleep(5)
