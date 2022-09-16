from from_decimal import *
from from_binary import *
from from_hexadecimal import *

def conv (from_type,value,to_type):

    match from_type:

        case 'd' | 'dec' | 'decimal':
           return convert_from_decimal_to_type(value,to_type)

        case 'b' | 'bin' | 'binary':
           return convert_from_binary_to_type(value,to_type)

        case 'h' | 'hex' | 'hexa' | 'hexadecimal':
           return convert_from_hexadecimal_to_type(value,to_type)