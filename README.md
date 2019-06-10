adxl345-python
==============

### Note
This is library and scripts to run four ADXL345 accelerometers using a Raspberry Pi and display/save result on a remote PC. 

You have to enable second (software) i2c bus in Raspbian adding line to `/boot/config.txt`:

```
dtoverlay=i2c-gpio,bus=3
```

For every bus you have connect two ADXL345, one configured at address `0x1d` and second at `0x53`.

The script uses UDP protocol to send data over a network. Log into RPi using ssh and run the script:

    python adxludp.py 192.168.8.109
    
where `192.168.8.109` is your PC's IP. On the PC edit the `UDP_IP` variable inside the `udpplot.py` script.
