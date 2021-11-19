from bs4 import BeautifulSoup
from pandas.core.base import DataError
import requests
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from streamlit_metrics import metric, metric_row


def load_data():
    data = pd.read_csv(
        'C:/Users/Hari/Desktop/Strive School/Build Weeks/Build Week1/Project_Webscraping/pre_data.csv'
    )
    return data


# Read in the cereal data
data = load_data()

st.title('BEST BIOGRAPHIES')
st.dataframe(data)


add_selectbox = st.sidebar.selectbox("FIND YOU BEST AUTHOR",("AUTHOR"), ('BOOK'))
      
    

