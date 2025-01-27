-- 1. Make a query to get the result for total distance per route:

SELECT
  r.id AS route_id,
  r.name,
  SUM(rp.distance) AS total_distance
FROM
  routes r
JOIN
  route_points rp ON r.id = rp.route_id
GROUP BY
  r.id, r.name;