import pymysql
import dotenv
import os

dotenv.load_dotenv()


# MYSQL CONNECTION
def connection():
    "Executes myqsl connection"
    connection = pymysql.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ["MYSQL_DB"],
    )
    return connection
