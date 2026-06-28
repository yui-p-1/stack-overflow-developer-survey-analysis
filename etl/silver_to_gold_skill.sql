CREATE OR REPLACE TABLE stackoverflow.gold.skill AS

SELECT
    person.Country,
    person.Country_Region,
    person_skill.Category,
    person_skill.Skill,
    AVG(person.ConvertedCompYearly) AS salary_avg,
    COUNT(DISTINCT person_skill.ResponseId) AS respondent_count,
    person_skill.Year
FROM
    stackoverflow.silver.person_skill
    INNER JOIN stackoverflow.silver.person
        ON person_skill.ResponseId = person.ResponseId
        AND person_skill.Year = person.Year
    INNER JOIN stackoverflow.gold.dim_country as d
        ON person.Country = d.Country
WHERE
    person.Age_Category NOT IN ('Under 18', 'Unknown')
    AND person_skill.ExperienceType IN ('Have', 'Professional')
GROUP BY
    person.Country,
    person.Country_Region,   
    person_skill.Category,
    person_skill.Skill,
    person_skill.Year