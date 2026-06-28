CREATE OR REPLACE TABLE stackoverflow.gold.country AS

SELECT
    p.Country,
    p.Country_Region,
    p.Age_Category,
    p.DevType_Category,
    p.Industry_Category,
    AVG(p.ConvertedCompYearly) AS salary_avg,
    COUNT(*) AS respondent_count,
    d.country_respondent_count,
    p.Year
FROM
    stackoverflow.silver.person AS p
    INNER JOIN stackoverflow.gold.dim_country AS d
        ON p.Country = d.Country
WHERE p.Age_Category NOT IN ('Under 18', 'Unknown')
GROUP BY
    p.Country,
    p.Country_Region,
    p.Age_Category,    
    p.DevType_Category,
    p.Industry_Category,
    d.country_respondent_count,
    p.Year
ORDER BY
    p.Year,
    p.Country