# rp-button
Python script for detecting a button event and triggering a POST

The project was made with a Raspberry Pi 3 (Raspbian 9 "Stretch"), solderless breadboard, 4-pin button, 2 wires and a 100 Ohm (±5% tolerance) resistor.

Connect the red wire to pin 1 on the Raspberry Pi and to A8 on the breadboard.
Add the resistor to D8 and D12
Add the button at E12 and E14
Connect the blue wire from A14 to pin 10 on the Raspberry Pi


Before running the script:
$ sudo apt-get install python-rpi.gpio python3-rpi.gpio
