from adxl345 import ADXL345
from time import sleep
import socket 
import sys

def main(argv):
    
    UDP_IP = "192.168.8.109"
    UDP_PORT = 5005
    MESSAGE = ""
    
    adxl345 = ADXL345(0x1d, 1) #adress, bus
    adxl345_2 = ADXL345(0x53, 1)
    adxl345s = ADXL345(0x1d, 3)
    adxl345s_2 = ADXL345(0x53, 3)

    if len(sys.argv) > 1 :
        UDP_IP = (sys.argv[1])

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

    while True:
        axes = adxl345.getAxes(True)
        axes_2 = adxl345_2.getAxes(True)
        axess = adxl345s.getAxes(True)
        axess_2 = adxl345s_2.getAxes(True)
    #    print "ADXL345 on address 0x%x:" % (adxl345.address)
    #    print "   x = %.3fG" % ( axes['x'] )
    #    print "   y = %.3fG" % ( axes['y'] )
    #    print "   z = %.3fG" % ( axes['z'] )
    #    print "ADXL345 on address 0x%x:" % (adxl345_2.address)
    #    print "   x = %.3fG" % ( axes_2['x'] )
    #    print "   y = %.3fG" % ( axes_2['y'] )
    #    print "   z = %.3fG" % ( axes_2['z'] )
    #    print "ADXL345 SB on address 0x%x:" % (adxl345s.address)
    #    print "   x = %.3fG" % ( axess['x'] )
    #    print "   y = %.3fG" % ( axess['y'] )
    #    print "   z = %.3fG" % ( axess['z'] )
    #    print "ADXL345 SB on address 0x%x:" % (adxl345s_2.address)
    #    print "   x = %.3fG" % ( axess_2['x'] )
    #    print "   y = %.3fG" % ( axess_2['y'] )
    #    print "   z = %.3fG" % ( axess_2['z'] )

        MESSAGE = "%.3f " % ( axes['x'] ) + "%.3f " % ( axes['y'] ) + "%.3f " % ( axes['z'] ) + "%.3f " % ( axes_2['x'] ) + "%.3f " % ( axes_2['y'] ) + "%.3f " % ( axes_2['z'] ) + "%.3f " % ( axess['x'] ) + "%.3f " % ( axess['y'] ) + "%.3f " % ( axess['z'] ) + "%.3f " % ( axess_2['x'] ) + "%.3f " % ( axess_2['y'] ) + "%.3f" % ( axess_2['z'] )
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        sleep(0.02) # Time in seconds
        


if __name__ == "__main__":
   main(sys.argv[1:])
