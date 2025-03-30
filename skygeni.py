##this file contains only the answers and questions of the problem. not having any logical code.
from sqlManager.sqlManager import sqlManager


#How many finance lending and blockchain clients does the organization have?
print("Question 1 Result : ")
ques1_query = "SELECT count(*) as industry_count from client_info_table where industry in ('Block Chain','Finance Lending')"
sqlManager(ques1_query) # answer of query 1 is = 47.



#Which industry in the organization has the highest renewal rate?
print("Question 2 Result : ")
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
sqlManager(ques2_query) # answer of query 2 is = AI.


print("Question 3 Result : ")
ques3_query = """
WITH renewed_subscriptions AS (
    SELECT client_id, DATE(start_date) AS renewal_date
    FROM subscription_info_data
    WHERE renewed = 'TRUE'
)
SELECT AVG(f.inflation_rate) AS avg_inflation_rate
FROM renewed_subscriptions r
JOIN finanical_info_table f
ON r.renewal_date >= DATE(f.start_date) 
AND r.renewal_date <= DATE(f.end_date);
"""
sqlManager(ques3_query)


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
['payment_year', 'median_amount']
# output : [(2018, 235.7), (2019, 360.9), (2020, 284.5), (2021, 306.79999999999995), (2022, 288.0)]





