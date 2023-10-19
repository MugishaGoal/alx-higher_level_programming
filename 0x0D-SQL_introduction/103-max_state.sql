-- A script that displays the max temperature of each state
SELECT state, MAX(temperature) AS max_temp
FROM weather
GROUP BY state
ORDER BY state;
