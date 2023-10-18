import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5, 4))
# 构造x轴刻度标签、数据
labels = ['MV', 'DS', 'HDS', 'GLAD']
a=[30/90, 56/90, 34/90, 33/90]
b=[40/90, 77/90, 13/90, 56/90]
c=[54/90, 62/90, 28/90, 67/90]
d=[58/90, 58/90, 32/90, 72/90]

# 四组数据
#plt.subplot(133)
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.2  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中


plt.bar(x - 1.5*width, a, width, label='Google_t',hatch='',color='white',ec='k')
plt.bar(x - 0.5*width, b, width, label='Atom',hatch='////',color='white',ec='k')
plt.bar(x + 0.5*width, c, width, label='Combine',hatch='....',color='white',ec='k')
plt.bar(x + 1.5*width, d, width, label='SWT',hatch='xxxx',color='white',ec='k')
plt.ylim(0,1)
plt.ylabel('proportion')
plt.xlabel('translation mode')


# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend()
#plt.savefig("myplot1.pdf", dpi=300)
plt.show()

