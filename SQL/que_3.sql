-- 3. Make a query for result by station_id and slot

SELECT
  t.station_id,
  s.name AS station_name,
  t.slot,
  t.time
FROM
  times t
JOIN
  station s ON s.id = t.station_id
WHERE
  t.station_id = 1
  AND t.slot = 1;