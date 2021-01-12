import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title='UFC')

st.write("""
### Predicting who win the fight
""")

st.write("""
In this project we are going to use `Random Forest` to predict the winner of the fight.
""")

st.write("""
This dataset is imported [Kaggle](https://www.kaggle.com/rajeevw/ufcdata). Cointains a list of every UFC fight from 1993 to 2019.
""")


st.image('img/img2.png', width=695)

st.multiselect('Chose the charts that you are interested in', options=['dasda','asdasd','dasdasd','adsad','dasdas','dasdasd'])
