import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()      # 子图


# 封装一下这个函数，用来后面生成数据
def list_generator(mean, dis, number):
    return np.random.normal(mean, dis * dis, number)  # normal分布，输入的参数是均值、方差以及生成的数量


# 我们生成四组数据用来做实验，数据量分别为70-100

sentence = [84.6,86,90.8,89.8,86.4,86.2,92.4,86.6,86,86.8,87.2,86,85.2,83,88.4,81.6,87.6,88.8,90.2,90.6,84.8,90.8,89.4,90.8,88.4,87.6,86.2,87.4,88.8,85.2]
min_cut = [86.4,87.8,88.6,94.2,87,92,90.2,92,89.8,94,90,92.4,87.2,90,90,86.8,90.4,86.8,91,90,89.4,87.6,86.6,91.2,89.6,91.6,90.4,91.2,90.6,85.8]
combine = [89,85.4,88.4,94.4,89.2,92,93.2,88,87.4,89,88.2,91.2,86.6,86.4,90.4,89.6,89.2,86.2,87.2,92,89,87.4,85.4,86.8,91.6,90,87.4,87,91.8,88.4]
google = [87.8,88,84.6,89.6,86.4,90.4,85.2,88,86,85.2,89.4,86.8,81.4,87.4,80.6,87.4,87.4,87.8,90,89.4,85.6,87.4,87,90.4,88.8,85.8,90.2,89.8,82,85.8]



data = [google,sentence, combine, min_cut ]
ax.boxplot(data)
ax.set_xticklabels(["Google_t","Atom", "Combine",  "SWT"])# 设置x轴刻度标签
plt.xlabel("方法")
plt.ylabel("平均分")
#plt.savefig("myplot2.pdf", dpi=300)
plt.show()
