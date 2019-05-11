import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point

import pptk

file_name = "data/colonge_small/dom1l-fp_32356_5645_1_nw.xyz"

#read the file into a numpy array

lidar_points = np.loadtxt(open(file_name, "r"), delimiter=",", skiprows=0)

color = np.array(np.zeros((lidar_points.shape[0], 3)))

for i in range(0, int(lidar_points.shape[0])) :
    color[i][0] = 1

v = pptk.viewer(lidar_points, color)