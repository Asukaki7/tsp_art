import pandas as pd
import os
from pyCombinatorial.algorithm import nearest_insertion
from pyCombinatorial.utils import graphs, util

ORIGIN_CSV="flag_logo-7500-stippletest.tsp.csv"
coordinates = pd.read_csv(ORIGIN_CSV, sep = ',')
# convert the coordinates to numeric values
coordinates = coordinates.apply(pd.to_numeric)
coordinates = coordinates.values
distance_matrix = util.build_distance_matrix(coordinates)

parameters = {
            'initial_location': -1, # -1 =  Try All Locations.
            'verbose': True
             }
route, distance = nearest_insertion(distance_matrix, **parameters)

# 获取输入文件的目录和文件名
output_dir, filename = os.path.split(ORIGIN_CSV)

# 修改文件名为.txt扩展名
output_filename = os.path.splitext(filename)[0] + '-tour.txt'


output_path = os.path.join(output_dir, output_filename)

graphs.plot_tour(coordinates, city_tour = route, view = 'browser', size = 10)
print(route)
print('Total Distance: ', round(distance, 2))


# 使用os.path.join()函数生成输出文件路径
# 写入输出文件
with open(output_path, 'w') as f:
    for i in range(len(route)):
        f.write(' '.join(str(route[i])) +'->')





