import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r'data-sample/TaxiData-Sample',header = None)
data.columns = ['VehicleNum', 'Stime', 'Lng', 'Lat', 'OpenStatus', 'Speed']
TaxiOD = pd.read_csv(r'data-sample/TaxiOD.csv')
TaxiOD.columns = ['VehicleNum', 'Stime', 'SLng', 'SLat', 'ELng', 'ELat','Etime']
data['Hour'] = data['Stime'].str.slice(0,2)

hourcount = data.groupby('Hour')['VehicleNum'].agg(np.size)
print(hourcount)

hourcount1= data.groupby(data['Stime'].apply(lambda r:r[:2]))['VehicleNum'].count().reset_index()
print(hourcount1)

import seaborn as sns
# sns.set_style('darkgrid',{"xtick.major.size": 10 , "ytick.major.size": 10})
#
# fig = plt.figure(1,(8,4),dpi = 250)
# ax = plt.subplot(111)
# plt.sca(ax)  #这两行也可以用 plt.subplot(111),一样的
# plt.plot(hourcount1['Stime'],hourcount1['VehicleNum'],'k-',hourcount1['Stime'],hourcount1['VehicleNum'],'k.')
# plt.bar(hourcount1['Stime'],hourcount1['VehicleNum'],width =0.5)
#
# plt.title('Hourly data Volume')
# plt.ylim(0,80000)
# plt.ylabel('Data volumn')
# plt.xlabel('Hour')
# plt.show()

print(TaxiOD.size)

TaxiOD = TaxiOD[-TaxiOD['Etime'].isnull()]

print(TaxiOD.size)

TaxiOD['order_time'] = TaxiOD['Etime'].str.slice(0,2).astype('int')*3600+\
TaxiOD['Etime'].str.slice(3,5).astype('int')*60+\
TaxiOD['Etime'].str.slice(6,8).astype('int')-\
TaxiOD['Stime'].str.slice(0,2).astype('int')*3600-\
TaxiOD['Stime'].str.slice(3,5).astype('int')*60-\
TaxiOD['Stime'].str.slice(6,8).astype('int')

TaxiOD['Hour'] = TaxiOD['Stime'].str.slice(0,2)

fig     = plt.figure(1,(10,5),dpi = 250)
ax      = plt.subplot(111)
plt.sca(ax)


sns.boxplot(x="Hour", y=TaxiOD["order_time"]/60, data=TaxiOD,ax = ax)

plt.ylabel('Order time(minutes)')
plt.xlabel('Order start time')
plt.ylim(0,60)


plt.show()