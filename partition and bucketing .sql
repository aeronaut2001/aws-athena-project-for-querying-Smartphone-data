CREATE TABLE partitioned_bucketed_parquet_table
WITH (
    format = 'Parquet',
    write_compression = 'SNAPPY',
    external_location = 's3://smartphone-data/Parquet-partition-bucketed-data/',
    partitioned_by = ARRAY['os'],
    bucketed_by = ARRAY['rating'],
    bucket_count = 30
) AS
SELECT
    "model" AS model,
    "price" AS price,
    "rating" AS rating,
    "sim" AS sim,
    "processor" AS processor,
    "ram" AS ram,
    "battery" AS battery,
    "display" AS display,
    "camera" AS camera,
    "card" AS card,
    "os" AS os
FROM
    "smartphone-database"."parquet_format_data" where os = 'Android v12'
