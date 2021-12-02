import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib import gridspec

from termcolor import colored

import warnings
warnings.filterwarnings("ignore")
@st.cache

def load_csv():
     dfloaddata = pd.read_csv('netflix_titles.csv', index_col='show_id')
     return df

df = load_csv()
# main points
st.title('NETFLIX Visual Anaylsis')

welcome = ("""
    ### Welcome! Use the panel on the left to navigate to different dashboards.
    
    Note: Data represents netflix trends in the United States
""")

st.write(welcome)

###dashboard options for the sidebar
#st.sidebar.title("netflix Dashboard")
options = st.sidebar.selectbox("Select a Menu Option to display:", 
                                   ('movie V/s TVshow', 'top 10 country with most movies', 'other', 'abcd'))
    
# displays headers fore each dashboard
st.header(options)

if options == 'movie V/s TVshow':
    plt.figure(figsize=(10,5))
    plt.pie(df['type'].value_counts().sort_values(),labels=df['type'].value_counts().index,explode=[0.05,0],
    autopct='%1.2f%%',colors=['Green','grey'])
    st.write(plt.show())

if options == 'top 10 country with most movies':
    country_data = df['country']
    country_count = pd.Series(dict(Counter(','.join(country_data).replace(' ,',',').replace(
    ', ',',').split(',')))).sort_values(ascending=False)

    top20country = country_count.head(20)


    fig = plt.figure(figsize=(20, 7))
    gs = gridspec.GridSpec(nrows=1, ncols=2, height_ratios=[6], width_ratios=[10, 5])

    ax = plt.subplot(gs[0])
    sns.barplot(top20country.index, top20country, ax=ax, palette="RdGy")
    ax.set_xticklabels(top20country.index, rotation='90')
    ax.set_title('Top 20 countries with most contents', fontsize=15, fontweight='bold')

    ax2 = plt.subplot(gs[1])
    ax2.pie(top20country, labels=top20country.index, shadow=True, startangle=0, colors=sns.color_palette("RdGy", n_colors=20),
       autopct='%1.2f%%')
    ax2.axis('equal') 

    st.write(plt.show())

