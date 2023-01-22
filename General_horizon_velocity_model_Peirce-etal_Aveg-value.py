"""
Created on Thu Aug 30 12:58:47 2018

@author: cao757
This is a code for the generation of velocity files for the JC132 data sets 
which has seideswipes and could not be used for velocity analysis.
"""

#Transfering vmat_vel_cdp into netCDF4 for input to CLaritas


from __future__ import division

import numpy as np

import matplotlib.pyplot as plt

"""Enter the file path for seafloor horizon times digitized from data set fro line of interest"""

seafloor_HorTime = np.loadtxt("file path")

"""
Seafloor horizon times is in micro seconds therefore the division by 1000.
These times are at each cdp. Therefore its length will give the number of CDPs.
TO generalise the script more a request for sampling time interval of interest
will be asked. 0.008 for Claritas vel files or 0.002 for other vel file. 
"""
depth_time = seafloor_HorTime/1000
s_time = input("Enter 0.008 for a CLaritas vel file or 0.002 for others:  ")

Velocities = [] 
'''list of all velocities for use in the velocity file''' 

def tm1(t1):  # time relating to TWT (Peirce etal 2019) definition for the first L1.1 cdp depth from grid file
    t1 = np.arange(0, 0.235294118, float(s_time)) #0.008)
    return t1
def vel1(v1):
    v1 = np.linspace(2750., 4250., len(tm1(1)))
    return v1
    
Velocities.extend(list(vel1(1)))

def tm2(t2): #Time definiotion for the subsequent part of velocity plot
    t2 = np.arange(0.24, 0.620836286, float(s_time)) 
    return t2
def vel2(v2):
    v2 = np.linspace(4269.94680851, 5187.5, len(tm2(2)))
    return v2
    
Velocities.extend(list(vel2(2)))

def tm3(t3): #last part of velocity time plot
    t3 = np.arange(0.624, 1.142575417, float(s_time)) 
    return t3
def vel3(v3):
    v3 = np.linspace(5196.2890625, 5750., len(tm3(3)))
    return v3

Velocities.extend(list(vel3(3)))

def tm4(t4): #last part of velocity time plot
    t4 = np.arange(1.144, 1.802369231, float(s_time)) 
    return t4
def vel4(v4):
    v4 = np.linspace(5753.81097561, 6062.5, len(tm4(4)))
    return v4

Velocities.extend(list(vel4(4)))

def tm5(t5): #last part of velocity time plot
    t5 = np.arange(1.808, 2.586682957, float(s_time)) 
    return t5
def vel5(v5):
    v5 = np.linspace(6065.72164948, 6375., len(tm5(5)))
    return v5

Velocities.extend(list(vel5(5)))

def tm6(t6): #last part of velocity time plot
    t6 = np.arange(2.592, 3.492343334, float(s_time)) 
    return t6
def vel6(v6):
    v6 = np.linspace(6377.23214286, 6625., len(tm6(6)))
    return v6

Velocities.extend(list(vel6(6)))

def tm7(t7): #last part of velocity time plot
    t7 = np.arange(3.496, 4.539072306, float(s_time)) 
    return t7
def vel7(v7):
    v7 = np.linspace(6625.48076923, 6687.5, len(tm7(7)))
    return v7

Velocities.extend(list(vel7(7)))

def tm8(t8): #last part of velocity time plot
    t8 = np.arange(4.544, 5.724257491, float(s_time)) 
    return t8
def vel8(v8):
    v8 = np.linspace(6687.92517007, 6750., len(tm8(8)))
    return v8

Velocities.extend(list(vel8(8)))

def tm9(t9): #last part of velocity time plot
    t9 = np.arange(5.728, 7.047786903, float(s_time)) 
    return t9
def vel9(v9):
    v9 = np.linspace(6750.30487805, 6800., len(tm9(9)))
    return v9

Velocities.extend(list(vel9(9)))

def tm10(t10): #last part of velocity time plot
    t10 = np.arange(7.048, 8.507640918, float(s_time)) 
    return t10
def vel10(v10):
    v10 = np.linspace(6800.27472527, 6850., len(tm10(10)))
    return v10

Velocities.extend(list(vel10(10)))

count5 = 0

no_cdp = len(depth_time) 

line_name = input("Enter the Line name to do ideal velocity model for :  ")

line_total_time = input("Enter the total time in seconds for line of interest:   ")

no_vel = int((float(line_total_time))/(float(s_time))) + 1     

mat_vel_cdp = np.ones((no_vel , no_cdp))

for CDPpoint in range(no_cdp): #total CDPpoint extracted from the seismic data
    count1 = 0 # count import os.pathfor totaltime in sesimc data at 0.002 smaple rate
    count2 = 0
    count3 = 0
    count4 = 0
    totaltime = [0]
    modelvel = [1500]
    vel = 1500
    while totaltime[count1] <= float(line_total_time) :
        if totaltime[count1] <= depth_time[count5] :
            vel = 1500
        else:
            vel = Velocities[count2]
            count2 += 1
            
            
        num = totaltime[count1] + float(s_time)   
        totaltime.append(num)
        modelvel.append(vel)
        mat_vel_cdp[count3][count5] *= modelvel[count4]
        count1 += 1
        count3 += 1
        count4 += 1
    count5 += 1
 

plt.figure(figsize=[20, 10], dpi=(70))
plt.imshow(mat_vel_cdp, interpolation='nearest',origin='lower', extent=[1000,5972,0,9500])
plt.xlabel('CDP')
plt.ylabel('Time (s)')
plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()
plt.colorbar()
plt.show()

'''new matrix generation for the interval velocity matrix using a list method
and appending these in the full matrix. The velocities for the matrix is 
extendeded in a list from all the velocities-time function above'''

save_path = 'path to file location for saving'

"""
## Save_path give the location the appended filename will be written to this could be any location of choice
"""
np.savetxt(str(save_path), mat_vel_cdp, fmt='%2f')



"""
### Converting matrix to netCDF4 file for read into Claritas
"""


save_path = 'file path name'+ str(line_name) +'_Intvel_model_arrays'+ str(s_time)+ '.nc'
## save_path will replace the filename which should be the first object in Dataset  

from netCDF4 import Dataset

model_grp = Dataset(str(save_path) , 'w', format='NETCDF3_CLASSIC')
model_grp.Title = "2-D earth model"

Vint_model_array = mat_vel_cdp.copy()


cdp_ndim = no_cdp # size of the matrix column
time_ndim = no_vel  # size of the matrix row

cdp_dim = 6.25 * no_cdp

time_dim = float(s_time) * no_vel


"""Dimension (instead and cdp = ELevation while time = Distance)"""
model_grp.createDimension('Elevation', time_ndim)
model_grp.createDimension('Distance', cdp_ndim)


#variables
velocity = model_grp.createVariable('Velocity', 'f4', ('Elevation', 'Distance',))
velocity.Units = "m/s"
velocity.X_Limits_and_increment = 1000.000, float(cdp_ndim + 1000),  1.000
velocity.X_name = "CDP"
velocity.X_units = "" 
velocity.Z_Limits_and_increment = 0.000, float((float(s_time)) * no_vel), float(s_time)
velocity.Z_name = "Time"
velocity.Z_units = "ms"
velocity.V_name = "Velocity"
velocity.V_units = "m/s"


# Data
cdp_range = np.linspace(0, cdp_dim, cdp_ndim)
time_range = np.linspace(0, time_dim, time_ndim)

Vint_model_array_transpose = Vint_model_array.transpose()
velocity[:,:] = Vint_model_array_transpose.reshape(time_ndim,cdp_ndim)

model_grp.close()



#
'''Conversion of mat_vel_cdp Vint to model_vrms Vrms'''
#

import math as mat
import numpy as np

model_vrms = np.ones(((no_vel ), no_cdp))

model_vint = mat_vel_cdp.copy()

count1 = 0

time_dim = float(line_total_time)

for cdp_point in range(no_cdp):
    count2 = 0
    total_time = 0.0
    vel_time_sum = 0.0
    vel_num = 0.0
    while total_time <= time_dim:
        int_time = float(s_time)
        vel_dino = model_vint[count2][count1]
        vel_dino_sqr = (model_vint[count2][count1]) ** 2
        vel_sqr_time = vel_dino_sqr * int_time
        vel_time_sum +=  vel_sqr_time
        vel_num += int_time
        total_time += float(s_time)    #0.008
        vel_sqrt = vel_time_sum/vel_num
        model_vrms[count2][count1] = mat.sqrt(vel_sqrt)
        count2 += 1
    count1 += 1
    

plt.figure(figsize=[20, 10], dpi=(70))
plt.imshow(model_vrms, interpolation='nearest',origin='lower', extent=[1000,5972,0,9500])
plt.xlabel('CDP')
plt.ylabel('Time (s)')
plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()
plt.colorbar()
plt.show()

np.savetxt(str(line_name) +'model_Vrms_'+ str(s_time)+ '.txt', model_vrms, fmt='%2f')



"""Converting model_vrms matrix to netCDF4 file for read into Claritas"""


from netCDF4 import Dataset

save_path = 'file path name'+ str(line_name) +'_model_Vrms_arrays_'+ str(s_time)+ '.nc'

model_vrms_grp = Dataset(str(save_path), 'w', format='NETCDF3_CLASSIC')
model_vrms_grp.Title = "2-D earth model Vrms"

#model_array_vrms = model_vrms.copy()
model_vrms_array = model_vrms.copy()
cdp_ndim = no_cdp # size of the matrix column
time_ndim = (no_vel) # size of the matrix row


# Dimension (instead and cdp = ELevation while time = Distance)
model_vrms_grp.createDimension('Elevation', time_ndim)
model_vrms_grp.createDimension('Distance', cdp_ndim )


#variables
velocity = model_vrms_grp.createVariable('Velocity', 'f4', ('Elevation', 'Distance',))
velocity.Units = "m/s"
velocity.X_Limits_and_increment = 1000.000, float(cdp_ndim + 1000),  1.000
velocity.X_name = "CDP"
velocity.X_units = "" 
velocity.Z_Limits_and_increment = 0.000, float(float(s_time) * no_vel), float(s_time)
velocity.Z_name = "Time"
velocity.Z_units = "ms"
velocity.V_name = "Velocity"
velocity.V_units = "m/s"


# Data
cdp_range = np.linspace(0, cdp_dim, cdp_ndim)
time_range = np.linspace(0, time_dim, time_ndim)


model_vrms_array_transpose = model_vrms_array.transpose()
velocity[:,:] = model_vrms_array_transpose.reshape(time_ndim,cdp_ndim)

model_vrms_grp.close()

##
"""Cascaded migration velocity flow calculated from intertval velocity for FDMIG"""
##

import math as mat

second_mig_Intvel = np.ones((no_vel,no_cdp))

stolt_mig_vel = (np.ones((no_vel,no_cdp))) * 1480

count1 = 0
count2 = 0

while count1 !=  no_vel:
    mat_vel_element = (mat_vel_cdp[count1][count2]) ** 2 #cascaded Velocity elemnet from interval velocity
    stolt_vel = 1480 ** 2
    second_mig_intvel_elem = mat_vel_element - stolt_vel
    second_mig_Intvel[count1][count2] = mat.sqrt(second_mig_intvel_elem)
    count1 += 1
    if count1 == no_vel:
        count2 += 1
        count1 = 0
    if count2 == no_cdp:
        break
    
plt.figure(figsize=(25,5))
plt.imshow(second_mig_Intvel, interpolation='nearest')
plt.colorbar()
plt.show()



"""##converting second cascade model Vint to netCDF4 for read into Claritas"""


from netCDF4 import Dataset

save_path = 'file path name'+ str(line_name) +'_model_SecCascade-IntVel_arrays_'+ str(s_time)+ '.nc'

model_Sec_Intvel_grp = Dataset(str(save_path), 'w', format='NETCDF3_CLASSIC')
model_Sec_Intvel_grp.Title = "2-D earth model second cacade InterVel"

Sec_mig_Intvel_model_array = second_mig_Intvel.copy()

cdp_ndim = no_cdp  # size of the matrix column
time_ndim = (no_vel) # size of the matrix row

cdp_dim = 6.25 * no_cdp
time_dim = float(s_time) * no_vel

""" Dimension (instead and cdp = ELevation while time = Distance)"""
model_Sec_Intvel_grp.createDimension('Elevation', time_ndim)
model_Sec_Intvel_grp.createDimension('Distance', cdp_ndim)


#variables
velocity = model_Sec_Intvel_grp.createVariable('Velocity', 'f4', ('Elevation', 'Distance',))
velocity.Units = "m/s"
velocity.X_Limits_and_increment = 1000.000, float(cdp_ndim + 1000),  1.000
velocity.X_name = "CDP"
velocity.X_units = "" 
velocity.Z_Limits_and_increment = 0.000, float(float(s_time) * no_vel), float(s_time)
velocity.Z_name = "Time"
velocity.Z_units = "ms"
velocity.V_name = "Velocity"
velocity.V_units = "m/s"


# Data
cdp_range = np.linspace(0, cdp_dim, cdp_ndim)
time_range = np.linspace(0, time_dim, time_ndim)


Sec_mig_Intvel_model_array_transpose = Sec_mig_Intvel_model_array.transpose()
velocity[:,:] = Sec_mig_Intvel_model_array_transpose.reshape(time_ndim,cdp_ndim)


model_Sec_Intvel_grp.close()

