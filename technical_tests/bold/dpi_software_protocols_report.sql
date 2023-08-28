SELECT protocl, sum(traffic_in), sum(traffic_out)
FROM traffic
GROUP by protocol
HAVING sum(traffic_in), sum(traffic_out)
ORDER BY protocol;