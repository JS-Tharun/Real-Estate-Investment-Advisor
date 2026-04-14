import streamlit as st
import plotly.express as px

def owner_type_count(df):
    st.write("### Owner Type Distribution")
    st.caption("Number of properties owned by different owner types")
    owner_counts = df['Owner_Type'].value_counts()
    st.bar_chart(
        owner_counts,
        x_label="Owner Type",
        y_label="Number of Properties"
    )

def prop_availability(df):
    st.write("### Property Availability")
    st.caption("Distribution of properties based on their availability status")
    
    availability_counts = df['Availability_Status'].value_counts().reset_index()
    availability_counts.columns = ['Availability_Status', 'Property_Count']
    availability_counts['Percentage'] = (availability_counts['Property_Count'] / availability_counts['Property_Count'].sum()) * 100

    fig = px.pie(
        availability_counts,
        names='Availability_Status',
        values='Property_Count'
    )
    st.plotly_chart(fig)

def price_public_transport(df):
    st.write("### Price by Proximity to Public Transport")
    st.caption("Average price difference based on proximity to public transport")
    df_transport = (
        df.groupby('Public_Transport_Accessibility')['Price_per_SqFt_in_Lakhs']
        .agg(['mean','count'])
        .reset_index()
    )
    df_transport['mean'] = df_transport['mean'] * 100000
    df_transport.rename(columns={'mean':'avg_price_per_sqft'}, inplace=True)
    df_transport.sort_values('avg_price_per_sqft', ascending=False, inplace=True)
    st.bar_chart(
        df_transport.set_index('Public_Transport_Accessibility')['avg_price_per_sqft'],
        x_label="Public Transport Accessibility",
        y_label="Average Price per Sqft (₹)"
    )