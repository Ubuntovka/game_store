"""
Transform data from csv to parquet using Spark.
"""
import os
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructType, DoubleType
import pandas as pd
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

MONGODB_URI = os.environ.get('MONGODB_URI')
SOURCE_GAMES = os.environ.get('SOURCE_GAMES')


class TransformationFromCSVtoParquet:

    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

        self.__spark = SparkSession.builder.master("local[1]") \
            .appName('FromCSVtoParquet') \
            .config("spark.mongodb.write.connection.uri", MONGODB_URI) \
            .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector:10.0.3") \
            .getOrCreate()
        self.__df = None

    def read_csv(self):
        schema = StructType() \
            .add("url", StringType(), True) \
            .add("id", IntegerType(), False) \
            .add("name", StringType(), True) \
            .add("subtitle", StringType(), True) \
            .add("icon_url", StringType(), True) \
            .add("average_user_rating", DoubleType(), True) \
            .add("user_rating_count", DoubleType(), True) \
            .add("price", DoubleType(), True) \
            .add("In-app Purchases", StringType(), True) \
            .add("description", StringType(), True) \
            .add("developer", StringType(), True) \
            .add("age_rating", StringType(), True) \
            .add("languages", StringType(), True) \
            .add("size", DoubleType(), True) \
            .add("primary_genre", StringType(), True) \
            .add("genres", StringType(), True) \
            .add("original_release_date", StringType(), True) \
            .add("current_version_release_date", StringType(), True)

        pandas_df = pd.read_csv(self.csv_file_path)
        self.__df = self.__spark.createDataFrame(pandas_df, schema)

    def transformation(self):
        if self.__df is not None:
            self.__df = self.__df.select("url", "id", "name", "icon_url", "average_user_rating",
                                         "user_rating_count", "price", "description",
                                         "developer", "age_rating", "languages", "size", "primary_genre",
                                         "genres", "original_release_date", "current_version_release_date")

    def load_to_db(self):
        self.__df.write \
            .format("mongodb") \
            .option('database', "Game") \
            .option('collection', "Game") \
            .mode("append") \
            .save()


a = TransformationFromCSVtoParquet(SOURCE_GAMES)
a.read_csv()
a.transformation()
a.load_to_db()
