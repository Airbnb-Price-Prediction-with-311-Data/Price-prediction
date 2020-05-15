CREATE TABLE least_common_complaints AS
SELECT
  complaint_type,
  count(complaint_type) AS number_occurrances,
  avg(latitude) AS avg_lat,
  avg(longitude) AS avg_lon
FROM
  dataset
GROUP BY complaint_type
ORDER BY number_occurrances ASC
LIMIT 20;