import pyvisa
from time import sleep
import math

rm = pyvisa.ResourceManager()
sg_com = rm.list_resources()[0] # Specific for my machine, run without square brackets into print to see the list.
sg = rm.open_resource(sg_com)

frequency = int(input("Input Frequency in GHz: "))
starting_amp = int(input("Input Starting Amplitude: "))  # -70 dBm
stop_amp = int(input("Input Stopping Amplitude: "))  # -50 dBm
incr = int(input("Input Increments: "))  # 2 dB
wait_time = int(input("How many seconds between each mode?: "))

sg.write(":OUTP ON")

sg.write(":FREQ:FIX " + str(frequency) + "GHz")
power = starting_amp
for i in range(abs(math.floor((stop_amp - starting_amp)/incr))+1):  # -70 - (-50) / 2 = -10 == 10 |||| 50 - 40 / 1 = 10
    print("The Signal Power is: " + str(power) + "dBm")
    sg.write(":POWER:AMPL " + str(power) + "dBm")
    power += incr
    sleep(wait_time)

sg.write(":OUTP OFF")




