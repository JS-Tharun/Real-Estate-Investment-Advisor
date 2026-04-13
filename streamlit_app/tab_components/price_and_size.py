import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

def price_distribution_chart(df):
    st.write("### Price Distribution")
    st.caption("Distribution of property prices in the dataset")
    bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, np.inf]
    labels = ['0 to 50L', '50L to 1Cr', '1Cr to 1.5Cr', '1.5Cr to 2Cr', '2Cr to 2.5 Cr', '2.5Cr to 3Cr', '3Cr to 3.5Cr', '3.5Cr to 4Cr', '4Cr to 4.5 Cr', '4.5Cr to 5Cr', '5Cr and more']
    price_bucket = pd.cut(df['Price_in_Lakhs'], bins=bins, labels=labels) # (left, right]
    price_bucket_counts = price_bucket.value_counts().sort_index()
    st.bar_chart(
        price_bucket_counts,
        x_label="Price Range",
        y_label="Number of Properties"
    )

def size_distribution_chart(df):
    st.write("### Size Distribution")
    st.caption("Distribution of property sizes in the dataset")
    bins = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, np.inf]
    labels = ['0 to 500', '500 to 1000', '1000 to 1500', '1500 to 2000', '2000 to 2500', '2500 to 3000', '3000 to 3500', '3500 to 4000', '4000 to 4500', '4500 to 5000', '5000 and above']
    size_bucket = pd.cut(df['Size_in_SqFt'], bins=bins, labels=labels)
    size_bucket_counts = size_bucket.value_counts().sort_index()
    st.bar_chart(
        size_bucket_counts,
        x_label="Size Bucket",
        y_label="Property Count"
    )

def property_type_chart(df):
    st.write("### Property Type")
    st.caption("Distribution of different property types in the dataset")
    price_per_sqft_on_type = (df.groupby('Property_Type')['Price_per_SqFt_in_Lakhs']
        .agg(['mean'])
        .reset_index()
        .sort_values('mean')
    )
    price_per_sqft_on_type['mean'] = price_per_sqft_on_type['mean'].round(6) * 100000
    st.bar_chart(
        price_per_sqft_on_type.set_index('Property_Type')['mean'],
        x_label="Property Type",
        y_label="Avg Price (₹)"
    )

def property_size_price_plot(df):
    st.write("### Price Distribution by Size")
    st.caption("Box plot showing the distribution of property prices across different size buckets")
    size_price_df = df[['Size_in_SqFt', 'Price_in_Lakhs']].copy()
    bins = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, np.inf]
    labels = ['0 to 500', '500 to 1000', '1000 to 1500', '1500 to 2000', '2000 to 2500', '2500 to 3000', '3000 to 3500', '3500 to 4000', '4000 to 4500', '4500 to 5000', '5000 and above']
    size_price_df['Size_Bucket'] = pd.cut(size_price_df['Size_in_SqFt'], bins=bins, labels=labels)

    fig = px.box(size_price_df, x='Size_Bucket', y='Price_in_Lakhs')
    st.plotly_chart(fig)
    