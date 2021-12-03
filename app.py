import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import collections
from matplotlib import gridspec
import plotly.express as px


from termcolor import colored

import warnings
warnings.filterwarnings("ignore")
@st.cache

def load_csv():
    dfloaddata = pd.read_csv('netflix_titles.csv', index_col='show_id')
    df = pd.DataFrame(dfloaddata)
    return df

df = load_csv()

# main points
st.title('NETFLIX Visual Anaylsis')

analysis = ("""
   -- Analysis for Netflix Show and TV Show.
    
    Note: Analysis for Netflix Show
""")

st.write(analysis)

###dashboard options for the sidebar
#st.sidebar.title("netflix Dashboard")
options = st.sidebar.selectbox("Select a Menu Option to display:", 
                                   ('movie V/s TVshow', 'top 10 country with most movies'))
    
# displays headers fore each dashboard
st.header(options)

print(df['type']);
if options == 'movie V/s TVshow':
    fig = go.Figure(
    go.Pie(
    labels = ['Movie','TV Show'],
    values = [round(df['type'].value_counts()[0]/df['type'].count()*100,2),round(df['type'].value_counts()[1]/df['type'].count()*100,2)],
    hoverinfo = "label+percent",
    textinfo = "value"
    ))
    st.plotly_chart(fig)
    

if options == 'top 10 country with most movies':
    print(df['first_country'].value_counts())
    print()
    dict = {'Country': df['first_country'].unique()[:85],
            'No of Movies': df['first_country'].value_counts()}
    
    df1 = pd.DataFrame(dict)
    
    fig = px.bar(        
        df1,
        x = "Country",
        y = "No of Movies",
        title = "Bar Graph"
    )
    st.plotly_chart(fig)
