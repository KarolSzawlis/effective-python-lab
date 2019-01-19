import pandas as pd

''' read data from the file US_Baby_Names_right.csv from the lab12_files directory'''
baby_names = pd.read_csv('US_Baby_Names_right.csv')
#file = open('lab09_files/US_Baby_Names_right.csv', 'r') Golisz
'''suspects the first 10 records from the set'''
print(baby_names.head(10))
'''delete columns  'Unnamed: 0' and 'Id'''
baby_names = baby_names.drop(axis=1, labels=['Id', 'Unnamed: 0'])
'''Is there more names of women or men in the collection?'''
print(baby_names.groupby('Gender').Gender.count())
#pd.DataFrame(baby_names.groupby(['Name', 'Gender']).count()).groupby('Gender').sum().Count goliszewski
''' group the poems to names and list the 10 most-frequent names.'''
print(baby_names.groupby('Name').Name.count().sort_values(ascending=False).head(10))

'''
the results from Step 6 will be presented on the graph using matplotlib.
Prepare three graphs, ie the 10 most common names: total, in men and women.'''
from matplotlib import pyplot as plt
allnames = baby_names.groupby('Name')['Name','Count'].sum().sort_values(ascending=False, by='Count').head(10)
print(allnames)
#mnames = baby_names[baby_names.Gender == 'M'].groupby('Name')['Name','Count'].sum().sort_values(ascending=False).head(10)
#fnames = baby_names[baby_names.Gender == 'F'].groupby('Name')['Name','Count'].sum().sort_values(ascending=False).head(10)
# print(allnames.keys)
# plt.bar(allnames.values, allnames.values)
allnames.plot.bar()
# mnames.plot.bar()
# fnames.plot.bar()
'''How many different names do you have in your collection?'''
print(baby_names.Name.nunique())
'''
Prepare the name generator, drawing them according to the probability distribution received on the basis of the processed file
'''
import random
import numpy as np
names = baby_names.groupby('Name').count().cumsum()
s = names.Count
def generate_name(baby_names):
    return s[s == min(s[s>random.randint(0,max(s))])].keys().values[0]
print(generate_name(baby_names))



'''
What is the most common name?
Determine the mean, median and standard deviation of the names.
'''
names_with_val = baby_names.groupby('Name').Name.count().sort_values(ascending=False)
print(names_with_val.head(1))
print(names_with_val.mean())
print(names_with_val.median())
print(names_with_val.std())

'''Step 1: Load the data'''
df = pd.DataFrame(pd.read_csv('ocupation.csv', sep='|'))
#df=pd.read_csv('lab09_files/ocupation.csv', sep='|')
'''Step 2: Look at the first 25 records'''
print(df.head(25))
'''Step 3: Look at the last 10 records'''
print(df.tail(10))
'''Step 4: How many observations is in the set? How many columns are in the set?'''
print(df.shape[0])
print(df.shape[1])
'''
print(len(df))
print(len(df.columns))
'''
'''Step 5: List the column names'''
print(df.columns.values)
'''Step 6: How many different professions are in the set?'''
print(df.occupation.nunique())
'''Step 7: prepare an effective graph on which you will present a percentage share
  individual professions in the set
  on charplet Use https://matplotlib.org/examples/pie_and_polar_charts/pie_demo_features.html'''
import matplotlib.pyplot as plt
labels = df.occupation.unique()
sizes = df.groupby('occupation').occupation.count()
fig1, ax1 = plt.subplots()
ax1.pie(sizes.values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

df2 = df.replace(sizes.sort_values(ascending=False).index[10:], 'other')
labels = df2.occupation.unique()
sizes = df2.groupby('occupation').occupation.count()
fig2, ax2 = plt.subplots()
ax2.pie(sizes.values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
'''Step 8: Prepare an effective chart on which you will present the top 10 professions
  and how many women work in them and how many men
  Use https://matplotlib.org/gallery/api/barchart.html#sphx-glr-gallery-api-barchart-py'''
import numpy as np
import matplotlib.pyplot as plt

men_occ = df2[df2.gender == 'M'].groupby(['occupation']).occupation.count()
women_occ = df2[df2.gender == 'F'].groupby(['occupation']).occupation.count()

ind = np.arange(len(men_occ))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12,12))
rects1 = ax.bar(ind - width/2, men_occ.values, width,
                color='SkyBlue', label='Men')
rects2 = ax.bar(ind + width/2, women_occ.values, width,
                color='IndianRed', label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(men_occ.keys())
ax.legend()
print(men_occ.keys()==women_occ.keys())