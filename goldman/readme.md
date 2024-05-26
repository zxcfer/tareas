# Task

The due date is EOD Tuesday, May 28.
The key is to keep it simple, no need to over-think anything. 
The assignment should only take a couple of hours.

## ESG Data Assignment:

Use Python to plot the __climate transition pathway__ of a given company vs its sector benchmarks, as defined by the non-profit research house **Transition Pathway Initiative.**

1. Download the Transition Pathway data from here: https://www.transitionpathwayinitiative.org/sectors. 

Use files `Company_Latest_Assessments` and `Sector_Benchmarks`

2. Identify the columns with __year titles__ and use these to define x-axis, the values in those cells on y-axis. Join the two tables based on Sector

3. Consider how one might filter the choice of benchmarks to relevant subsets. Layer the benchmarks in varying temperature outcomes, different colours below/between/above, as background to company

4. Consider making the tool easier for others to use, more like a dashboard,  less like code/notebook etc. For example, give __drop-down selection boxes__ to choose key values

5. Step 5 is optional if time permits -  write a simple function to discover companies that are **significant outliers** compared to their sector peers, either for good or bad transition plans

* Plotly 
* Streamlit

Thank you and good luck!

Jake

1. 

Create a Python script to draw a chart of performance index per year of a specific company and in the same chart plot the same index of the sector. We have two CSV files, the first CSV is "COMP.CSV" and has the columns: "Sector name", "Scenario name", "2019", "2020" and "2021" columns. The second one "SECTOR.CSV" has the columns "Company Name", "Sector" and "2019", "2020" and "2021".
Company will be specified by name in a variable.
Imange should be stored in "D:\tmp\out.png"
Use Pandas, Plotly.

Create a streamlit dashboard in which I will show a chart created by plotly. The dashboard should have two dropdown input boxes. 
The first input box has a large set of data, it should be filled with a list of 100 items, so it should have search. The seond drop down is much simpler and contains a list of 3 items