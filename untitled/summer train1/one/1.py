import pandas as pd
#读取数据
data = pd.read_csv(r'data-sample/TaxiData-Sample',header = None)
#给数据命名列
data.columns = ['VehicleNum', 'Stime', 'Lng', 'Lat', 'OpenStatus', 'Speed']
#显示数据的前5行
data.head(5)
# 将数据排序,并把排序后的数据赋值给原来的数据
data = data.sort_values(by = ['VehicleNum','Stime'])
data.head(5)
#筛选前的数据量
print(len(data))

data = data[-((data['OpenStatus'].shift(-1) == data['OpenStatus'].shift())&
(data['OpenStatus'].shift(-1) != data['OpenStatus'])&
(data['VehicleNum'].shift(-1) == data['VehicleNum'].shift())&
(data['VehicleNum'].shift(-1) == data['VehicleNum']))]

#如果你代码对的话，筛选完了data的数据量应该是
print(len(data))

#让这几个字段的下一条数据赋值给新的字段，在字段名加个1，代表后面一条数据的值
data.loc[:,'OpenStatus1'] = data['OpenStatus'].shift(-1)
data.loc[:,'VehicleNum1'] = data['VehicleNum'].shift(-1)
data.loc[:,'Lng1'] = data['Lng'].shift(-1)
data.loc[:,'Lat1'] = data['Lat'].shift(-1)
data.loc[:,'Stime1'] = data['Stime'].shift(-1)

data.loc[:,'StatusChange'] = data['OpenStatus1']-data['OpenStatus']

data = data[((data['StatusChange'] == 1)|(data['StatusChange'] == -1))
&(data['VehicleNum'] == data['VehicleNum1'])]

#data数据只保留一些我们需要的字段
data = data[['VehicleNum','Stime','Lng','Lat','StatusChange']]

data = data.rename(columns = {'Lng':'SLng','Lat':'SLat'})
data['ELng'] = data['SLng'].shift(-1)
data['ELat'] = data['SLat'].shift(-1)
data['Etime'] = data['Stime'].shift(-1)
data = data[data['StatusChange'] == 1]
data = data.drop('StatusChange',axis = 1)

print(data.head(5))