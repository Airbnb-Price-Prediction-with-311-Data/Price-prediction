CREATE TABLE top_complaints_zip AS
SELECT
  complaint_type,
  incident_zip,
  count(complaint_type) AS number_occurrances
FROM
  dataset
GROUP BY complaint_type,incident_zip
ORDER BY number_occurrances DESC
; 

DELETE FROM table_name WHERE number_occurrances<100;
