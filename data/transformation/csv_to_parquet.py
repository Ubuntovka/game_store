"""
Transform data from csv to parquet using Spark.
"""
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, StringType, StructType, DoubleType, BooleanType
import pandas as pd


class TransformationFromCSVtoParquet:

    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

        self.__spark = SparkSession.builder.master("local[1]") \
            .appName('FromCSVtoParquet') \
            .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/test/c") \
            .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/test/c") \
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
            .mode("overwrite").save()


a = TransformationFromCSVtoParquet("../appstore_games.csv")
a.read_csv()
a.transformation()
a.load_to_db()
