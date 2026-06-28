CREATE OR REPLACE TABLE stackoverflow.gold.dim_year AS

SELECT DISTINCT
    Year
FROM stackoverflow.silver.person
ORDER BY Year