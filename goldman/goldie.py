import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime

def update_chart(company_df, sector_df):
    # company_name = 'ACC'
    company_name = st.session_state.company_name

    specific_date = '' # "Airlines_01/02/2022"
    
    # Filter specific company
    company_data = company_df[company_df["Company Name"] == company_name]
    print(company_data)

    # check if empty company_data
    if company_data.empty:
        st.write("No data for this company")
        return

    sector = company_data.iloc[0]["Sector"]
    company = company_data.iloc[0]["Company Name"]

    # Select Company name, Sector and 2013 to 2050 columns
    years = [str(x) for x in range(2013, 2051)]

    company_data = company_data[years]
    company_data["Scenario name"] = company
    company_data["Date"] = ''
    company_data = company_data.reindex(columns=["Date", "Scenario name"] + years)

    company_data['Scenario name'] = company_data['Scenario name'].astype("string")

    # replace string sector in column of sector_df
    sector_df = sector_df[(sector_df["Sector name"] == sector)]
    sector_df = sector_df[(sector_df["Region"] == 'Global')]
    print(sector_df)

    if not sector_df.empty:
        sector_df['Date'] = sector_df['Benchmark ID'].replace(sector+'_', '')
        if not specific_date:
            specific_date = sector_df.iloc[0]["Date"]

        sector_df = sector_df[(sector_df["Date"] == specific_date)]
    else:
        sector_df['Date'] = ''

    sector_columns = ['Date', 'Scenario name'] + years
    sector_data = sector_df[sector_columns]

    print(company_data)
    print(sector_data)
    merged_df = pd.concat([company_data, sector_data], axis=0, ignore_index=True)

    merged_df = merged_df.drop(columns=['Date'])
    merged_df = merged_df.set_index('Scenario name').unstack().unstack().reset_index(names='year').rename_axis(columns=None)

    # set year column as index
    df = merged_df.set_index('year')
    column_names = df.columns.tolist()

    print(df)

    # remove company from column names
    column_names.remove(company)

    # plot the df, index as x axis, columns as y axis
    fig = px.area(df, x=df.index, y=column_names, 
                  color_discrete_sequence=["#FDB714", "#009CA7", "#F05023"])
    fig2 = px.line(df, x=df.index, y=company_name)

    subfig = make_subplots(specs=[[{"secondary_y": True}]])
    subfig.add_traces(fig.data + fig2.data)

    # update chart after company selector is updated
    subfig.update_layout(title_text=company_name)

    print('updating chart')
    chart_slot.plotly_chart(subfig)

company_name = 'ACC'
specific_date = '' # "Airlines_01/02/2022"
company_df = pd.read_csv("D:\data\_COMPANY.CSV")
sector_df = pd.read_csv("D:\data\_SECTOR.CSV")

# Streamlit app
st.title('Company Climate Transition Pathway')

# Create company selector for streamlit
company_name = st.selectbox("Company",
                            company_df["Company Name"].unique(),
                            on_change=update_chart,
                            args=(company_df, sector_df),
                            key='company_name')

print('first print chart')
st.session_state.first_time = True
if chart_slot.empty:
    chart_slot = st.empty()
