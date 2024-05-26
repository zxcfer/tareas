import pandas as pd
import kaleido
import plotly.express as px

company_name = 'ACC'
specific_date = '' # "Airlines_01/02/2022"
company_df = pd.read_csv("D:\data\_COMPANY.CSV")
sector_df = pd.read_csv("D:\data\_SECTOR.CSV")

# Filter specific company
company_data = company_df[company_df["Company Name"] == company_name]
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
sector_df['Date'] = sector_df['Benchmark ID'].replace(sector+'_', '')
if not specific_date:
    specific_date = sector_df.iloc[0]["Date"]

# filter sector_df by 'Sector name' and 'Specific date'
sector_data = sector_df[(sector_df["Sector name"] == sector) & (sector_df["Date"] == specific_date)]

sector_columns = ['Date', 'Scenario name'] + years
sector_data = sector_df[sector_columns]
sector_data['Scenario name'] = sector_data['Scenario name'].astype("string")

print(company_data)
print(sector_data)
merged_df = pd.concat([company_data, sector_data], axis=0, ignore_index=True)
print(merged_df)

df = merged_df.set_index('Scenario name').unstack().unstack().reset_index(names='year').rename_axis(columns=None)
print(df)

# plot the data
fig = px.line(company_data, y="Company Name", x=years)

print("fer")
# # Save the plot as an image
fig.write_image("D:/tmp/out_1.png", engine="kaleido")
print("fin")
