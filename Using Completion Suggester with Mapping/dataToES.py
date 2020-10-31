import findspark
import requests
from pprint import pprint
import time
from ES_Config import es, mapping, index

findspark.init("/usr/local/spark/")
from pyspark.sql import SparkSession, functions as func


class SparkESTask(object):
    @staticmethod
    def connection():
        try:
            res = requests.get('http://localhost:9200')
            pprint(res.content)
        except:
            print("Connection failed! Check if Elasticsearch process has been started.")
            exit(1)

    def spark_df_to_es(self, file, name):
        try:
            self.df = spark.read.csv(filepath, sep=r'\t', header=True)
            self.df = self.df.select(func.col("primaryTitle").alias("movies"))
            self.df.coalesce(1).write.format("csv").mode('overwrite').save("movies_clean_dataset", header='true')

            time.sleep(5)

            self.new_df = spark.read.csv("movies_clean_dataset/*.csv", header=True)

            time.sleep(5)

            print("Creating Elasticsearch Index Mapping...")
            time.sleep(1)

            es.indices.create(index=name, body=mapping)
            time.sleep(1)

            print("Successfully mapped index...")
            time.sleep(1)

            print("Sending data to Elasticsearch by PySpark...")
            time.sleep(1)

            self.new_df.write.format(
                "org.elasticsearch.spark.sql"
            ).option(
                "es.resource", '%s' % (name)
            ).option(
                "es.nodes", 'localhost'
            ).option(
                "es.port", '9200'
            ).save()

            print("Successfully ingested data into Elasticsearch!")
            time.sleep(1)

            print("\nTotal number of records:")
            count = es.count(index=name)
            pprint(count)
        except:
            print("Something went wrong in sparkDF()!")

    @staticmethod
    def delete_index(name):
        try:
            es.indices.delete(index=name)
            print(f"{index_name} index deleted successfully!")
        except:
            print(f"Error deleting {name} index")

    def run(self):
        running = True
        try:
            while running:
                print("-----------------------------------------")
                print("1.Add data to ES\n"
                      "2.Delete index\n"
                      "E.TO EXIT")
                print("-----------------------------------------")
                mode = input("Enter your choice: ")

                if mode == "1":
                    self.spark_df_to_es(filepath, index_name)
                elif mode == "2":
                    self.delete_index(index_name)
                elif mode.upper() == "E":
                    break
                else:
                    print("Invalid input! Try Again!")
        except:
            print("Something went wrong in run()!")


if __name__ == "__main__":
    filepath = "/home/ubuntu/title.basics.tsv"
    start = SparkESTask()
    start.connection()
    # ### Entering index name
    index_name = index
    # ### Creating Spark Session
    spark = SparkSession.builder.appName('task').getOrCreate()
    print("SparkSession Started Successfully!")
    start.run()
    # ### Stopping the SparkSession
    es.transport.close()
    print("Closed connection to Elasticsearch!")
    spark.stop()
    print("SparkSession Stopped Successfully!")
