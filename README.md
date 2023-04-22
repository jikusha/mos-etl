# mos-etl
End to end flow for extracting data from a source database to another destination after doing transformations

Idea is to divide the entire process into 3 stages.

1. Extract data from mysql source database to kafka using pyspark as the processing engine, then will move the data from kafka to s3.

2. Then will extract the data from S3 to Databricks Delta table using Pyspark in Databricks.

3. Move the data from Delta table to PostgreSQL Data base using Pyspark.
