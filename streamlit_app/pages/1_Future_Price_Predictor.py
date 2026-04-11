import mlflow
import streamlit as st
import pandas as pd
import dagshub
import os
from dotenv import load_dotenv


dagshub.init(
  repo_owner='JS-Tharun', 
  repo_name='Real-Estate-Investment-Advisor', 
  mlflow=True
)

load_dotenv()

os.environ['MLFLOW_TRACKING_USERNAME'] = f"{os.getenv('DAGSHUB_USERNAME')}"
os.environ['MLFLOW_TRACKING_PASSWORD'] = f"{os.getenv('DAGSHUB_PASSWORD')}"

dataframe = pd.read_csv("data/Future_Price.csv")

st.set_page_config(
    page_title="Future Property Price Prediction",
    layout="wide"
)

with st.container(border=True):
    st.title("This is the Price Predictor page")

with st.form("Price Prediction Form"):


    with st.container():

        city_values = dataframe["City"].sort_values().unique()
        city_selection = st.selectbox(
            label="City",
            options=city_values
        )

        locality_values = dataframe["Locality"].unique()
        locality_selection = st.selectbox(
            label="Locality",
            options=locality_values
        )

        property_type_values = dataframe["Property_Type"].unique()
        property_type_selection = st.selectbox(
            label="Property Type",
            options=property_type_values
        )

        
        bhk_selection = st.number_input(
            label="BHK",
            min_value=1,
            max_value=5,
            step=1
        )

        size_selection = st.number_input(
            label="Size (in sqft)",
            min_value=500,
            max_value=5000,
            value=500,
            step=100
        )

        price_per_sqft_selection = st.number_input(
            label="Price per sqft (in Lakhs)",
            min_value=0.001,
            max_value=1.0,
            value=1.0,
            step=0.1
        )

        furnishing_status_values = dataframe["Furnished_Status"].unique()
        furnishing_status_selection = st.selectbox(
            label="Furnished Status",
            options=furnishing_status_values
        )

        direction_values = dataframe["Direction_Facing"].unique()
        direction_selection = st.selectbox(
            label="Direction Facing",
            options=direction_values
        )

        floor_selection = st.number_input(
            label="Floor Number",
            min_value=0,
            max_value=30,
            step=1
        )

        total_floors_selection = st.number_input(
            label="Total Floors",
            min_value=1,
            max_value=30,
            step=1
        )

        age_selection = st.number_input(
            label="Age of the Property (in years)",
            min_value=0,
            max_value=50,
            step=1
        )

        owner_type_values = dataframe["Owner_Type"].unique()
        owner_type_selection = st.selectbox(
            label="Owner Type",
            options=owner_type_values
        )

        availability_values = dataframe["Availability_Status"].unique()
        availability_selection = st.selectbox(
            label="Availability Status",
            options=availability_values
        )

        total_schools_selection = st.number_input(
            label="Total Schools Nearby",
            min_value=0,
            max_value=10,
            step=1
        )

        total_hospitals_selection = st.number_input(
            label="Total Hospitals Nearby",
            min_value=0,
            max_value=10,
            step=1
        )

        public_transport_score_selection = dataframe["Public_Transport_Accessibility"].unique()
        public_transport_score_selection = st.selectbox(
            label="Public Transport Accessibility",
            options=public_transport_score_selection
        )

        parking_space = st.toggle(label="Parking Space Available")
        parking_space_selection = (1 if parking_space else 0)

        security = st.toggle(label="Security Available")
        security_selection = (1 if security else 0)

        clubhouse = st.toggle(label="Clubhouse Available")
        clubhouse_selection = (1 if clubhouse else 0)

        gardens = st.toggle(label="Gardens Available")
        gardens_selection = (1 if gardens else 0)

        gym = st.toggle(label="Gym Available")
        gym_selection = (1 if gym else 0)

        play_area = st.toggle(label="Play Area Available")
        play_area_selection = (1 if play_area else 0)

        swimming_pool = st.toggle(label="Swimming Pool Available")
        swimming_pool_selection = (1 if swimming_pool else 0)

        submit_button = st.form_submit_button(label="Predict Future Price")

        if submit_button:
            st.write("Predicting future price based on the selected features...")
            X = pd.DataFrame([{
                "City": city_selection,
                "Locality": locality_selection,
                "Property_Type": property_type_selection,
                "BHK": bhk_selection,
                "Size_in_SqFt": size_selection,
                "Price_per_SqFt_in_Lakhs": price_per_sqft_selection,
                "Furnished_Status": furnishing_status_selection,
                "Direction_Facing": direction_selection,
                "Floor_No": floor_selection,
                "Total_Floors": total_floors_selection,
                "Age_of_Property": age_selection,
                "Owner_Type": owner_type_selection,
                "Availability_Status": availability_selection,
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

            st.write(f"Input features: {X}")
            st.write("Future price prediction will be displayed here after implementing the model.")

            st.write(X)

            mlflow.set_experiment(os.environ["MLFLOW_EXPERIMENT_NAME_REG"])
            mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])

            prod_model = "Future_Price_Predictor-Prod"

            model_uri=f"models:/{prod_model}@champion"

            loaded_model = mlflow.pyfunc.load_model(model_uri)
            y_pred = loaded_model.predict(X)
            st.write(f"Predicted Future Price: {y_pred[0]} Lakhs")



