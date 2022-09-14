from time import sleep
import random

def random_blinking(test_equipment,starting_freq,ending_freq,power,time_between_blinks):
        '''
        Input:
                Test_equipment - Object.
                Starting_frequency - In MHz.
                Ending_frequency - In MHz.
                Power - In dBm.
                Time_between_blinks - In seconds.
        Output:
                Frequency sweep starting from starting_frequency to ending_frequency,
                in freq_jump steps.
        '''
        test_equipment.write("POWER:AMPL " + str(power) + "dBm")
        while 1:
                random_freq = round(random.uniform(starting_freq, ending_freq), 2)
                test_equipment.write(":FREQ:FIX " + str(random_freq) + "MHz")
                test_equipment.write(":OUTP ON")
                sleep(time_between_blinks)
                test_equipment.write(":OUTP OFF")
                sleep(time_between_blinks)
        test_equipment.write("POWER:OUTP OFF")





