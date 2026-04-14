import streamlit as st
import pandas as pd

@st.cache_data
def load_data(filter_dict):
    data = pd.read_csv('../Datasets/Future_Price.csv')
    # Apply filters from the filter dictionary
    for key, value in filter_dict.items():
        if value is not None:
            # Handle range filters (tuples)
            if isinstance(value, tuple):
                data = data[(data[key] >= value[0]) & (data[key] <= value[1])]
            # Handle multiselect filters (lists)
            elif isinstance(value, list):
                data = data[data[key].isin(value)]
            # Handle single value filters
            else:
                data = data[data[key] == value]
    return data