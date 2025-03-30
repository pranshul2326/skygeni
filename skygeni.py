##this file contains only the answers and questions of the problem. not having any logical code.
from sqlManager.sqlManager import sqlManager

# Example SQL Queries
query1 = "SELECT * FROM finance_data LIMIT 5"  # Fetch first 5 rows
query2 = "SELECT AVG(inflation_rate) FROM finance_data"  # Calculate average inflation rate
query3 = "SELECT start_date, gdp_growth_rate FROM finance_data WHERE gdp_growth_rate > 3.0"  # Filter by GDP growth rate

# Execute queries and print results
sqlManager(query3)
