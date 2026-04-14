import streamlit as st
import pandas as pd
import numpy as np
from data.filtered_data import load_data
from tab_components.price_and_size import price_distribution_chart, size_distribution_chart, property_type_chart, property_size_price_plot
from tab_components.location import price_per_sqft_state_chart, price_city, median_age_locality_chart, bhk_dis_city, top_localities_chart
from tab_components.feature_relationship import feature_correlation_heatmap
from utils.filters import filter, sidebar_filters


    
# Load sidebar first to set filters
with st.sidebar:
    sidebar_filters()

# Filtered Data based on sidebar filters 
df = load_data(filter)

st.write("# Dashboard")

price_size_analysis, location_analysis, feature_rel_corr = st.tabs([
    "Price & Size", "Location", "Feature Relationships"
])

with price_size_analysis:
    with st.container(border=True):
        price_distribution_chart(df)

    with st.container(border=True):
        property_size_price_plot(df)

    col1, col2 = st.columns(2, border=True)
    with col1:
        size_distribution_chart(df)
    with col2:
        property_type_chart(df)
    

with location_analysis:
    with st.container(border=True):
        price_per_sqft_state_chart(df)

    col1, col2 = st.columns([1.5, 1], border=True)
    with col1:
        top_localities_chart(df)

    with st.container(border=True):
        price_city(df)
    
    with col2:
        median_age_locality_chart(df)

    with st.container(border=True):
        bhk_dis_city(df)
        
with feature_rel_corr:
    with st.container(border=True):
        feature_correlation_heatmap(df)
