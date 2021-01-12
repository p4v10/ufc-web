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
plt.title('UFC Event Per Year')
st.pyplot(fig1)
