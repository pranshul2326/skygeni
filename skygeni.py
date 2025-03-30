##this file contains only the answers and questions of the problem. not having any logical code.
from sqlManager.sqlManager import sqlManager

# Example SQL Queries
query1 = "SELECT * FROM finanical_info_table LIMIT 5"  # Fetch first 5 rows
query2 = "SELECT AVG(inflation_rate) FROM finanical_info_table"  # Calculate average inflation rate
query3 = "SELECT start_date, gdp_growth_rate FROM finanical_info_table WHERE gdp_growth_rate > 3.0"  # Filter by GDP growth rate
ques1_query = "SELECT  from client_info_table where industry in ()"

# Execute queries and print results
sqlManager(query1)
