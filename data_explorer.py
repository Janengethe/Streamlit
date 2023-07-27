import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns


st.set_option('deprecation.showPyplotGlobalUse', False)
# Display the raw data
# Question 1: Show the average sepal length for each species
# Question 2: Display a scatter plot comparing two features
# Question 3: Filter data based on species
# Question 4: Display a pairplot for the selected species
# Question 5: Show the distribution of a selected feature

st.subheader("Name: Jane Ng'ethe, Email: janengethew@gmail.com")

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
if st.checkbox("Show Average sepal Length"):
    st.subheader("Average sepal length for each species")
    average = data.groupby("species")["sepal_length"].mean()
    st.write(average)

# Question 2: Display a scatter plot comparing two features
st.subheader("Scatter Plot")
st.write("Sepal Length and Petal Length")
fig = px.scatter(data, x="sepal_length", y="petal_length", color="species")
st.plotly_chart(fig)

st.write("Sepal Length and Sepal Width")
fig = px.scatter(data, x="sepal_length", y="sepal_width", color="species")
st.plotly_chart(fig)

st.subheader("Compare two features using a scatter plot")
feature_1 = st.selectbox("Select the first feature:", data.columns[:-1])
feature_2 = st.selectbox("Select the second feature:", data.columns[:-1])

scatter_plot = px.scatter(data, x=feature_1, y=feature_2, color="species", hover_name="species")
st.plotly_chart(scatter_plot)

# Question 3: Filter data based on species
st.subheader("Filter data based on species")
selected_species = st.multiselect("Select species to display:", data["species"].unique())

if selected_species:
    filtered_data = data[data["species"].isin(selected_species)]
    st.dataframe(filtered_data)
else:
    st.write("No species selected.")


# Question 4: Display a pairplot for the selected species
if st.checkbox("Display a pairplot for the selected species"):
    st.subheader("Pairplot for selected species")

    if selected_species:
        sns.pairplot(filtered_data, hue="species")
    else:
        sns.pairplot(data, hue="species")
    st.pyplot()

# Question 5: Show the distribution of a selected feature
st.subheader("Distribution of a Selected Feature")
selected_feature = st.selectbox("Select a feature to display its distribution:", data.columns[:-1])

hist_plot = px.histogram(data, x=selected_feature, color="species", nbins=30, marginal="box", hover_data=data.columns)
st.plotly_chart(hist_plot)