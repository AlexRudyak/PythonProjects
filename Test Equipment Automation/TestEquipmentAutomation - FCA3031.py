import pyvisa
from time import sleep
from datetime  import date,datetime

#Preset commands
command_list = ["INPUT1:SLOPE POSITIVE", # two counter connected each one with 2 inputs therefore 4 options to preset
                "INPUT1:COUPLING DC",
                "INPUT1:IMPEDANCE 50",
                "INPUT1:ATTENUATION 1X",
                "INPUT1:LEVEL:AUTO Manual",
                "INPUT1:LEVEL 2.0",
                "INPUT1:FILT OFF",

                "INPUT2:SLOPE POSITIVE",
                "INPUT2:COUPLING DC",
                "INPUT2:IMPEDANCE 50",
                "INPUT2:ATTENUATION 1X",
                "INPUT2:LEVEL:AUTO Manual",
                "INPUT2:LEVEL 2.0",
                "INPUT2:FILT OFF"
]

# Open backend and print connected devices
rm = pyvisa.ResourceManager()
print(rm.list_resources())
counter_1_com = rm.list_resources()[0]
counter_2_com = rm.list_resources()[1]

# Open comms to counter
counter_1 = rm.open_resource(counter_1_com)
counter_2 = rm.open_resource(counter_2_com)

# Preset the counters
for command in command_list: 
    counter_1.write(command)
    counter_2.write(command)

filename = "TimeIntervalLogs_" + str(date.today()) + "_" + datetime.now().strftime("%H.%M.%S") + ".csv"     """The file name will change each time it ran
                                                                                                               With date and time of the run"""
log = open(filename, 'w')
i = 1
log.write("Date, Time, Counter 1, Counter 2\n")

while 1:
    log = open(filename, 'a')

    sample1 = counter_1.query("READ?", delay = 0.5)
    sample2 = counter_2.query("READ?", delay = 0.5)

    log.write(str(date.today()) + ',' + datetime.now().strftime("%H.%M.%S") + ',' + sample1[:-1] + ',' + sample2) # remove the \n from sample1
    print("Sample " + str(i))
    i += 1
    sleep(1)
    log.close() # close the file after each iteration to remove from RAM into ROM
