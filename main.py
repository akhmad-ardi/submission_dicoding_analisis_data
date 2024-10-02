import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set_theme(style='dark')

# Load dataset
df_day = pd.read_csv('data_dashboard/cleaned_day_data.csv')

# Set up Streamlit app title
st.title("Bike Rentals")

st.sidebar.header("Filter Options")
selected_season = st.sidebar.selectbox('Select Season', options=[1, 2, 3, 4], index=0, format_func=lambda x: {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}[x])
filtered_data = df_day[df_day['season'] == selected_season]

# Sidebar for selecting analysis
st.sidebar.header("Select Analysis")
analysis_type = st.sidebar.selectbox("Choose Analysis", 
                                     options=["Weather Impact on Bike Rentals", 
                                              "Seasonal and Daily Trends"])

season = ""
if selected_season == 1:
   season = "Spring"
elif selected_season == 2:
   season = "Summer"
elif selected_season == 3:
   season = "Fall"
elif selected_season == 4:
   season = "Winter"

st.subheader("Data for Season: {}".format(season))
st.write(filtered_data.head())

# Analysis 1: How Weather Affects Bike Rentals
if analysis_type == "Weather Impact on Bike Rentals":
    st.subheader("How Weather Affects Bike Rentals")

    # Filter options for user to choose weather factor
    weather_factor = st.selectbox("Select Weather Factor", 
                                  options=["Temperature", "Humidity", "Windspeed", "Weather Situation"])
    
    if weather_factor == "Temperature":
        # Scatter plot: Temperature vs Total Bike Rentals
        st.subheader("Scatter Plot: Temperature vs Total Bike Rentals")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='temp', y='cnt', data=df_day)
        plt.title('Temperature vs Total Bike Rentals')
        plt.xlabel('Temperature')
        plt.ylabel('Total Rentals')
        st.pyplot(plt)
        
    elif weather_factor == "Humidity":
        # Scatter plot: Humidity vs Total Bike Rentals
        st.subheader("Scatter Plot: Humidity vs Total Bike Rentals")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='hum', y='cnt', data=df_day)
        plt.title('Humidity vs Total Bike Rentals')
        plt.xlabel('Humidity')
        plt.ylabel('Total Rentals')
        st.pyplot(plt)
        
    elif weather_factor == "Windspeed":
        # Scatter plot: Windspeed vs Total Bike Rentals
        st.subheader("Scatter Plot: Windspeed vs Total Bike Rentals")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='windspeed', y='cnt', data=df_day)
        plt.title('Windspeed vs Total Bike Rentals')
        plt.xlabel('Windspeed')
        plt.ylabel('Total Rentals')
        st.pyplot(plt)
        
    elif weather_factor == "Weather Situation":
        # Box plot: Weather Situation vs Total Bike Rentals
        st.subheader("Box Plot: Weather Situation vs Total Bike Rentals")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='weathersit', y='cnt', data=df_day)
        plt.title('Weather Situation vs Total Bike Rentals')
        plt.xlabel('Weather Situation (1 = Clear, 2 = Mist, 3 = Light Snow/Rain)')
        plt.ylabel('Total Rentals')
        st.pyplot(plt)

# Analysis 2: Seasonal and Daily Trends in Bike Rentals
elif analysis_type == "Seasonal and Daily Trends":
    st.subheader("Seasonal and Daily Trends in Bike Rentals")

    # Line plot: Month vs Total Bike Rentals
    st.subheader("Line Plot: Month vs Total Bike Rentals")
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='mnth', y='cnt', data=df_day, marker='o')
    plt.title('Month vs Total Bike Rentals')
    plt.xlabel('Month')
    plt.ylabel('Total Rentals')
    st.pyplot(plt)
    
    # Bar plot: Weekday vs Total Bike Rentals
    st.subheader("Bar Plot: Weekday vs Total Bike Rentals")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weekday', y='cnt', data=df_day)
    plt.title('Weekday vs Total Bike Rentals')
    plt.xlabel('Weekday (0 = Sunday, 6 = Saturday)')
    plt.ylabel('Total Rentals')
    st.pyplot(plt)