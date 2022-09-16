import sys
sys.tracebacklimit = 0
from conv import *
from errors import *
from texts import *
from from_binary import *
from from_decimal import *
from from_hexadecimal import *

try:

    match sys.argv[1]:
   
        case '-h' | '-help':
            print(help_text)

        case "-conv":
            if len(sys.argv) != 5:
                raise convArgumentNumberException

            print("Answer: " + str(conv(sys.argv[2],sys.argv[3],sys.argv[4])))

        case "-add":
            if len(sys.argv) != 7:
                raise addArgumentNumberException

            decOne = int(conv(sys.argv[2],sys.argv[3],'d'))
            decTwo = int(conv(sys.argv[4],sys.argv[5],'d'))
            print("Answer: " + str(conv('d',decOne + decTwo,sys.argv[6])))

        case "-sub": 
            print ("sub")

        case "-xor":
            print("xor")

except convArgumentNumberException:
    print("""Error! Not enough Input Parameters.
Syntax: ucalc -conv inputType value outputType
Type ucalc -h for help""")

except addArgumentNumberException:
    print("""Error! Not enough Input Parameters.
Syntax: ucalc -add inputType1 value1 inputType2 value2 outputType
Type ucalc -h for help""")

