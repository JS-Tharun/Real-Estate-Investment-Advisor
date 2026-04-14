import streamlit as st
import pandas as pd
import numpy as np
from data.filtered_data import load_data
from tab_components.price_and_size import price_parking_chart, price_direction, price_distribution_chart, size_distribution_chart, property_type_chart, property_size_price_plot, price_furnished_chart, price_city_furnished_chart, price_state_direction
from tab_components.location import prop_availability_city, price_per_sqft_state_chart, price_city, median_age_locality_chart, bhk_dis_city, top_localities_chart
from tab_components.feature_relationship import feature_relationship_plots
from tab_components.investment_ownership import owner_type_count, prop_availability, price_public_transport
from utils.filters import filter, sidebar_filters


    
# Load sidebar first to set filters
with st.sidebar:
    sidebar_filters()

# Filtered Data based on sidebar filters 
df = load_data(filter)

st.write("# Dashboard")

price_size_analysis, location_analysis,investment_ownership, feature_rel_corr  = st.tabs([
    "Price & Size", "Location",  "Investment & Ownership", "Feature & Amenity Relationships"
])

with price_size_analysis:
    col1, col2 = st.columns([2,1], border=True)
    with col1:
        price_distribution_chart(df)
    
    with col2:
        price_direction(df)
        
        

    col1, col2 = st.columns([2.5,1], border=True)
    with col1:
        property_size_price_plot(df)
        
    with col2:
        price_parking_chart(df)
        

    col1, col2, col3 = st.columns([2,1,1], border=True)
    with col1:
        size_distribution_chart(df)
    with col2:
        property_type_chart(df)

    with col3:
        price_furnished_chart(df)



with location_analysis:
    with st.container(border=True):
        prop_availability_city(df)
        

    col1, col2 = st.columns([1.5, 1], border=True)
    with col1:
        top_localities_chart(df)

    with st.container(border=True):
        price_city(df)
    
    with col2:
        median_age_locality_chart(df)

    with st.container(border=True):
        bhk_dis_city(df)

    with st.container(border=True):
        price_city_furnished_chart(df)

    with st.container(border=True):
        price_state_direction(df)

    with st.container(border=True):
        price_per_sqft_state_chart(df)
        
with feature_rel_corr:
    with st.container(border=True):
        feature_relationship_plots(df)

with investment_ownership:
    col1, col2, col3 = st.columns([1.5,1.5, 1], border=True)
    with col1:  
        owner_type_count(df)
    with col2:
        price_public_transport(df)
    with col3:
        prop_availability(df)

    