import streamlit as st

st.set_page_config(
    page_title="Real Estate Property Investment Analysis",
    layout="wide"
)

def main():

    with st.container():
        st.write("# Real Estate Investment Advisor🏠📈")
        st.write("# Predicting Property Profitability & Future Value💸")
        st.markdown("""
            ### 📊 Analysis Dashboard  
            Gain actionable insights through interactive visual charts for smarter real estate decisions.

            ### 📈 Future Price Prediction  
            Forecast property prices over the next 5 years using data-driven predictive models.

            ### 🧠 Investment Advisor  
            Evaluate whether a property is a good investment based on expected returns and key indicators.
        """)

        st.divider()

        st.markdown(
            """
            ## 📄 Pages Overview

            | Pages | Description |
            |-------|-------------|
            | 📊 Analysis Dashboard | Visualize real estate trends and insights through interactive charts |
            | 📈 Future Price Prediction | Predict property prices over the next 5 years using advanced models |
            | 🧠 Investment Advisor | Identify whether a property is a good investment based on expected returns |

            """
        )
        

if __name__ == "__main__":
    main()