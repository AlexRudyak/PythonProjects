help_text = """
This is a CMD Integrated Unit Converter.

Supported Types:

Binary      - 'b' or 'bin' or 'binary'                - Takes values '0's or '1's
Decimal     - 'd' or 'dec' or 'decimal'               - Takes values 0-9
Hexadecimal - 'h' or 'hex' or 'hexa' or 'hexadecimal' - Takes values 0-9, A-F

Available Functions:

-conv   Convert Function
        Converts from one unit type to another.

        Syntax: ucalc -conv fromType value toType
        

-add    Add Function.
        Adds two numbers from different or same types into desired type.

        Syntax: ucalc -add inputType1 value1 inputType2 value2 outputType

Future Support:
XOR for all bases.
SUBtract for all bases.
"""

available_types = ['b',
                  'bin',
                  'binary',
                  'd',
                  'dec',
                  'decimal',
                  'h', 
                  'hex', 
                  'hexa', 
                  'hexadecimal'
                  ]