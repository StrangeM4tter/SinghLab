"""

This is a generic code to measure resistance using DC Keithley 2400 and nvm

"""

### Import ###

import numpy as np
import time
import matplotlib.pyplot as plt

from pymeasure.instruments.keithley import Keithley2400
source = Keithley2400("GPIB::21")

from pymeasure.instruments.keithley import Keithley2182
nvm = Keithley2182("GPIB::7")

### Setup 2400 ###

currentmax = .1e-6
currentmin = 0
currentstep = 1e-9
currentrange =  int((currentmax-currentmin)/currentstep+1)

source.apply_current()
source.measure_voltage()

source.source_current = 0
float(source.source_current)
float(source.voltage)
float(nvm.voltage)

## initalize array ##
current = []
voltage = []
voltage2 = []
setcurrent = currentmin

for i in range(currentrange):
    source.source_current = setcurrent
    voltage = np.append(voltage, float(nvm.voltage))
    voltage2 = np.append(voltage2, float(source.voltage))
    current = np.append(current, float(source.source_current))
    setcurrent = setcurrent + currentstep

IVsweep = np.asarray([current,voltage,voltage2])
IVsweep = np.transpose(IVsweep)

np.savetxt("Al_wire_Iswp_4.txt", IVsweep, fmt='%.18e', delimiter=' ', newline=';\r\n')

plt.plot(current,np.abs(voltage))

source.source_current = 0
float(source.source_current)
float(source.voltage)
float(nvm.voltage)

voltagezero = []
voltage2zero = []

for i in range(1000):
    voltagezero = np.append(voltagezero, float(nvm.voltage))
    voltage2zero = np.append(voltage2zero, float(source.voltage))

zero = np.asarray([voltagezero,voltage2zero])
zero = np.transpose(zero)

np.savetxt("Al_wire_zero.txt", zero, fmt='%.18e', delimiter=' ', newline=';\r\n')
np.mean(voltagezero)
