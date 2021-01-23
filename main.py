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

df = pd.read_csv('data/new_data.csv')
st.image('img/img2.png', width=695)
choices = {1: 'Events per Year',
2: 'Events by Country',
3: 'Fighters Divisions',
4: 'Fight Win By',
6: 'Men vs Women Distribution '}

def format_func(option):
    return choices[option]

option = st.multiselect('Chose the charts that you are interested in', options=list(choices.keys()), format_func=format_func)


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


#Divisions
fig3 = plt.figure(figsize=(16,8))
sns.countplot(y=df['weight_class'],palette='magma')
sns.set(style='white')
plt.title('Fighters Divisions')


#by fight win
values = df['win_by'].value_counts()
labels = values.index
fig4 = plt.figure(figsize=(16,8))
plt.title('UFC Fight Win By')
sns.barplot(x=values,y=labels,palette='magma')



#men & women fights
women = df.weight_class.str.contains('Women')
women1 = len(df[women])
men = (len(df['weight_class'])) - len(df[women])

labels = 'Men Fights', 'Women Fights'
sizes = [men, women1]
explode = (0, 0.1)

fig6 = fig6, ax3 = plt.subplots(figsize=(16,8))
ax3.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%', shadow=False, startangle=45)
plt.title('Men vs Women')
ax3.axis('equal')


#Charts function
def back_multi(option):
    for x in option:
        if x == 1:
            st.pyplot(fig1)
        elif x == 2:
            st.pyplot(fig2)
        elif x == 3:
            st.pyplot(fig3)
        elif x == 4:
            st.pyplot(fig4)
        elif x == 6:
            st.pyplot(fig6)

back_multi(option)
