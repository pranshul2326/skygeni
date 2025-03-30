##this file contains only the answers and questions of the problem. not having any logical code.
from sqlManager.sqlManager import sqlManager


#How many finance lending and blockchain clients does the organization have?
print("Question 1 Result : ")
#Returns the total number of clients in 'Block Chain' or 'Finance Lending' industries
ques1_query = "SELECT count(*) as industry_count from client_info_table where industry in ('Block Chain','Finance Lending')"
sqlManager(ques1_query) 
# answer of query 1 is : 47.
print()


#Which industry in the organization has the highest renewal rate?
print("Question 2 Result : ")
# This query finds the industry with the highest subscription renewal rate by calculating the ratio of renewed subscriptions to total subscriptions for each industry.
# It joins client_info_table with subscription_info_data, groups by industry, then sorts by renewal rate to return only the top performer.
ques2_query = """
WITH IndustryRenewal AS (
    SELECT 
        icd.industry,
        COUNT(si.client_id) AS total_subscriptions,
        SUM(CASE WHEN si.renewed = 'True' THEN 1 ELSE 0 END) AS renewed_count,
        SUM(CASE WHEN si.renewed = 'True' THEN 1 ELSE 0 END) * 1.0 / COUNT(si.client_id) AS renewal_rate
    FROM client_info_table icd
    JOIN subscription_info_data si ON icd.client_id = si.client_id
    GROUP BY icd.industry
)
SELECT industry
FROM IndustryRenewal
ORDER BY renewal_rate DESC
LIMIT 1;
"""
# Execute queries and print results
sqlManager(ques2_query) 
# answer of query 2 is : AI.
print()


print("Question 3 Result : ")
# This query calculates the average inflation rate during periods when subscriptions were renewed.
# It joins subscription_info_data with finanical_info_table where the subscription end date falls within the financial date range.
ques3_query  = """
SELECT AVG(f.inflation_rate) as average_inflation_rate
FROM subscription_info_data s
JOIN finanical_info_table f 
ON s.end_date BETWEEN f.start_date AND f.end_date
WHERE s.renewed = 1
"""
sqlManager(ques3_query)
#output : average_inflation_rate : 4.3118
print()

# This query calculates the median amount paid for each year across all payment methods.
#   It extracts the year from payment_date, then uses ROW_NUMBER() and window functions to identify median positions for each year's payments.
print("Question 4 Result : ")
ques4_query = """
WITH PaymentData AS (
    SELECT 
        CAST(SUBSTR(payment_date, -4, 4) AS INTEGER) AS payment_year, 
        amount_paid,
        ROW_NUMBER() OVER (PARTITION BY CAST(SUBSTR(payment_date, -4, 4) AS INTEGER) ORDER BY amount_paid) AS row_num,
        COUNT(*) OVER (PARTITION BY CAST(SUBSTR(payment_date, -4, 4) AS INTEGER)) AS total_count
    FROM payment_info_table
),
MedianCalc AS (
    SELECT 
        payment_year, 
        amount_paid,
        total_count,
        row_num,
        (total_count + 1) / 2.0 AS median_position
    FROM PaymentData
)
SELECT 
    payment_year,
    AVG(amount_paid) AS median_amount
FROM MedianCalc
WHERE row_num IN (FLOOR(median_position), CEIL(median_position))
GROUP BY payment_year
ORDER BY payment_year;
"""
sqlManager(ques4_query)
#output : 
# payment_year | median_amount
# 2018 | 235.7
# 2019 | 360.9
# 2020 | 284.5
# 2021 | 306.79999999999995
# 2022 | 288.0




