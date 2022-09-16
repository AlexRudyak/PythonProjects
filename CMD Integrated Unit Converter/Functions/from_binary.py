def convert_from_binary_to_type(binary_value,to_type):
    base = 2
    match to_type:

        # from binary to decimal
        case 'd' | 'dec' | 'decimal':
            return int(str(binary_value),base)

        # from binary to hexadecimal
        case 'h' | 'hex' | 'hexa' | 'hexadecimal':
            return hex(int(str(binary_value),base))
        
        # if binary return as is
        case 'b' | 'bin' | 'binary':
            return bin(int(str(binary_value),base)).replace("0b","")