### Import ###

import numpy as np
import time
import matplotlib.pyplot as plt
import pyvisa as visa
import socket

from pymeasure.instruments.keithley import Keithley2400
from pymeasure.instruments.keithley import Keithley2000
from pymeasure.instruments.lakeshore import LakeShore331

from lakeshore425 import Lakeshore425

rm = visa.ResourceManager()
rm.list_resources()

## GPIB Connect ##
#Check the GPIB address and fill in correct one#
nvm = Keithley2000("GPIB::8")
source = Keithley2400("GPIB::18")
lakeshore = LakeShore331("GPIB::12")

### Setup nvm ###

### Setup 2400 ###

setcurrent = 1e-8

source.apply_current()
print(nvm.voltage)
nvm.beep_state = 'disabled'

source.source_current = setcurrent
source.source_current
### Setup Temperature Sweep ###
tempfinal = 4.0


## initalize array ##
current = []
voltage = []
temperature = []

lakeshore.temperature_A
lakeshore.setpoint_1 = 300

#Sweeping -- note will need to switch while condition to > if sweeping down and < if sweeping up
while currenttemp < tempfinal:
    current = np.append(current, float(source.source_current))
    voltage = np.append(voltage, float(nvm.voltage))
    temperature = np.append(temperature, float(lakeshore.temperature_A))
    currenttemp = lakeshore.temperature_A

#plotting
plt.plot([temperature,voltage])
plt.show()

#Saving
Tsweep = np.asarray([temperature,current,voltage])
Tsweep = np.transpose(Tsweep)

plot(temperature, current/voltage)

#Change save file name!
np.savetxt("data.txt", Tsweep, fmt='%.18e', delimiter=' ', newline=';\r\n')
