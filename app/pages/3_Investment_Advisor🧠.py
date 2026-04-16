import mlflow
import streamlit as st
import pandas as pd
import dagshub
import os
import json
import numpy as np
from dotenv import load_dotenv

#----------------------------------------------------------------------
# Load the dataset
#----------------------------------------------------------------------

dataframe = pd.read_csv("../Datasets/Property_Investment.csv")


# ----------------------------------------------------------------------
# Initialize DagsHub connection and MLflow tracking
# ----------------------------------------------------------------------
dagshub.init(
  repo_owner='JS-Tharun', 
  repo_name='Real-Estate-Investment-Advisor', 
  mlflow=True
)

load_dotenv()

os.environ['MLFLOW_TRACKING_USERNAME'] = f"{os.getenv('DAGSHUB_USERNAME')}"
os.environ['MLFLOW_TRACKING_PASSWORD'] = f"{os.getenv('DAGSHUB_PASSWORD')}"

mlflow.set_experiment(os.environ["MLFLOW_EXPERIMENT_NAME_ADV"])
mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])



# ----------------------------------------------------------------------
# Load the champion models from MLflow and cache it for Streamlit
# ----------------------------------------------------------------------

@st.cache_resource
def load_champion_model():
    prod_models = ["XGB_Inv_Advisor", "RF_Inv_Advisor", "DT_Inv_Advisor"]
    models = []

    for model in prod_models:
        model_uri = f"models:/{model}@champion"
        loaded_model = mlflow.pyfunc.load_model(model_uri)
        models.append(loaded_model)
    return models

with st.spinner("Loading Models...."):
    loaded_models = load_champion_model()


#----------------------------------------------------------------------
# Streamlit App Configuration
#----------------------------------------------------------------------

st.set_page_config(
    page_title="Investment Advisor",
    layout="wide"
)

with st.container():
    st.title("Property Investment Advisor")
    st.markdown("Enter the property details below to identify whether it is a good investment or not.")

# Form container with grid-based layout
with st.form("Investment Advisor Form"):
    # Location Section - Card-like container
    with st.container(border=True):
        st.subheader("📍 Location Details")
        col1, col2, col3 = st.columns(3)
        with col1:
            city_values = dataframe["City"].sort_values().unique()
            city_selection = st.selectbox(
                label="City",
                options=city_values
            )
        with col2:
            locality_values = dataframe["Locality"].unique()
            locality_selection = st.selectbox(
                label="Locality",
                options=locality_values
            )
        with col3:
            direction_values = dataframe["Direction_Facing"].unique()
            direction_selection = st.selectbox(
                label="Direction Facing",
                options=direction_values
            )

    st.markdown("")  # Spacer

    # Property Details Section - Card-like container
    with st.container(border=True):
        st.subheader("🏠 Property Details")
        col1, col2, col3 = st.columns(3)
        with col1:
            property_type_values = dataframe["Property_Type"].unique()
            property_type_selection = st.selectbox(
                label="Property Type",
                options=property_type_values
            )
        with col2:
            furnishing_status_values = dataframe["Furnished_Status"].unique()
            furnishing_status_selection = st.selectbox(
                label="Furnished Status",
                options=furnishing_status_values
            )

        with col3:
            price_selection = st.slider(
                "Price (₹ in lakhs)",
                min_value = dataframe['Price_in_Lakhs'].min(),
                max_value = dataframe['Price_in_Lakhs'].max(),
                value = 30.0,
                step = 0.1
            )
        

        col1, col2, col3 = st.columns(3)        
        with col1:
            size_selection = st.number_input(
                label="Size (in sqft)",
                min_value=500,
                max_value=5000,
                value=500,
                step=100
            )

        with col2:
            bhk_selection = st.number_input(
                label="BHK",
                min_value=1,
                max_value=5,
                step=1
            )
            
    
        with col3:
            age_selection = st.number_input(
                label="Age of Property (years)",
                min_value=0,
                max_value=50,
                step=1
            )
        

    st.markdown("")  # Spacer

    # Amenities Section - Card-like container
    with st.container(border=True):
        st.subheader("🏊 Amenities")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            parking_space = st.toggle(label="Parking Space")
            parking_space_selection = (1 if parking_space else 0)
        with col2:
            security = st.toggle(label="Security")
            security_selection = (1 if security else 0)
        with col3:
            clubhouse = st.toggle(label="Clubhouse")
            clubhouse_selection = (1 if clubhouse else 0)
        with col4:
            gardens = st.toggle(label="Gardens")
            gardens_selection = (1 if gardens else 0)

        col1, col2, col3 = st.columns(3)
        with col1:
            gym = st.toggle(label="Gym")
            gym_selection = (1 if gym else 0)
        with col2:
            play_area = st.toggle(label="Play Area")
            play_area_selection = (1 if play_area else 0)
        with col3:
            swimming_pool = st.toggle(label="Swimming Pool")
            swimming_pool_selection = (1 if swimming_pool else 0)

    st.markdown("")  # Spacer

    # Nearby Facilities Section - Card-like container
    with st.container(border=True):
        st.subheader("🏥 Nearby Facilities")
        col1, col2, col3 = st.columns(3)
        with col1:
            total_schools_selection = st.number_input(
                label="Total Schools Nearby",
                min_value=0,
                max_value=10,
                step=1
            )
        with col2:
            total_hospitals_selection = st.number_input(
                label="Total Hospitals Nearby",
                min_value=0,
                max_value=10,
                step=1
            )
        with col3:
            public_transport_score_selection = dataframe["Public_Transport_Accessibility"].unique()
            public_transport_score_selection = st.selectbox(
                label="Public Transport Accessibility",
                options=public_transport_score_selection
            )

    st.markdown("")  # Spacer

    # Submit Button - Centered in a row
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        submit_button = st.form_submit_button(label="💡 Invest?", use_container_width=True)


if submit_button:
    with st.container(border=True):
        st.subheader("🔮 Prediction Results")
        with st.spinner("Should You Investment..."):
            X = pd.DataFrame([{
                "City": city_selection,
                "Locality": locality_selection,
                "Property_Type": property_type_selection,
                "BHK": bhk_selection,
                "Size_in_SqFt": size_selection,
                "Price_in_Lakhs": price_selection,
                "Furnished_Status": furnishing_status_selection,
                "Direction_Facing": direction_selection,
                "Age_of_Property": age_selection,
                "Total_Nearby_Schools": total_schools_selection,
                "Total_Nearby_Hospitals": total_hospitals_selection,
                "Public_Transport_Accessibility": public_transport_score_selection,
                "Parking_Space": parking_space_selection,
                "Security": security_selection,
                "Clubhouse": clubhouse_selection,
                "Garden": gardens_selection,
                "Gym": gym_selection,
                "Playground": play_area_selection,
                "Pool": swimming_pool_selection
            }])

            #----------------------------------------------------------------------------------
            # Prediction using production models
            #----------------------------------------------------------------------------------

            predictions = []
            for model in loaded_models:
                y_pred = model.predict(X)
                predictions.append(y_pred)

            # Majority voting (mode across rows)
            final_prediction = np.round(np.mean(predictions, axis=0)).astype(int)
            if final_prediction[0] == 1:
                st.success("📈 Good Investment")
            else:
                st.warning("📉 Bad Investment")