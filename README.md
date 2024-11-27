# Speed change in GCode

Speed change in GCode for 3D printers (Fxxxx parameter) by a factor.


```
$ python3 ./edit_gcode.py -h

usage: edit_gcode.py [-h] [--multiplier MULTIPLIER] directory

Process G-code files in a directory. Modify the speed of the G-code files by multiplying a factor (default 0.5). This script will create a 'modified' sub-directory in the specified directory and save
the modified files there.

positional arguments:
  directory             The directory containing G-code files.

optional arguments:
  -h, --help            show this help message and exit
  --multiplier MULTIPLIER
                        Speed multiplier.

```
Example:
```
$ python3 ./edit_gcode.py ~/workspace/FPV/3Dprint/Eclipson_MX/G-codes/PLA/ --multiplier 0.5
The sub-directory 'modified' exists in /home/test/G-codes/PLA/
Processing file: /home/test/G-codes/PLA/Horn_x2.gcode
Processing file: /home/test/G-codes/PLA/Prop_hub.gcode
...
Processing file: /home/test/G-codes/PLA/Hinge_x16.gcode
```

![meld window](meld_modified.png)