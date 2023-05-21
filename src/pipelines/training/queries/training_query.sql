SELECT pickup_longitude
       , pickup_latitude
       , dropoff_longitude
       , dropoff_latitude
       , passenger_count * 1.0 AS passenger_count
       , CASE WHEN (fare_amount + tolls_amount) <= 15 THEN 1 ELSE 0 END AS fare_le_15

FROM `nyc-tlc.yellow.trips`

WHERE trip_distance > 0
AND fare_amount >= 2.5
AND pickup_longitude > -78
AND pickup_longitude < -70
AND dropoff_longitude > -78
AND dropoff_longitude < -70
AND pickup_latitude > 37
AND pickup_latitude < 45
AND dropoff_latitude > 37
AND dropoff_latitude < 45
AND passenger_count > 0

AND pickup_datetime >= "2022-01-01T00:00:00"
-- AND pickup_datetime <= "2022-12-31T23:59:59"
AND pickup_datetime <= "{{ max_pickup_datetime }}"

LIMIT 10
;