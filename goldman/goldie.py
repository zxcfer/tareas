import pandas as pd
import plotly.express as px

company_name = "CompanyABC"
company_df = pd.read_csv("COMPANY.CSV")
sector_df = pd.read_csv("SECTOR.CSV")

# Filter specific company
company_data = company_df[company_df["Company Name"] == company_name]

# Select Company name, Sector and years columns
company_data = company_df

merged_df = pd.merge(company_data, sector_df, on="Company Name")


# Plot the performance index per year for the company and the sector
fig = px.line(merged_df, x="year", y=["Scenario name", "Sector"],
              title=f"Performance Index Comparison for {company_name} and Sector per Year")

# 

# Save the plot as an image
fig.write_image("D:/tmp/out.png")
