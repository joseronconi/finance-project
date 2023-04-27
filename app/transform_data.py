from pyspark.sql import SparkSession
import lib_aws as aws

# Upload data to s3
bucket_name = 'project-finance-api'
file_name = 'all_results_fundamentus.csv'

# Create Spark Session
spark = SparkSession.builder.appName('Fundamentus').getOrCreate()

s3.Object(bucket_name, file_name).upload_file('all_results.csv')