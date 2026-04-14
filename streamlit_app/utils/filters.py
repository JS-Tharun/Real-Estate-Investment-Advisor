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
    price_filter()
    size_filter()
    bhk_filter(df)
    property_type_filter(df)
    year_built_filter(df)
    total_floors_filter(df)

    st.divider()
    st.write("## Nearby Facilities")
    school_filter(df)
    hospital_filter(df)
    public_transport_filter(df)

    st.divider()
    st.write("## Amenities")
    parking_filter(df)
    secutity_filter(df)
    clubhouse_filter(df)
    garden_filter(df)
    gym_filter(df)
    playground_filter(df)
    pool_filter(df)
    

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
    selected_property_type = st.multiselect(
        "Property Type", 
        property_type_options,
        default=[]
    )
    filter['Property_Type'] = selected_property_type if selected_property_type else None

def bhk_filter(df):
    bhk_options = sorted(df['BHK'].unique())
    selected_bhk = st.slider(
        "BHK", 
        min_value=int(min(bhk_options)),
        max_value=int(max(bhk_options)),
        value=(int(min(bhk_options)), int(max(bhk_options)))
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

def price_filter():
    selected_price = st.slider(
        "Price (in Lakhs)", 
        min_value=10,
        max_value=500,
        value=(10, 500),
        step=10
    )
    filter['Price_in_Lakhs'] = selected_price

def year_built_filter(df):
    year_built_options = sorted(df['Year_Built'].unique())
    selected_year_built = st.slider(
        "Year Built", 
        min_value=int(min(year_built_options)),
        max_value=int(max(year_built_options)),
        value=(int(min(year_built_options)), int(max(year_built_options)))
    )
    filter['Year_Built'] = selected_year_built

def total_floors_filter(df):
    total_floors_options = sorted(df['Total_Floors'].unique())
    selected_total_floors = st.slider(
        "Total Floors", 
        min_value=int(min(total_floors_options)),
        max_value=int(max(total_floors_options)),
        value=(int(min(total_floors_options)), int(max(total_floors_options)))
    )
    filter['Total_Floors'] = selected_total_floors

def school_filter(df):
    school_options = sorted(df['Total_Nearby_Schools'].unique())
    selected_total_nearby_schools = st.slider(
        "Total Nearby Schools", 
        min_value=int(min(school_options)),
        max_value=int(max(school_options)),
        value=(int(min(school_options)), int(max(school_options)))
    )
    filter['Total_Nearby_Schools'] = selected_total_nearby_schools

def hospital_filter(df):
    hospital_options = sorted(df['Total_Nearby_Hospitals'].unique())
    selected_total_nearby_hospitals = st.slider(
        "Total Nearby Hospitals", 
        min_value=int(min(hospital_options)),
        max_value=int(max(hospital_options)),
        value=(int(min(hospital_options)), int(max(hospital_options)))
    )
    filter['Total_Nearby_Hospitals'] = selected_total_nearby_hospitals

def public_transport_filter(df):
    public_transport_options = sorted(df['Public_Transport_Accessibility'].unique())
    selected_distance_to_public_transport = st.multiselect(
        "Distance to Public Transport (in meters)", 
        public_transport_options,
        default=[]
    )
    filter['Public_Transport_Accessibility'] = selected_distance_to_public_transport if selected_distance_to_public_transport else None


def parking_filter(df):
    selected_parking = st.selectbox(
        "Parking Availability",
        options=['Yes', 'No'],
        index=None,
        placeholder='All'
    )
    filter['Parking_Space'] = selected_parking

def secutity_filter(df):
    selected_security = st.selectbox(
        "Security Features",
        options=['Yes', 'No'],
        index=None,
        placeholder='All'
    )
    filter['Security'] = selected_security

def clubhouse_filter(df):
    selected_clubhouse = st.selectbox(
        "Clubhouse Availability",
        options=['Yes', 'No'],
        index=None,
        placeholder='All'
    )
    filter['Clubhouse'] = selected_clubhouse

def garden_filter(df):
    selected_garden = st.selectbox(
        "Garden Availability",
        options=['Yes', 'No'],
        index=None,
        placeholder='All'
    )
    filter['Garden'] = selected_garden

def gym_filter(df):
    selected_gym = st.selectbox(
        "Gym Availability",
        options=['Yes', 'No'],
        index=None,
        placeholder='All'
    )
    filter['Gym'] = selected_gym

def playground_filter(df):
    selected_playground = st.selectbox(
        "Playground Availability",
        options=['Yes', 'No'],
        index=None,
        placeholder='All'
    )
    filter['Playground'] = selected_playground

def pool_filter(df):
    selected_pool = st.selectbox(
        "Pool Availability",
        options=['Yes', 'No'],
        index=None,
        placeholder='All'
    )
    filter['Pool'] = selected_pool