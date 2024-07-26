-- 2. Make a query for get result for same route by stop id for source and destination

SELECT
  rp.route_id,
  rp1.stop_id AS source_stop_id,
  rp2.stop_id AS dest_stop_id
FROM
  route_points rp
JOIN
  route_points rp1 ON rp1.route_id = rp.route_id AND rp1.order = 1
JOIN
  route_points rp2 ON rp2.route_id = rp.route_id AND rp2.order = 2;