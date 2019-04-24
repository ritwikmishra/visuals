import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns


ct1 = 0.25
ct2 = 0.50
ct3 = 0.75
#pd.set_option('display.width', 250)
#sudo pip install xlrd
ef = pd.ExcelFile('graph.xlsx')
print ef.sheet_names
# tdata = pd.read_excel(ef, 'pq0')
# tdata = tdata.sample(frac=1, random_state=42).reset_index(drop=True)
# # tdata = tdata[:1000]
# print tdata.head()
# print tdata.describe()


# fig = plt.figure(figsize=(8, 6))
# t = fig.suptitle('Reliability <= 0.3', fontsize=14)
# ax = fig.add_subplot(111, projection='3d')

# xs = list(tdata['pphf'])
# ys = list(tdata['pc'])
# zs = list(tdata['P(Q0)'])
# data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]
# for data in zip(xs, ys, zs):
# 	x, y, z = data
# 	ax.scatter(x, y, z, alpha=1, c='red', edgecolors='blue', s=20)

# ax.set_xlabel('pphf')
# ax.set_ylabel('pc')
# ax.set_zlabel('P(Q0)')
# ax.legend()


# tdata = pd.read_excel(ef, 'pq1')
# # tdata = tdata[:100]
# fig = plt.figure(figsize=(8, 6))
# t = fig.suptitle('Reliability <= 0.3', fontsize=14)
# ax = fig.add_subplot(111, projection='3d')

# xs = list(tdata['pphf'])
# ys = list(tdata['pphf-sysf'])
# zs = list(tdata['P(Q1)'])
# data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]
# for data in zip(xs, ys, zs):
# 	x, y, z = data
# 	ax.scatter(x, y, z, alpha=1, c='red', edgecolors='blue', s=20)

# ax.set_xlabel('pphf')
# ax.set_ylabel('pphf-sysf')
# ax.set_zlabel('P(Q1)')
# ax.legend()


# tdata = pd.read_excel(ef, 'pq23')
# # tdata = tdata[:100]
# fig = plt.figure(figsize=(8, 6))
# t = fig.suptitle('Reliability <= 0.3', fontsize=14)
# ax = fig.add_subplot(111, projection='3d')

# xs = list(tdata['pc'])
# ys = list(tdata['pc-sysf'])
# zs = list(tdata['P(Q2,3)'])
# data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]
# for data in zip(xs, ys, zs):
# 	x, y, z = data
# 	ax.scatter(x, y, z, alpha=1, c='red', edgecolors='blue', s=20)

# ax.set_xlabel('pc')
# ax.set_ylabel('pc-sysf')
# ax.set_zlabel('P(Q2,3)')
# ax.legend()


# tdata = pd.read_excel(ef, 'pq4')
# fig = plt.figure(figsize=(8, 6))
# t = fig.suptitle('Reliability <= 0.3', fontsize=14)
# ax = fig.add_subplot(111)

# xs = list(tdata['ppsf-sysf'])
# ys = list(tdata['P(Q4)'])
# for data in zip(xs, ys):
# 	x, y = data
# 	ax.scatter(x, y, alpha=1, c='red', edgecolors='blue', s=20)

# ax.set_xlabel('ppsf-sysf')
# ax.set_ylabel('P(Q4)')
# ax.legend()


tdata = pd.read_excel(ef, 'teng')
tdata = tdata[:100]
print(len(tdata))
fig = plt.figure(figsize=(8, 6))
t = fig.suptitle('Reliability <= 0.3', fontsize=14)
ax = fig.add_subplot(111, projection='3d')

xs = list(tdata['pphf'])
ys = list(tdata['phc-sc'])
zs = list(tdata['Teng'])
data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]
for data in zip(xs, ys, zs):
	x, y, z = data
	ax.scatter(x, y, z, alpha=1, c='red', edgecolors='blue', s=50, linewidths=1.1)

ax.set_xlabel('pphf')
ax.set_ylabel('phc-sc')
ax.set_zlabel('Teng')
ax.legend()

plt.show()