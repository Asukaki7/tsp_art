import os
import numpy as np
import pandas as pd

# path处填入npy文件具体路径
input_file = 'handled_pictur/task1-6700-stipple.tsp.npy'

# 从输入文件路径中提取文件名和扩展名
filename, ext = os.path.splitext(input_file)

# 将npy文件的数据格式转化为csv格式
np_to_csv = pd.DataFrame(data=np.load(input_file))

# 创建一个新的dataframe，第一行为x和y
new_df = pd.DataFrame([['x', 'y']])

# 将新的dataframe和原来的dataframe拼接起来，忽略原来的索引
new_df = pd.concat([new_df, np_to_csv], ignore_index=True)

# 生成输出文件路径，与输入文件在同一目录下，扩展名为.csv
output_file = os.path.join(os.path.dirname(input_file), filename + '.csv')

# 存入具体目录下的np_to_csv.csv 文件，第一行为x和y
new_df.to_csv(output_file, index=False, header=False)
