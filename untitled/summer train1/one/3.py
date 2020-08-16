

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas
from shapely.geometry import Point,Polygon,shape
shp = r'shapefile/sz.shp'
sz = geopandas.GeoDataFrame.from_file(shp,encoding = 'utf-8')
# sz1=sz.iloc[0:1] 这里拆分只能一行一行拆
print(sz)
sz.plot()
# sz1.plot()
plt.show()

