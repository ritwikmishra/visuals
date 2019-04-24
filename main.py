# Inspired from
# https://towardsdatascience.com/the-art-of-effective-visualization-of-multi-dimensional-data-6c7202990c57
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns
import datetime


file_name = "tdata.xlsx"
clist = ['blue', 'green', 'red', 'yellow', 'cyan', 'magenta', 'purple', 'orange', 'khaki', '#4d847f','#83844d', '#844d4d', '#4d8453', '#4d5384',]
mlist = ['o','v','s','P','D','*','X','p','<','>','h','H']
ndata = pd.read_excel(file_name) #sudo pip install xlrd
pd.set_option('display.width', 250)
print "\t\tPLOTTING 10 NUMERICAL ATTRIBUTES AT A TIME"
print "\tDon't forget to change the file_name in the source code. Current file_name is \""+file_name+"\""
print "\tDon't forget to save the generated images"
print "\tAll the legends will be saved in a file called legends.txt"
dtstring = str(datetime.datetime.now()).replace('.',':')
file = open("legends.txt",'a')
file.write("Test conducted on: "+dtstring+"\n")
ndata = ndata.sample(frac=1, random_state=42).reset_index(drop=True)

# ndata = ndata[:400]
print "Description of the dataset in "+file_name+" is as follows:"
print ndata.describe(percentiles = [0.10, 0.25, 0.50, 0.75, 0.90])
print "\nSome top values of dataset are as follows:"
print ndata.head()

# print len(ndata)
# raw_input()



################################## Dimension build up STARTS ######################################
print "\tAll the values are case sensitive"
xaxis = raw_input('Enter x-axis attribute name: ')
file.write("X-axis = '"+xaxis+"' attribute\n")
yaxis = raw_input('Enter y-axis attribute name: ')
file.write("Y-axis = '"+yaxis+"' attribute\n")
zaxis = raw_input('Enter z-axis attribute name: ')
file.write("Z-axis = '"+zaxis+"' attribute\n")

xs = list(ndata[xaxis])
ys = list(ndata[yaxis])
zs = list(ndata[zaxis])

data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]

# -----		------		------		------		------		------		------		------

facet = raw_input('Enter facet attribute: ')
lcut = [ndata[facet].min()]
cuts = int(raw_input('\t\tHow many cuts do you want? '))
ch = raw_input('\t\tEnter boundary values manually or automatically (m/a)? ')
if 'a' in ch:
	lcut = [0.0]
	k=0
	while k<cuts:
		lcut.append(1.0/cuts + lcut[len(lcut)-1])
		k+=1
	lcut = list(ndata[facet].quantile(lcut))
else:
	lcut = [0.0]
	if cuts>1:
		print "Enter "+str(cuts-1)+" values for cutting"
		k=0
		while k<cuts-1:
			lcut.append(float(raw_input('\t\tEnter value'+str(k+1)+': ')))
			k+=1
	lcut.append(ndata[facet].max())
lcut[-1] = lcut[-1] + 0.001

if 'a' in ch:
	ch = "automatically"
else:
	ch = "manually"

file.write("There will be "+str(cuts)+" diagrams containing all the boundary values of '"+facet+"' attribute generated "+ch+"\n")

# -----		------		------		------		------		------		------		------

sz = raw_input('\nEnter attribute for size of the point: ')
scut = int(raw_input('\t\tEnter number of categories you want in size of the point: '))
ml = [0.0]
ch = raw_input('\t\tEnter boundary values manually or automatically (m/a)? ')
if 'a' in ch:
	k=0
	while k<scut:
		ml.append(1.0/scut + ml[len(ml)-1])
		k+=1
	ml = ml[1:]
	ml = list(ndata[sz].quantile(ml))
else:
	k=0
	ml = []
	while k<scut-1:
		ml.append(float(raw_input('\t\tEnter categories boundary '+str(k+1)+': ')))
		k+=1

ss = []
for x in list(ndata[sz]):
	k=0
	while k<len(ml):
		if x <= ml[k]:
			ss.append(10+((k+1)*2 -1)*10)
			break
		k+=1

if 'a' in ch:
	ch = "automatically"
else:
	ch = "manually"

file.write("Size of the points depends on '"+sz+"' attribute "+ch+"\n")
k=0
while k<len(ml):
	file.write("\tIf "+sz+".value() < "+str(ml[k])+"\tthen\tPoint size = "+str(10+((k+1)*2 -1)*10)+"\n")
	k+=1

# -----		------		------		------		------		------		------		------


sz = raw_input('\nEnter attribute for color of the point: ')
scut = int(raw_input('\t\tEnter number of categories you want in color of the point: '))
ml = [0.0]
ch = raw_input('\t\tEnter boundary values manually or automatically (m/a)? ')
if 'a' in ch:
	k=0
	while k<scut:
		ml.append(1.0/scut + ml[len(ml)-1])
		k+=1
	ml = ml[1:]
	ml = list(ndata[sz].quantile(ml))
else:
	k=0
	ml = []
	while k<scut-1:
		ml.append(float(raw_input('\t\tEnter categories boundary '+str(k+1)+': ')))
		k+=1
colors = []
for x in list(ndata[sz]):
	k=0
	while k<len(ml):
		if x <= ml[k]:
			colors.append(clist[k])
			break
		k+=1

if 'a' in ch:
	ch = "automatically"
else:
	ch = "manually"

file.write("Color of the points depends on '"+sz+"' attribute "+ch+"\n")
k=0
while k<len(ml):
	file.write("\tIf "+sz+".value() < "+str(ml[k])+"\tthen\tPoint color = "+clist[k]+"\n")
	k+=1

# -----		------		------		------		------		------		------		------

sz = raw_input('\nEnter attribute for color of the point edge:')
scut = int(raw_input('\t\tEnter number of categories you want in color of the point edge: '))
clist.reverse()
ml = [0.0]
ch = raw_input('\t\tEnter boundary values manually or automatically (m/a)? ')
if 'a' in ch:
	k=0
	while k<scut:
		ml.append(1.0/scut + ml[len(ml)-1])
		k+=1
	ml = ml[1:]
	ml = list(ndata[sz].quantile(ml))
else:
	k=0
	ml = []
	while k<scut-1:
		ml.append(float(raw_input('\t\tEnter categories boundary '+str(k+1)+': ')))
		k+=1
ec = []
for x in list(ndata[sz]):
	k=0
	while k<len(ml):
		if x <= ml[k]:
			ec.append(clist[k])
			break
		k+=1

if 'a' in ch:
	ch = "automatically"
else:
	ch = "manually"

file.write("Color of the point edge depends on '"+sz+"' attribute "+ch+"\n")
k=0
while k<len(ml):
	file.write("\tIf "+sz+".value() < "+str(ml[k])+"\tthen\tcolor of the point edge = "+clist[k]+"\n")
	k+=1

# -----		------		------		------		------		------		------		------

sz = raw_input('\nEnter attribute for marker of the point: ')
scut = int(raw_input('\t\tEnter number of categories you want in marker of the point: '))
ml = [0.0]
ch = raw_input('\t\tEnter boundary values manually or automatically (m/a)? ')
if 'a' in ch:
	k=0
	while k<scut:
		ml.append(1.0/scut + ml[len(ml)-1])
		k+=1
	ml = ml[1:]
	ml = list(ndata[sz].quantile(ml))
else:
	k=0
	ml = []
	while k<scut-1:
		ml.append(float(raw_input('\t\tEnter categories boundary '+str(k+1)+': ')))
		k+=1
markers = []
for x in list(ndata[sz]):
	k=0
	while k<len(ml):
		if x <= ml[k]:
			markers.append(mlist[k])
			break
		k+=1

if 'a' in ch:
	ch = "automatically"
else:
	ch = "manually"

file.write("Marker of the point depends on '"+sz+"' attribute generated "+ch+"\n")
k=0
while k<len(ml):
	file.write("\tIf "+sz+".value() < "+str(ml[k])+"\tthen\tmarker of the point = "+mlist[k]+"\n")
	k+=1
file.write("\tRefer to https://matplotlib.org/api/markers_api.html#module-matplotlib.markers to see markers and their respective symbols\n")

# -----		------		------		------		------		------		------		------

sz = raw_input('\nEnter attribute for opacity of the point: ')
opaqlist = list(ndata[sz]/ndata[sz].max())
file.write("Opacity of the point depends on '"+sz+"' attribute. All the values are scaled between 0 (transparent) to 1 (opaque) by dividing all by the MAX value\n")

# -----		------		------		------		------		------		------		------

sz = raw_input('\nEnter attribute for width of the point edge: ')
lwl = list(1*(0.7 + ndata[sz]/ndata[sz].max())) # 1.4*( 1 + {0 ... 1} )
file.write("Width of the point edge depends on '"+sz+"' attribute. All the values are scaled between 0.7 to 1.5\n\tRefer to the source code to see the formula.\n")

################################## Dimension build up ENDS ######################################


print "\n\nWait.. Plotting..."

ptr = 1

while ptr <= cuts:
	fig = plt.figure(figsize=(8, 6))
	ax = fig.add_subplot(111, projection='3d')
	
	k=0
	for data, color, size, mark, op, lw, e, f in zip(data_points, colors, ss, markers, opaqlist, lwl, ec, list(ndata[facet])):
		x, y, z = data
		if f >= lcut[ptr-1] and f<lcut[ptr]:
			ax.scatter(x, y, z, alpha=op, c=color, edgecolors=e, s=size, marker=mark, linewidths=lw)
			k+=1
	t = fig.suptitle("Diagram "+str(ptr)+"\n"+str(lcut[ptr-1])+" <= "+facet+" < "+str(lcut[ptr])+"\n"+str(k)+" points\nGenerated on "+dtstring, fontsize=12)
	ax.set_xlabel(xaxis)
	ax.set_ylabel(yaxis)
	ax.set_zlabel(zaxis)
	ax.legend()
	ptr+=1

file.write("\n\t\tImages generated successfully!\n===================================================================\n\n")
file.close()
plt.show()
