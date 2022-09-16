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
            output = ""
            binary_value = bin(int(str(binary_value),base)).replace("0b","")
            if len(binary_value)%4 != 0:
                binary_value = (4-len(binary_value)%4)*"0" + binary_value
            for i,digit in enumerate(binary_value):
                output += digit
                if (i+1)%4 == 0:
                    output += " "
            return output