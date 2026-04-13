import streamlit as st
import pandas as pd

filter = {}

def sidebar_filters():
    @st.cache_data
    def filter_load_data():
        data = pd.read_csv('../Datasets/Future_Price.csv')
        return data
    df = filter_load_data()

    st.write("# Filters")
    city_filter(df)
    locality_filter(df)
    property_type_filter(df)

def city_filter(df):
    city_options = sorted(df['City'].unique())
    selected_city = st.selectbox(
        "City", 
        city_options,
        index=None
    )
    filter['City'] = selected_city

def locality_filter(df):
    locality_options = sorted(df['Locality'].unique())
    selected_locality = st.selectbox(
        "Locality", 
        locality_options,
        index=None
    )
    filter['Locality'] = selected_locality

def property_type_filter(df):
    property_type_options = sorted(df['Property_Type'].unique())
    selected_property_type = st.selectbox(
        "Property Type", 
        property_type_options,
        index=None
    )
    filter['Property_Type'] = selected_property_type