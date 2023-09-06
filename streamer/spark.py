# Import the necessary modules
import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql.functions import from_json,col,from_unixtime
from pyspark.sql.types import StructType,StructField, StringType,FloatType,LongType,TimestampType

from datetime import datetime, date
from pyspark.sql import Row



# Create a SparkSession
spark = SparkSession \
   .builder \
   .appName("Finnhub Producer Spark App") \
   .master("local[*]") \
   .getOrCreate()


df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:29092") \
  .option("subscribe", "stocks") \
  .option('startingOffsets','earliest')\
  .load()




schema = StructType([
    StructField('c',StringType(),True),
    StructField('p',FloatType(),True),
    StructField('s',StringType(),True),
    StructField('t',LongType(),True),
    StructField('v',FloatType(),True)
    
])

trade_df = df.selectExpr('CAST(value as STRING)') \
            .select(from_json(col('value'),schema) \
            .alias('data')) \
            .select('data.*')


stock_df = trade_df.withColumnRenamed('c','Conditions') \
    .withColumnRenamed('p','Price') \
    .withColumnRenamed('s','Symbol') \
    .withColumnRenamed('v','Volume') \
    .withColumn('Timestamp',from_unixtime(col('t')/1000).cast(TimestampType())) \
    .drop('t')


url='jdbc:postgresql://postgresql:5432/postgres'
dbtable='stocks'
user='postgres'
password='password'
driver='org.postgresql.Driver'


def stream_writer(dataframe,batch_id):
 dataframe.write \
   .format('jdbc') \
   .option("url",url) \
   .option("dbtable",dbtable) \
   .option("user",user) \
   .option("password",password) \
   .option('driver',driver) \
   .mode('append') \
   .save()


writer = stock_df.writeStream \
  .outputMode("update") \
  .foreachBatch(stream_writer) \
  .option("truncate", "false") \
  .trigger(processingTime="15 seconds") \
  .start() \
  .awaitTermination()
 

