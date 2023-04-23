import dotenv
from pyspark.sql import SparkSession, DataFrame
from log_handler import logger
from base_exception import TaskFailedError
import db_connect


class SparkClient:
    def __init__(self):
        logger.info("Initializing Spark Session!!!")
        self.spark = SparkSession.builder.master('local[*]'). \
            config('spark.jars.packages', "mysql:mysql-connector-java:8.0.11"). \
            appName("mos-etl").getOrCreate()
        self.spark.sparkContext.setLogLevel('ERROR')
        # self.spark.conf.set('spark.jars.packages', "mysql:mysql-connector-java:8.0.11")
        self.jdbc_properties = None
        dotenv.load_dotenv()
        logger.info("Spark Session is created and is available to use!!!")

    def get_spark(self):
        return self.spark

    def close_session(self):
        try:
            logger.info("Closing the Spark Session:")
            self.spark.stop()
        except e:
            logger.info(f"Not Able to close the spark sesssion due to : {e}")
            raise TaskFailedError("Spark Session is not closed")

    def read_mysql_table_into_dataframe(self, query: str) -> DataFrame:
        self.set_jdbc_connection_properties()
        connection_properties = self.jdbc_properties
        try:
            df = self.spark.read.format('jdbc'). \
                options(
                    url=connection_properties['url'],
                    user=connection_properties['user'],
                    query=query,
                    password=connection_properties['password'],
                    driver=connection_properties['driver']
                ).load()
            return df
        except Exception as ex:
            logger.error(f"Not Able to connect to data base due to {ex}")
            raise ex

    def set_jdbc_connection_properties(self):
        self.jdbc_properties = db_connect.get_mysql_connection_properties()


df = SparkClient().read_mysql_table_into_dataframe("select * from call_agent_mapping")
df.show()
