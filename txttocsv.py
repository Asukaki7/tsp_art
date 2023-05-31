import csv

with open('node.txt') as f:
    lines = f.readlines()

res = []
for i, line in enumerate(lines):
    line = line.strip()
    nums = line.split(' ')
    nums.insert(0, str(i+1))  #将行号插入到列表的第一个位置
    nums.pop(1)  #删除重复的行号
    res.append(nums)

with open('node.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['行号', '数据1', '数据2'])
    writer.writerows(res)