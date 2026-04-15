import mlflow
import streamlit as st
import pandas as pd
import dagshub
import os
import json
import numpy as np
from dotenv import load_dotenv

st.write("Hello")

#----------------------------------------------------------------------
# Load the dataset
#----------------------------------------------------------------------

dataframe = pd.read_csv("../Datasets/Property_Investment.csv")