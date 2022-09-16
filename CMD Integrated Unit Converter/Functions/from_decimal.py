def convert_from_decimal_to_type(decimal_value,to_type):
    base = 10
    match to_type:

        # from decimal to binary
        case 'b' | 'bin' | 'binary':
            output = ""
            binary_value = bin(int(str(decimal_value),base)).replace("0b","")
            if len(binary_value)%4 != 0:
                binary_value = (4-len(binary_value)%4)*"0" + binary_value
            for i,digit in enumerate(binary_value):
                output += digit
                if (i+1)%4 == 0:
                    output += " "
            return output
            
        # from decimal to hexadecimal
        case 'h' | 'hex' | 'hexa' | 'hexadecimal':
            return hex(int(str(decimal_value),base))

        # if decimal return as is
        case 'd' | 'dec' | 'decimal':
            return decimal_value
