import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5, 4))
# 构造x轴刻度标签、数据
labels = ['1','2','3','4','5','6','7','8','9','10']
first =[90.22222222222223, 96.66666666666667, 95.05555555555556, 82.72727272727273, 85.91666666666667, 81.18181818181819, 89.0909090909091, 83.75, 88.92857142857143, 86.0]
second =[91.3, 92.72727272727273, 95.15789473684211, 84.0, 87.83333333333333, 83.38095238095238, 91.56521739130434, 91.0, 90.38461538461539, 85.6]
third =[90.11111111111111, 92.57142857142857, 95.0952380952381, 84.11111111111111, 86.58823529411765, 81.45, 90.72727272727273, 91.1304347826087, 90.0, 86.08333333333333]
fourth =[87.23809523809524, 91.6470588235294, 94.77272727272727, 83.08333333333333, 85.91666666666667, 83.43333333333334, 80.33333333333333, 84.625, 86.66666666666667,0]

# 四组数据
# plt.subplot(133)
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.2  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中


plt.bar(x - 1.5*width, fourth, width, label='Google_t', hatch='', color='white', ec='k')
plt.bar(x - 0.5*width, first, width, label='Atom', hatch='////',color='white',ec='k')
plt.bar(x + 0.5*width, third, width, label='Combine', hatch='....',color='white',ec='k')
plt.bar(x + 1.5*width, second, width, label='SWT', hatch='xxxx',color='white',ec='k')
plt.ylim(75,100)
plt.ylabel('average score')
plt.xlabel('worker id')


# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend()
#plt.savefig("myplot1.pdf", dpi=300)
plt.show()