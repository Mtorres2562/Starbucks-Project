import streamlit as st
import pandas as pd
import plotly.express as px

star = pd.read_csv('C:/Users/mtorr/Documents/Coding-Temple/8-Module/Assignments/M8-Mini-Project-Starbucks-EDA/data/new_cleaned_dataset.csv')
star = star.drop(columns=["Unnamed: 0"], errors="ignore")


# set page title and icon
st.set_page_config(page_title = "Starbucks Dataset Explorer", page_icon="☕")

# sidebar navigation
page = st.sidebar.selectbox("Select a page",["Home", "Data Overview", "Exploratory Data Analysis (EDA)"])

# first page
if page == "Home":
    st.title("☕️ Starbucks Dataset Explorer")
    st.subheader("Welcome to our Starbucks Dataset Explorer App!")
    st.write("""
             This app is meant to give more insight to the Starbucks Dataset.
             We will dive into the various drinks and beverages starbucks makes.
             Exploring the features that makes a drink and the realtionship of those features, 
             visualizing them all through various graphs.
             """)    
    st.image('https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-1610545851.jpg?c=16x9&q=h_653,w_1160,c_fill/f_webp', caption = 'Starbucks Coffee mugs')


# Data Overview
elif page == "Data Overview":
    st.title ("📋 Data Overview")
    st.subheader("About the Data")
    st.write("""Starbucks is a well know coffee shop around the world, with over 87000 possible drink combinations.
             With this Dataset we will be looking at 240 of those drinks, the type of Beverages, and the Preperations of them.
             Including the nutrition facts of each drink from number of calries to miligrams of caffeine. 
             """)
    st.image('https://www.usatoday.com/gcdn/authoring/authoring-images/2023/08/23/USAT/70655313007-starbucks-fall-beverages.png?crop=1275,719,x82,y0&width=660&height=371&format=pjpg&auto=webp', caption= "Starbucks drinks")

    # Display data
    st.subheader("Quick glance at the Data")
    if st.checkbox("Show Dataframe"):
        st.dataframe(star)

    # Shape of Dataset
    if st.checkbox("Show shape of Data"):
        st.write(f"The dataset contains {star.shape[0]} rows and {star.shape[1]} columns")

# Exploratory Data Analysis (EDA)
elif page == "Exploratory Data Analysis (EDA)":
    st.title("📊 Exploratory Data Analysis (EDA)")

    st.subheader("Select the type of visualtization You'd like to expore.")
    eda_type = st.multiselect("Visualization Options", ['Histograms', 'Scatterplots', 'Box Plots', 'Bar Charts'])

    obj_cols = star.select_dtypes(include = 'object').columns.tolist()
    num_cols  = star.select_dtypes(include ='number').columns.tolist() 

    # Histogram plot
    if 'Histograms' in eda_type:
        st.subheader("Histograms-Visualizing Numerical Distribution")
        h_selected_col = st.selectbox("Select a numerical column for the histogram:", num_cols)
        if h_selected_col:
            chart_title = f"Distribution of {h_selected_col.title().replace('_',' ')}"
            if st.checkbox("Show by Drink's"):
                st.plotly_chart(px.histogram(star, x = h_selected_col, color = 'Drink', title = chart_title, barmode= 'overlay'))
            elif st.checkbox("Show by Beverage"):
                st.plotly_chart(px.histogram(star, x = h_selected_col, color = 'Beverage', title = chart_title, barmode= 'overlay'))
            elif st.checkbox("Show by Preperation"):
                st.plotly_chart(px.histogram(star, x = h_selected_col, color = 'Preperation', title = chart_title, barmode= 'overlay'))
            else:
                st.plotly_chart(px.histogram(star, x = h_selected_col, title = chart_title))

    # Scatter Plot
    if 'Scatterplots' in eda_type:
        st.subheader("Scatterplots - Visualizing Relationships")
        selected_col_x = st.selectbox("Select x-axis variable:", num_cols)
        selected_col_y = st.selectbox("Select y-axis variable:", num_cols)
        if selected_col_x and selected_col_y:
            chart_title = f"{selected_col_x.title().replace('_', ' ')} vs. {selected_col_y.title().replace('_', ' ')}"
            st.plotly_chart(px.scatter(star, x=selected_col_x, y=selected_col_y, color='Drink', title=chart_title))
    
    # Box plot
    if 'Box Plots' in eda_type:
        st.subheader("Box Plots - Visualizing Numerical Distributions")
        b_selected_col = st.selectbox("Select a numerical column for the box plot:", num_cols)
        if b_selected_col:
            chart_title = f"Distribution of {b_selected_col.title().replace('_', ' ')}"
            st.plotly_chart(px.box(star, x=b_selected_col, y='Drink', title=chart_title, color='Drink'))

    # Bar Chart
    if 'Bar Charts' in eda_type:
        st.subheader("Bar Chart - Visualizing Categorical Distribution")
        selected_col = st.selectbox("Select a categorical variable:", obj_cols)
        if selected_col:
            chart_title = f'Distribution of {selected_col.title()}'
            st.plotly_chart(px.bar(star, y=selected_col, color=selected_col, title=chart_title))