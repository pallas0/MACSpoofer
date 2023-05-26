

# MAC Spoofer

This is a simple MAC spoofer program written in Python. It allows you to change the MAC (media access card) address of a network interface on your computer.  I built this to get around pay walls that track visits through server-side tracking, where deleting cookies wouldn't be enough.  It should provide increased internet anonymity without the hassle and cost of a VPN.

## Requirements

This program requires Python 3 and the optparse module. If you don't have optparse installed, you can install it using pip:

```
pip install optparse
```

## Usage

To run the program, open a terminal and navigate to the directory where the program is located. Then, run the following command:

```
sudo python3 MACspoofer.py -i [interface] -m [new MAC address]
```

Replace `[interface]` with the name of the network interface you want to spoof (e.g. en0 on macOS or eth0 on Linux), and replace `[new MAC address]` with the MAC address you want to use.

## Example

```
sudo python3 MACspoofer.py -i en0 -m 00:11:22:33:44:55
```

This will spoof the MAC address of the en0 interface to 00:11:22:33:44:55.

## Debugging Notes

- If you're using macOS, replace `wlan0` with `en0` in the program code.
- If you encounter any issues or errors, try running the program with the `-h` option to see the help message and available options.

## Disclaimer

This program is intended for educational purposes only. Use at your own risk. The author is not responsible for any damages caused by the use of this program.
