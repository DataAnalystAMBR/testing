import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Set page config to minimal
st.set_page_config(layout="centered", page_title="Notion Chart")

# Hides streamlit menu and footer for cleaner embed
# CSS to hide the footer and fullscreen button
hide_style = """
    <style>
    /* Hides the "Made with Streamlit" footer */
    footer {visibility: hidden;}
    
    /* Hides the top header bar */
    header {visibility: hidden;}

    /* Hides the Fullscreen button in the bottom right */
    button[title="View fullscreen"] {
        visibility: hidden;
    }
    
    /* Hides the 'Manage App' and other community cloud branding */
    .embeddedAppMetaInfoBar_container__DxxL1 {
        display: none !important;
    }
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

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
