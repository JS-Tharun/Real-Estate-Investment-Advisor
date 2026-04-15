import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def feature_relationship_plots(df):
    st.write("### Feature Relationships")
    st.caption("Scatter plots showing relationships between features")
    df_numeric = df.select_dtypes(include='number')
    df_numeric.drop(columns=['ID', 'Future_Price_5Y'], axis=1, inplace=True)
    fig = px.imshow(df_numeric.corr(), text_auto=".2f", width=1000, height=800)
    st.plotly_chart(fig, config={"responsive": True})

