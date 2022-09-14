import pyvisa
from Functions.blinking import blinking
from Functions.random_blinking import random_blinking
from Functions.sweep import sweep

available_functions = ["Sweep", "Blink", "Random Blink"]

# Define the signal generator and its com port
rm = pyvisa.ResourceManager()
print(rm.list_resources()) # List available connected devices
sg_com = rm.list_resources()[0] # Specific for my machine
sg = rm.open_resource(sg_com) # Open comms 

# Print list of availabe functions and let the user decide which one to pick
for i,available_function in enumerate(available_functions):
    print(str(i+1) + ") " + available_function)
function_choice = input("Choose a function 1-" + str(len(available_functions)) + ": ")

# Call for the chosen function
match function_choice:
    case 1: # Sweep the CW, units: Object, MHz, MHz, MHz, dBm
        sweep(test_equipment=sg,starting_frequency=2400,ending_frequency=2401,frequency_jump=0.1,power=-40)
    case 2: # Single Frequency On/Off CW, units: Object, MHz, Seconds, dBm
        blinking(test_equipment=sg,blinking_frequency=2400,time_between_blinks=0.25,power=-40)
    case 3: # Random Frequency On/Off CW, units: Object, MHz, MHz, dBm, Seconds
        random_blinking(test_equipment=sg,starting_frequency=2400,ending_frequency=2401,power=-40,time_between_blinks=0.05)

# Turn off RF output
sg.write(":OUTP OFF")






