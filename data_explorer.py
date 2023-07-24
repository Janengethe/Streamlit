import streamlit as st
import pandas as pd
import plotly.express as px


# Display the raw data
# Question 1: Show the average sepal length for each species
# Question 2: Display a scatter plot comparing two features
# Question 3: Filter data based on species
# Question 4: Display a pairplot for the selected species
# Question 5: Show the distribution of a selected feature


def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    data = pd.read_csv(url, header=None, names=column_names)
    return data

data = load_data()


st.title("Iris Dataset")
st.write("creating an Interactive Data Explorer using VSCode and Deploying to Streamlit Share")


# Display the raw data
if st.checkbox("Show Data"):
    st.subheader("Raw Data")
    st.dataframe(data)


# The average sepal length for each species
