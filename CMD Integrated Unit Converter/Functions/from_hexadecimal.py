def convert_from_hexadecimal_to_type(hexadecimal_value,to_type):
    base = 16
    match to_type:

        # from hexadecimal to decimal
        case 'd' | 'dec' | 'decimal':
            return int(str(hexadecimal_value),base)

        # from hexadecimal to binary
        case 'b' | 'bin' | 'binary':
            output = ""
            binary_value = bin(int(str(hexadecimal_value),base)).replace("0b","")
            if len(binary_value)%4 != 0:
                binary_value = (4-len(binary_value)%4)*"0" + binary_value
            for i,digit in enumerate(binary_value):
                output += digit
                if (i+1)%4 == 0:
                    output += " "
            return output

        # if hexa return as is
        case 'h' | 'hex' | 'hexa' | 'hexadecimal':
            return hex(int(str(hexadecimal_value),base))
            
