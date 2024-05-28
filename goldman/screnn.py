import streamlit as st
import pandas as pd
import kaleido
import plotly.express as px
from datetime import datetime
from .goldie import update_chart

company_name = 'ACC'
specific_date = '' # "Airlines_01/02/2022"
company_df = pd.read_csv("D:\data\_COMPANY.CSV")
sector_df = pd.read_csv("D:\data\_SECTOR.CSV")

# Streamlit app
st.title('Interactive Chart with Streamlit and Plotly')

# Create company selector for streamlit
company_name = st.selectbox("Company",
                            company_df["Company Name"].unique(),
                            on_change=update_chart,
                            args=(company_df, sector_df))

# plot the df, index as x axis, columns as y axis
fig = px.line(df, x=df.index, y=column_names)

# update chart after company selector is updated
fig.update_layout(title_text=company_name)

st.plotly_chart(fig)
