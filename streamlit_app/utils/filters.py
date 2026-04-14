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
    st.write("## Location Filters")
    state_filter(df)
    city_filter(df[df['State'] == filter.get('State', df['State'].iloc[0])])
    locality_filter(df)
    st.divider()
    st.write("## Property Details")
    property_type_filter(df)
    bhk_filter(df)
    size_filter()
    

def state_filter(df):
    state_options = sorted(df['State'].unique())
    selected_state = st.selectbox(
        "State", 
        state_options,
        index=None
    )
    filter['State'] = selected_state

def city_filter(df):
    city_options = sorted(df['City'].unique())
    selected_city = st.multiselect(
        "City", 
        city_options,
        default=[]
    )
    filter['City'] = selected_city if selected_city else None

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

def bhk_filter(df):
    bhk_options = sorted(df['BHK'].unique())
    selected_bhk = st.slider(
        "BHK", 
        min_value=int(min(bhk_options)),
        max_value=int(max(bhk_options)),
        value=int(min(bhk_options))
    )
    filter['BHK'] = selected_bhk

def size_filter():
    selected_size = st.slider(
        "Size (in sqft)", 
        min_value=500,
        max_value=5000,
        value=(500, 5000),
        step=100
    )
    filter['Size_in_SqFt'] = selected_size