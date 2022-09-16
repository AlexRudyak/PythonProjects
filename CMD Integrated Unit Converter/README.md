# CMD Integrated Unit Base Converter

Debugging/Coding Embedded projects and There is a need to convert units from different bases?<br>
Dont want to use the windows calculator again because it is too slow?<br>
Want to convert the base units and still be on your coding file?<br>

This is a CMD Integrated Unit Base Converter.

Made with pure python.

Simply make an executable and add to PATH.

Installing _pyinstaller_:
>pip install pyinstaller

Create an executable of _ucalc.py_ and add it to path:
>pyinstaller --onefile ucalc.py

A directory named `dist` will be created.
Either add the path to the .exe or copy paste the program into system32 directory.

## Supported Types:

Binary      - 'b' or 'bin' or 'binary'                - Takes values '0's or '1's<br>
Decimal     - 'd' or 'dec' or 'decimal'               - Takes values 0-9<br>
Hexadecimal - 'h' or 'hex' or 'hexa' or 'hexadecimal' - Takes values 0-9, A-F<br>

## Available Functions:

`-h | -help` <br>

Display a help message.

Syntax:
>ucalc -h

`-conv`<br>

Convert Function.<br>
Converts from one unit type to another.

Syntax:
```
ucalc -conv fromType value toType
```        
```
ucalc -conv d 10 b
Answer: 1010

ucalc -conv binary 111000111 hex
Answer: 0x1c7

ucalc -conv hexa 0xff11 b
Answer: 1111 1111 0001 0001
```

`-add`<br>

Add Function.<br>
Adds two numbers from different or same types into desired type.<br>

Syntax:
```
ucalc -add inputType1 value1 inputType2 value2 outputType
```
```
ucalc -add d 10 b 1001 d
Answer: 19

ucalc -add binary 111000111 hex 0xff binary
Answer: 0010 1100 0110

ucalc -add hexa 0xff11 decimal 128 h
Answer: 0xff91
```
## Future Support:
XOR for all bases.<br>
SUBtract for all bases.
Negetive binary and hexadecimals, currently only adding to negative decimal numbers works.


Can be used without creating a .exe with:
>python ucalc.py -function 

