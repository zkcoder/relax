import csv
import matplotlib.pyplot as plt
import numpy as np
temp = []

with open('score5.csv', encoding='utf-8-sig') as f:
    for row in csv.reader(f, skipinitialspace=True):
        temp.append(row)

print(temp)

c = []
for i in range(5):
    count = 0
    for j in range(3):
        count = int(temp[j * 5 + i][1]) + count
    c.append(count)

for i in range(5):
    count = 0
    for j in range(30, 60):
        count = int(temp[j * 5 + i][1]) + count
    c.append(count)
for i in range(5):
    count = 0
    for j in range(60, 90):
        count = int(temp[j * 5 + i][1]) + count
    c.append(count)
print(c)
for i in range(5):
    count = 0
    for j in range(90, 120):
        count = int(temp[j * 5 + i][1]) + count
    c.append(count)
print(c)
plt.figure(figsize=(5, 4))
# 构造x轴刻度标签、数据
labels = ['1', '2', '3', '4', '5']
first =[c[0]/30, (c[0]+c[1])/60, (c[0]+c[1]+c[2])/90, (c[0]+c[1]+c[2]+c[3])/120, (c[0]+c[1]+c[2]+c[3]+c[4])/150]
second =[c[5]/30, (c[5]+c[6])/60, (c[5]+c[6]+c[7])/90, (c[5]+c[6]+c[7]+c[8])/120, (c[5]+c[6]+c[7]+c[8]+c[9])/150]
third =[c[10]/30, (c[10]+c[11])/60, (c[10]+c[11]+c[12])/90, (c[10]+c[11]+c[12]+c[13])/120, (c[10]+c[11]+c[12]+c[13]+c[14])/150]
fourth =[c[15]/30, (c[15]+c[16])/60, (c[15]+c[16]+c[17])/90, (c[15]+c[16]+c[17]+c[18])/120, (c[15]+c[16]+c[17]+c[18]+c[19])/150]
# 四组数据
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.2  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
plt.bar(x - 1.5*width, fourth, width, label='Google_t', hatch='', color='white', ec='k')
plt.bar(x - 0.5*width, first, width, label='Atom', hatch='////', color='white', ec='k')
plt.bar(x + 0.5*width, third, width, label='Combine',hatch='....', color='white', ec='k')
plt.bar(x + 1.5*width, second, width, label='SWT', hatch='xxxx', color='white', ec='k')
plt.ylim(75, 100)
plt.ylabel('average score')
plt.xlabel("number of sample")

# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend()
# plt.savefig("myplot4.pdf", dpi=300)
plt.show()


