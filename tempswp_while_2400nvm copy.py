import socket
import time
import numpy as np
import matplotlib.pyplot as plt

#Fridge - connected via Trition software
from pymeasure.instruments.oxfordinstruments.Oxford_combined import Oxford
Oxford = Oxford()
Oxford.connect()

#nanovoltmeter
from pymeasure.instruments.keithley import Keithley2182
nvm = Keithley2182("GPIB::7")

#Keithley2400
from pymeasure.instruments.keithley import Keithley2000, Keithley2400
source = Keithley2400("GPIB::21")


### Test connections ###
Oxford.get_temp_T8()
source.voltage
float(nvm.voltage)
source.output = 1

### Set up ###
nvm.beep_state = 'disabled'
source.source_current = 100e-9
source.source_current = 0

#initalize arrays
tarray = [] #saved temps
voltage2 = [] #voltage from source
voltage = [] #voltage measured by nvm
tarray_R = [] #resistance measurement from fridge
tick3 = []
currentt = Oxford.get_temp_T8() #current fridge temp

#measure till reaches end point -- use until the set function is working...
start = time.time()
while (currentt > 0.01):
    tarray = np.append(tarray, Oxford.get_temp_T8())
    tarray_R = np.append(tarray_R, float(Oxford.get_res_T8()[25:-4]))
    voltage = np.append(voltage, float(nvm.voltage))
    voltage2 = np.append(voltage2, float(source.voltage))
    tick3 = np.append(tick3, float(time.time()-start))
    currentt = Oxford.get_temp_T8()
    time.sleep(10)

source.source_current = 0
data = np.asarray([tarray, tarray_R, voltage, voltage2,tick3])
data = np.transpose(data)

np.savetxt('temp_sweep1.txt', data, fmt='%.18e', delimiter=' ', newline='\r\n')

plt.plot(tarray, np.abs(voltage))
plt.show()
