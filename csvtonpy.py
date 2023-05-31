import numpy as np
import csv

embedding_vec = np.zeros((7600, 2))

with open('flag_logo-7500-stipple.tsp.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  #跳过标题行
    index = 0
    for row in reader:
        nums = [num for num in row[0:]]
        embedding_vec[index] = nums
        index += 1

np.save('node_emb.npy', embedding_vec)
test = np.load('node_emb.npy')

print(test)