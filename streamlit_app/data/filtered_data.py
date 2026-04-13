import streamlit as st
import pandas as pd

@st.cache_data
def load_data(filter_dict):
    data = pd.read_csv('../Datasets/Future_Price.csv')
    # Apply filters from the filter dictionary
    for key, value in filter_dict.items():
        if value is not None:
            data = data[data[key] == value]
    return data