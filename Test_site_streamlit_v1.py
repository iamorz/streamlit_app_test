# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:33:20 2024

@author: swzen
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the Streamlit app
st.title("Simple Streamlit Test App")

# Introduction text
st.write("""
This is a simple Streamlit app to test deployment.
You can use interactive components like sliders, dropdowns, and plots.
""")

# Add a slider to select a number of random points
n_points = st.slider("Select number of random points to plot", 10, 100, 50)

# Generate random data
x = np.random.randn(n_points)
y = np.random.randn(n_points)

# Create a dropdown for selecting the plot color
selected_color = st.selectbox("Select plot color", ['blue', 'green', 'red'])

# Create the plot
fig, ax = plt.subplots()
ax.scatter(x, y, color=selected_color)
ax.set_title(f"Scatter plot of {n_points} random points")

# Display the plot in Streamlit
st.pyplot(fig)

# A simple table
st.write("Here is a sample table:")
data = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.randn(10)
})
st.dataframe(data)

# Display a success message to indicate completion
st.success("The app is ready for deployment!")
