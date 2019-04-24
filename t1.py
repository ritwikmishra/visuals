import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns

white_wine = pd.read_csv('winequality-white.csv', sep=';')
red_wine = pd.read_csv('winequality-red.csv', sep=';')

# store wine type as an attribute
red_wine['wine_type'] = 'red'   
white_wine['wine_type'] = 'white'

# bucket wine quality scores into qualitative quality labels
red_wine['quality_label'] = red_wine['quality'].apply(lambda value: 'low' 
                                                          if value <= 5 else 'medium' 
                                                              if value <= 7 else 'high')
red_wine['quality_label'] = pd.Categorical(red_wine['quality_label'], 
                                           categories=['low', 'medium', 'high'])
white_wine['quality_label'] = white_wine['quality'].apply(lambda value: 'low' 
                                                              if value <= 5 else 'medium' 
                                                                  if value <= 7 else 'high')
white_wine['quality_label'] = pd.Categorical(white_wine['quality_label'], 
                                             categories=['low', 'medium', 'high'])

# merge red and white wine datasets
wines = pd.concat([red_wine, white_wine])

# re-shuffle records just to randomize data points
wines = wines.sample(frac=1, random_state=42).reset_index(drop=True)

print wines.head()

subset_attributes = ['residual sugar', 'total sulfur dioxide', 'sulphates', 
                     'alcohol', 'volatile acidity', 'quality']
rs = red_wine[subset_attributes].describe()
ws = white_wine[subset_attributes].describe()

print pd.concat([rs, ws], axis=1, keys=['Red Wine Statistics', 'White Wine Statistics'])


# wines.hist(bins=15, color='steelblue', edgecolor='black', linewidth=1.0,
#            xlabelsize=8, ylabelsize=8, grid=False)    
# plt.tight_layout(rect=(0, 0, 1, 1)) 

# Histogram
# fig = plt.figure(figsize = (6,4))
# title = fig.suptitle("Sulphates Content in Wine", fontsize=14)
# fig.subplots_adjust(top=0.85, wspace=0.3)

# ax = fig.add_subplot(1,1, 1)
# ax.set_xlabel("Sulphates")
# ax.set_ylabel("Frequency") 
# ax.text(1.2, 800, r'$\mu$='+str(round(wines['sulphates'].mean(),2)), 
#          fontsize=12)
# freq, bins, patches = ax.hist(wines['sulphates'], color='steelblue', bins=15,
#                                     edgecolor='black', linewidth=1)
                                    

# # Density Plot
# fig = plt.figure(figsize = (6, 4))
# title = fig.suptitle("Sulphates Content in Wine", fontsize=14)
# fig.subplots_adjust(top=0.85, wspace=0.3)

# ax1 = fig.add_subplot(1,1, 1)
# ax1.set_xlabel("Sulphates")
# ax1.set_ylabel("Frequency") 
# sns.kdeplot(wines['sulphates'], ax=ax1, shade=True, color='steelblue')

# # Bar Plot
# fig = plt.figure(figsize = (6, 4))
# title = fig.suptitle("Wine Quality Frequency", fontsize=14)
# fig.subplots_adjust(top=0.85, wspace=0.3)

# ax = fig.add_subplot(1,1, 1)
# ax.set_xlabel("Quality")
# ax.set_ylabel("Frequency") 
# w_q = wines['quality'].value_counts()
# w_q = (list(w_q.index), list(w_q.values))
# ax.tick_params(axis='both', which='major', labelsize=8.5)
# bar = ax.bar(w_q[0], w_q[1], color='steelblue', 
# edgecolor='black', linewidth=1)

# # Correlation Matrix Heatmap
# f, ax = plt.subplots(figsize=(10, 6))
# corr = wines.corr()
# hm = sns.heatmap(corr, annot=True, ax=ax, cmap="coolwarm",fmt='.2f',
#                  linewidths=.05)
# f.subplots_adjust(top=0.93)
# t= f.suptitle('Wine Attributes Correlation Heatmap', fontsize=14)

# # Pair-wise Scatter Plots
# cols = ['density', 'residual sugar', 'total sulfur dioxide', 'fixed acidity']
# pp = sns.pairplot(wines[cols], height=1.8, aspect=1.8,
#                   plot_kws=dict(edgecolor="k", linewidth=0.5),
#                   diag_kind="kde", diag_kws=dict(shade=True))

# fig = pp.fig 
# fig.subplots_adjust(top=0.93, wspace=0.3)
# t = fig.suptitle('Wine Attributes Pairwise Plots', fontsize=14)

# # Scaling attribute values to avoid few outiers
# cols = ['density', 'residual sugar', 'total sulfur dioxide', 'fixed acidity']
# subset_df = wines[cols]

# # sudo apt-get install python-sklearn 
# from sklearn.preprocessing import StandardScaler
# ss = StandardScaler()

# scaled_df = ss.fit_transform(subset_df)
# scaled_df = pd.DataFrame(scaled_df, columns=cols)
# final_df = pd.concat([scaled_df, wines['wine_type']], axis=1)
# final_df.head()

# # plot parallel coordinates
# from pandas.plotting import parallel_coordinates
# pc = parallel_coordinates(final_df, 'wine_type', color=('#FFE888', '#FF9999'))

# # Scatter Plot
# plt.scatter(wines['sulphates'], wines['alcohol'],
#             alpha=0.4, edgecolors='w')

# plt.xlabel('Sulphates')
# plt.ylabel('Alcohol')
# plt.title('Wine Sulphates - Alcohol Content',y=1.05)


# # Joint Plot
# jp = sns.jointplot(x='sulphates', y='alcohol', data=wines,
# kind='reg', space=0, height=5, ratio=4)

# # Using subplots or facets along with Bar Plots
# fig = plt.figure(figsize = (10, 4))
# title = fig.suptitle("Wine Type - Quality", fontsize=14)
# fig.subplots_adjust(top=0.85, wspace=0.3)
# # red wine - wine quality
# ax1 = fig.add_subplot(1,2, 1)
# ax1.set_title("Red Wine")
# ax1.set_xlabel("Quality")
# ax1.set_ylabel("Frequency") 
# rw_q = red_wine['quality'].value_counts()
# rw_q = (list(rw_q.index), list(rw_q.values))
# ax1.set_ylim([0, 2500])
# ax1.tick_params(axis='both', which='major', labelsize=8.5)
# bar1 = ax1.bar(rw_q[0], rw_q[1], color='red', 
#                edgecolor='black', linewidth=1)

# # white wine - wine quality
# ax2 = fig.add_subplot(1,2, 2)
# ax2.set_title("White Wine")
# ax2.set_xlabel("Quality")
# ax2.set_ylabel("Frequency") 
# ww_q = white_wine['quality'].value_counts()
# ww_q = (list(ww_q.index), list(ww_q.values))
# ax2.set_ylim([0, 2500])
# ax2.tick_params(axis='both', which='major', labelsize=8.5)
# bar2 = ax2.bar(ww_q[0], ww_q[1], color='white', 
# edgecolor='black', linewidth=1)

# # Multi-bar Plot
# cp = sns.countplot(x="quality", hue="wine_type", data=wines, 
# palette={"red": "#FF9999", "white": "#FFE888"})

# # facets with histograms
# fig = plt.figure(figsize = (10,4))
# title = fig.suptitle("Sulphates Content in Wine", fontsize=14)
# fig.subplots_adjust(top=0.85, wspace=0.3)

# ax1 = fig.add_subplot(1,2, 1)
# ax1.set_title("Red Wine")
# ax1.set_xlabel("Sulphates")
# ax1.set_ylabel("Frequency") 
# ax1.set_ylim([0, 1200])
# ax1.text(1.2, 800, r'$\mu$='+str(round(red_wine['sulphates'].mean(),2)), 
#          fontsize=12)
# r_freq, r_bins, r_patches = ax1.hist(red_wine['sulphates'], color='red', bins=15,
#                                      edgecolor='black', linewidth=1)

# ax2 = fig.add_subplot(1,2, 2)
# ax2.set_title("White Wine")
# ax2.set_xlabel("Sulphates")
# ax2.set_ylabel("Frequency")
# ax2.set_ylim([0, 1200])
# ax2.text(0.8, 800, r'$\mu$='+str(round(white_wine['sulphates'].mean(),2)), 
#          fontsize=12)
# w_freq, w_bins, w_patches = ax2.hist(white_wine['sulphates'], color='white', bins=15,
#                                      edgecolor='black', linewidth=1)


# # facets with density plots
# fig = plt.figure(figsize = (10, 4))
# title = fig.suptitle("Sulphates Content in Wine", fontsize=14)
# fig.subplots_adjust(top=0.85, wspace=0.3)

# ax1 = fig.add_subplot(1,2, 1)
# ax1.set_title("Red Wine")
# ax1.set_xlabel("Sulphates")
# ax1.set_ylabel("Density") 
# sns.kdeplot(red_wine['sulphates'], ax=ax1, shade=True, color='r')

# ax2 = fig.add_subplot(1,2, 2)
# ax2.set_title("White Wine")
# ax2.set_xlabel("Sulphates")
# ax2.set_ylabel("Density") 
# sns.kdeplot(white_wine['sulphates'], ax=ax2, shade=True, color='y')

# # Using multiple Histograms 
# fig = plt.figure(figsize = (6, 4))
# title = fig.suptitle("Sulphates Content in Wine", fontsize=14)
# fig.subplots_adjust(top=0.85, wspace=0.3)
# ax = fig.add_subplot(1,1, 1)
# ax.set_xlabel("Sulphates")
# ax.set_ylabel("Frequency") 

# g = sns.FacetGrid(wines, hue='wine_type', palette={"red": "r", "white": "y"})
# g.map(sns.distplot, 'sulphates', kde=False, bins=15, ax=ax)
# ax.legend(title='Wine Type')
# plt.close(2)

# # Box Plots
# f, (ax) = plt.subplots(1, 1, figsize=(12, 4))
# f.suptitle('Wine Quality - Alcohol Content', fontsize=14)

# sns.boxplot(x="quality", y="alcohol", data=wines,  ax=ax)
# ax.set_xlabel("Wine Quality",size = 12,alpha=0.8)
# ax.set_ylabel("Wine Alcohol %",size = 12,alpha=0.8)

# # Violin Plots
# f, (ax) = plt.subplots(1, 1, figsize=(12, 4))
# f.suptitle('Wine Quality - Sulphates Content', fontsize=14)

# sns.violinplot(x="quality", y="sulphates", data=wines,  ax=ax)
# ax.set_xlabel("Wine Quality",size = 12,alpha=0.8)
# ax.set_ylabel("Wine Sulphates",size = 12,alpha=0.8)

plt.show()