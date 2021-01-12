import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='UFC')

st.write("""
### Predicting who win the fight
""")

st.write("""
In this project we are going to use `Random Forest` to predict the winner of the fight.
""")

st.write("""
This dataset is imported from [Kaggle](https://www.kaggle.com/rajeevw/ufcdata). Cointains a list of every UFC fight from 1993 to 2019.
""")


st.image('img/img2.png', width=695)

chart_p = st.multiselect('Chose the charts that you are interested in', options=['Events per Year','asdasd','dasdasd','adsad','dasdas','dasdasd'])


df = pd.read_csv('data/new_data.csv')

# Ufc events per year
values = df['date_year'].sort_values(ascending=False).value_counts().sort_index()
labels = values.index

clrs = ['navy' if (y < max(values)) else 'black' for y in values]

fig1 = plt.figure(figsize=(16,8))
bar = sns.barplot(x=labels, y=values, palette='magma')

ax=plt.gca()
y_max = values.max()
ax.set_ylim(1)
for p in ax.patches:
    ax.text(p.get_x() + p.get_width()/2., p.get_height(), p.get_height(),
           fontsize=12, color='black', ha='center', va='bottom')
plt.xlabel('Year')
plt.ylabel('Quantity of fights')
plt.title('UFC Events Per Year')
st.pyplot(fig1)

#Events by country
fig2 = plt.figure(figsize=(16,8))
bar = sns.countplot(df['country'], palette='magma')
plt.xticks(rotation=90)
ax = plt.gca()
y_max = df['country'].value_counts().max()
ax.set_ylim(1)
for p in ax.patches:
    ax.text(p.get_x() + p.get_width()/2., p.get_height(), p.get_height(),
           fontsize=10, color='black', ha='center', va='bottom')

plt.title('Event by Country')
st.pyplot(fig2)


#Divisions
fig4 = plt.figure(figsize=(16,8))
sns.countplot(y=df['weight_class'],palette='magma')
sns.set(style='white')
plt.title('Fighters Divisions')
st.pyplot(fig4)


#by fight win
values = df['win_by'].value_counts()
labels = values.index
fig5 = plt.figure(figsize=(16,8))
plt.title('UFC Fight Win By')
sns.barplot(x=values,y=labels,palette='magma')
st.pyplot(fig5)

#outcome by division
bar = df.groupby(['weight_class', 'win_by']).size().reset_index().pivot(columns='win_by', index='weight_class', values=0)
bar.plot(kind='barh', stacked=True, figsize=(16,8))
plt.legend(bbox_to_anchor=(1.23, 0.99), loc=1, borderaxespad=0.)
plt.title('UFC Fight Outcome by Division')
plt.ylabel('Division')
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)










#men & women fights
women = df.weight_class.str.contains('Women')
women1 = len(df[women])
men = (len(df['weight_class'])) - len(df[women])

labels = 'Men Fights', 'Women Fights'
sizes = [men, women1]
explode = (0, 0.1)

fig3 = fig3, ax3 = plt.subplots(figsize=(16,8))
ax3.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%', shadow=False, startangle=45)
ax3.axis('equal')
st.pyplot(fig3)
