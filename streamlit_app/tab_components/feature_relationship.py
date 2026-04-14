import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def feature_correlation_heatmap(df):
    st.write("### Feature Correlation Heatmap")
    st.caption("Correlation between different features in the dataset")
    df_numeric = df.select_dtypes(include='number')
    df_numeric.drop('ID', axis=1, inplace=True)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df_numeric.corr(numeric_only=True), annot=True, fmt='.2f', cmap='YlGnBu')
    st.pyplot(fig)