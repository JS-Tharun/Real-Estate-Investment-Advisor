import streamlit as st

st.set_page_config(
    page_title="Real Estate Property Investment Analysis",
    layout="wide"
)

def main():

    with st.container():
        st.write("# Real Estate Property Future Price Prediction 🏠📈")
        st.write(
            """
            This page provides insights into the future price prediction of real estate properties using machine learning models. 
            The predictions are based on various features such as location, property type, size, and historical price trends.
            
            ### Key Features:
            - **Model Performance**: Evaluate the performance of different regression models used for price prediction.
            - **Feature Importance**: Understand which features have the most significant impact on property prices.
            - **Interactive Visualizations**: Explore interactive charts and graphs to visualize the predicted prices and their distribution.
            
            ### How to Use:
            1. Select a property from the dropdown menu to view its predicted future price.
            2. Use the filters to adjust the input features and see how they affect the predicted price.
            3. Analyze the model's performance metrics to understand the accuracy of the predictions.
            
            This tool is designed to assist buyers, investors, and real estate professionals in making informed decisions based on data-driven insights.
            """
        )

if __name__ == "__main__":
    main()