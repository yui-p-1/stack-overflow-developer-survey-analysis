CREATE OR REPLACE TABLE stackoverflow.gold.dim_country AS

SELECT
    Country,
    MAX(Country_Region) AS Country_Region,
    COUNT(*) AS country_respondent_count
FROM
    stackoverflow.silver.person
WHERE
    Country IS NOT NULL
    AND Age_Category NOT IN ('Under 18', 'Unknown')
GROUP BY
    Country
HAVING
    COUNT(*) >= 5000