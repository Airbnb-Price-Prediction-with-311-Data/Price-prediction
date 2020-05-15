CREATE TABLE top_complaints AS
SELECT
  complaint_type,
  count(complaint_type) AS number_occurrances
FROM
  dataset
GROUP BY complaint_type
ORDER BY number_occurrances DESC
LIMIT 20; 