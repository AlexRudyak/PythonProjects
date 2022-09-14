from time import sleep

def blinking(test_equipment,blinking_freq,time_between_blinks,power):
        '''
        Input:
                test_equipment - Object
                blinking_frequency - In MHz
                time_between_blinks - In Seconds
                power - In dBm
        Output:
                Blinking frequency with programmable time between blinks
                On/Off with D.C 50%.
        '''
        test_equipment.write("POWER:AMPL " + str(power) + "dBm")
        test_equipment.write(":FREQ:FIX " + str(blinking_freq) + "MHz")
        while 1:
                test_equipment.write(":OUTP ON")
                sleep(time_between_blinks)
                test_equipment.write(":OUTP OFF")
                sleep(time_between_blinks)
        test_equipment.write(":OUTP OFF")