from time import sleep

def sweep(test_equipment,starting_freq,ending_freq,freq_jump,power):
        '''
        Input:
                Test_equipment - Object
                Starting_frequency - In MHz
                Ending_frequency - In MHz
                Frequency_jump - In MHz
                Power - In dBm
        Output:
                Frequency sweep starting from starting_frequency to ending_frequency 
                in freq_jump steps.
                Repeats untill interupted.
        '''
        num_jumps = int((ending_freq-starting_freq)/freq_jump)
        test_equipment.write("POWER:AMPL " + str(power) + "dBm")
        test_equipment.write(":OUTP ON")
        while 1:
                test_equipment.write(":FREQ:FIX " + str(starting_freq) + "MHz")
                for i in range(num_jumps+1):
                        test_equipment.write(":FREQ:FIX " + str(starting_freq+freq_jump*i) + "MHz")
                        sleep(0.05)
        test_equipment.write("POWER:OUTP OFF")





