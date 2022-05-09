import pyvisa
from time import sleep
import math

rm = pyvisa.ResourceManager()
sg_com = rm.list_resources()[0]
sg = rm.open_resource(sg_com)

starting_amp = int(input("Input Starting Amplitude:"))  # -70 dBm
stop_amp = int(input("Input Stopping Amplitude:"))  # -50 dBm
incr = int(input("Input Increments:"))  # 2 dB
wait_time = int(input("How many seconds between each mode? "))

sg.write(":OUTP ON")

# L1 Band
sg.write(':FREQ:FIX 1.0 GHz')
power = starting_amp
for i in range(abs(math.floor((stop_amp - starting_amp)/incr))+1):  # -70 - (-50) / 2 = -10 == 10 |||| 50 - 40 / 1 = 10
    print("The Signal Power is: " + str(power) + "dBm")
    sg.write(":POWER:AMPL " + str(power) + "dBm")
    power += incr
    sleep(wait_time)


# L2 Band
sg.write(':FREQ:FIX 3.0 GHz')
power = starting_amp
for i in range(abs(math.floor((stop_amp - starting_amp)/incr))+1):  # 0, 1, 2 -80 - (-50 = -30 / 7 = 28/7 = 4
    print("The Signal Power is: " + str(power) + "dBm")
    sg.write(":POWER:AMPL " + str(power) + "dBm")
    power += incr
    sleep(wait_time)

sg.write(":OUTP OFF")




