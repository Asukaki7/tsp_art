# 导入matplotlib.pyplot库
import matplotlib.pyplot as plt

# 打开txt文档，以只读模式，指定编码为utf-8
f = open("handled_pictur/handled_tsp/flag_logo-7500-stipple.tsp", "r", encoding="utf-8")

# 初始化两个空列表，用于存储x和y值
x_list = []
y_list = []

# 逐行读取文档中的数据
for line in f:
    # 去除每行末尾的换行符
    line = line.strip()
    # 将每一行按空格分割，得到序号、x和y值的字符串列表
    num, x, y = line.split()
    # 将x和y值转换为浮点数，并添加到对应的列表中
    x_list.append(float(x))
    y_list.append(float(y))

# 关闭文档
f.close()

# 调用plot()函数，绘制线图，指定线条颜色和宽度等参数
plt.plot(x_list, y_list, color="black", linewidth=2)

# 显示图像
plt.show()
