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

        self.__spark = SparkSession.builder \
            .appName('FromCSVtoParquet') \
            .config("spark.executor.memory", "1g") \
            .config("spark.mongodb.write.connection.uri", MONGODB_URI) \
            .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector:10.0.3") \
            .getOrCreate()
        self.__df = None

    def read_csv(self):
        schema = StructType() \
            .add("URL", StringType(), True) \
            .add("ID", IntegerType(), False) \
            .add("Name", StringType(), True) \
            .add("Subtitle", StringType(), True) \
            .add("Icon URL", StringType(), True) \
            .add("Average User Rating", DoubleType(), True) \
            .add("User Rating Count", DoubleType(), True) \
            .add("Price", DoubleType(), True) \
            .add("In-app Purchases", StringType(), True) \
            .add("Description", StringType(), True) \
            .add("Developer", StringType(), True) \
            .add("Age Rating", StringType(), True) \
            .add("Languages", StringType(), True) \
            .add("Size", DoubleType(), True) \
            .add("Primary Genre", StringType(), True) \
            .add("Genres", StringType(), True) \
            .add("Original Release Date", StringType(), True) \
            .add("Current Version Release Date", StringType(), True)
        # df = self.__spark.read.options(header='True').schema(schema).csv(self.csv_file_path)

        pandas_df = pd.read_csv(self.csv_file_path)
        self.__df = self.__spark.createDataFrame(pandas_df, schema)
        # self.__df.printSchema()

    def transformation(self):
        if self.__df is not None:
            self.__df.select("URL", "ID", "Name", "Icon URL", "Average User Rating",
                             "User Rating Count", "Price", "Description",
                             "Developer", "Age Rating", "Languages", "Size", "Primary Genre",
                             "Genres", "Original Release Date", "Current Version Release Date")
            # self.__df.show(truncate=False)

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
