from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import socket
import datetime

UDP_IP = "192.168.8.109" # port PC nie RPi
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="AKCELOMETRY")
win.resize(1000,600)
win.setWindowTitle('Akcelometry')

rng=2

p1 = win.addPlot(title="Nr 1")
p1.enableAutoRange('x', True)
p1.enableAutoRange('y', False)
p1.setYRange(-rng,rng)
p1.invertX(True)
curvex1 = p1.plot(pen='r')
curvey1 = p1.plot(pen='g')
curvez1 = p1.plot(pen='b')
adata = np.zeros([600])

ptr = 0

p2 = win.addPlot(title="Nr 2")
p2.enableAutoRange('x', True)
p2.enableAutoRange('y', False)
p2.setYRange(-rng,rng)
p2.invertX(True)
curvex2 = p2.plot(pen='r')
curvey2 = p2.plot(pen='g')
curvez2 = p2.plot(pen='b')

win.nextRow()

p3 = win.addPlot(title="Nr 3")
p3.enableAutoRange('x', True)
p3.enableAutoRange('y', False)
p3.setYRange(-rng,rng)
p3.invertX(True)
curvex3 = p3.plot(pen='r')
curvey3 = p3.plot(pen='g')
curvez3 = p3.plot(pen='b')

p4 = win.addPlot(title="Nr 4")
p4.enableAutoRange('x', True)
p4.enableAutoRange('y', False)
p4.setYRange(-rng,rng)
p4.invertX(True)
curvex4 = p4.plot(pen='r')
curvey4 = p4.plot(pen='g')
curvez4 = p4.plot(pen='b')

now = datetime.datetime.now()
startdate = now.strftime("%Y-%m-%d %H:%M")

def update():
    global curvex1, curvey1, curvez1, curvex2, curvey2, curvez2, curvex3, curvey3, curvez3, curvex4, curvey4, curvez4, adata, p1, ptr
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print "received message:", data
    with open('log'+startdate+'.txt','ab') as f:
        f.write(data+'\n')
        
    values =  data.split(" ")
    #print values
    for v in range(len(values)):
        adata[v] = float(values[v])
        
    #np.savetxt('test.csv', adata, delimiter=" ")
    adata = np.roll(adata, len(values))

    ptr = ptr + len(values)
    if ptr >= 600:
        ptr = 0
        
    curvex1.setData(adata[0::len(values)])
    curvey1.setData(adata[1::len(values)])
    curvez1.setData(adata[2::len(values)])
    curvex2.setData(adata[3::len(values)])
    curvey2.setData(adata[4::len(values)])
    curvez2.setData(adata[5::len(values)])
    curvex3.setData(adata[6::len(values)])
    curvey3.setData(adata[7::len(values)])
    curvez3.setData(adata[8::len(values)])
    curvex4.setData(adata[9::len(values)])
    curvey4.setData(adata[10::len(values)])
    curvez4.setData(adata[11::len(values)])

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(20)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()
