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

4. Consider making the tool easier for others to use, more like a dashboard, less like code/notebook etc. For example, give __drop-down selection boxes__ to choose key values

5. Step 5 is optional if time permits -  write a simple function to discover companies that are **significant outliers** compared to their sector peers.

* Plotly 
* Streamlit
