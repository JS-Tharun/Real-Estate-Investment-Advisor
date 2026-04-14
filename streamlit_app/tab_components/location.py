import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def price_per_sqft_state_chart(df):
    st.write("### Price per Sqft by State")
    st.caption("Average price per square foot for each state")
    price_per_sqft_state_df = (df.groupby('State')['Price_per_SqFt_in_Lakhs']
        .agg(['mean'])
        .rename(columns={'mean':'avg_price_per_sqft'})  
        .reset_index()      
    )
    price_per_sqft_state_df['avg_price_per_sqft'] = price_per_sqft_state_df['avg_price_per_sqft'] * 100000
    price_per_sqft_state_df = price_per_sqft_state_df.sort_values(by='avg_price_per_sqft', ascending=False)
    st.bar_chart(
        price_per_sqft_state_df.set_index('State')['avg_price_per_sqft'],
        x_label="State",
        y_label="Average Price per Sqft (₹)"
    )

def price_city(df):
    st.write("### Average Price by City")
    st.caption("Average price for each city")
    price_city_df = (df.groupby('City')['Price_in_Lakhs']
        .agg(['mean'])
        .rename(columns={'mean':'avg_price'})  
        .reset_index()      
    )
    price_city_df['avg_price'] = price_city_df['avg_price'] * 100000
    price_city_df = price_city_df.sort_values(by='avg_price', ascending=False)
    st.bar_chart(
        price_city_df.set_index('City')['avg_price'],
        x_label="City",
        y_label="Price (₹)"
    )

def median_age_locality_chart(df):
    st.write("### Median Age of Properties by Locality")
    st.caption("Median age of properties for each locality")
    age_by_locality_df = (df.groupby('Locality')['Age_of_Property']
        .agg(['median'])
        .reset_index()
        .rename(columns={'median': 'median_property_age'})
    )
    fig = px.box(
        age_by_locality_df['median_property_age']
    )
    st.plotly_chart(fig)

def bhk_dis_city(df):
    st.write("### Average BHK Count by City")
    st.caption("Average number of bedrooms (BHK) for each city")
    BHK_City_dist = df.groupby(['City', 'BHK']).size().unstack()
    fig = px.imshow(BHK_City_dist, text_auto=".2f", width=1000, height=800)
    st.plotly_chart(fig, config={"responsive": True})

def top_localities_chart(df):
    st.write("### Top Localities by Average Price")
    st.caption("Top localities based on average price")
    avg_price = (
        df.groupby(['City', 'Locality'])['Price_in_Lakhs']
        .agg(['mean', 'median', 'count', 'min', 'max'])
        .rename(columns={'mean': 'avg_price', 'median': 'median_price', 'count':'property_count', 'min': 'min_price', 'max':'max_price'})
        .reset_index()
    )
    top_5_localities = avg_price.sort_values(by='avg_price', ascending=False).head(5)
    # Weighted (Bayesian) average to tackle low property count for each locality
    C = df['Price_in_Lakhs'].mean()  # global mean
    m = 10 #avg_price['property_count'].median()  # Setting the global median count as constant to better reflect "typical" locality

    avg_price['weighted_score'] = (
        (avg_price['property_count'] * avg_price['avg_price'] + m * C) /
        (avg_price['property_count'] + m)
    )

    weighted_top_5_localities = avg_price.sort_values(by='weighted_score', ascending=False).head(5)
    weighted_top_5_localities['Rank'] = weighted_top_5_localities['weighted_score'].rank(ascending=False)
    fig = px.bar(
        weighted_top_5_localities,
        x='City',
        y='avg_price',
        text='Locality',
        labels={
            'City': 'City',
            'avg_price': 'Average Price (₹)'
        }
    )
    fig.update_traces(textposition='inside')
    fig.update_layout(
        xaxis_title="City",
        yaxis_title="Average Price (₹)",
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)

def prop_availability_city(df):
    st.write("### Property Availability by City")
    st.caption("Distribution of property availability status across different cities")
    availability_city_df = df.groupby(['City', 'Availability_Status']).size().reset_index(name='Property_Count')
    fig = px.bar(
        availability_city_df,
        x='City',
        y='Property_Count',
        color='Availability_Status',
        labels={
            'City': 'City',
            'Property_Count': 'Number of Properties',
            'Availability_Status': 'Availability Status'
        }
    )
    st.plotly_chart(fig, use_container_width=True)