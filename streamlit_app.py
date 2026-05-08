import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Set page config to minimal
st.set_page_config(layout="centered", page_title="Notion Chart")

# Hides streamlit menu and footer for cleaner embed
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 1. Create sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# 2. Create interactive chart
c = alt.Chart(chart_data).mark_line().encode(
     x=alt.X('a', title='X Axis'),
     y=alt.Y('b', title='Y Axis'),
     tooltip=['a', 'b', 'c']
).interactive()

# 3. Display in Streamlit
st.title("My Data Chart")
st.altair_chart(c, use_container_width=True)
