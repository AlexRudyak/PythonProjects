# CMD Integrated Unit Converter

Debugging/Coding Embedded projects and There is a need to convert unitsfrom different?<br>
Dont want to use the windows calculator again because it is too slow?<br>
Want to convert the units and still be on your coding file?<br>

This is a CMD Integrated Unit Converter.

Made with pure python.

Simply make an executable and add to PATH.

Installing _pyinstaller_:
>pip install pyinstaller

## Supported Types:

Binary      - 'b' or 'bin' or 'binary'                - Takes values '0's or '1's<br>
Decimal     - 'd' or 'dec' or 'decimal'               - Takes values 0-9<br>
Hexadecimal - 'h' or 'hex' or 'hexa' or 'hexadecimal' - Takes values 0-9, A-F<br>

## Available Functions:

- -conv<br>

Convert Function.<br>
Converts from one unit type to another.

Syntax:
>ucalc -conv fromType value toType
        

- -add<br>

Add Function.<br>
Adds two numbers from different or same types into desired type.<br>

Syntax:
>ucalc -add inputType1 value1 inputType2 value2 outputType

## Future Support:
XOR for all bases.<br>
SUBtract for all bases.


