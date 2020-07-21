import logging
import psycopg2
from psycopg2 import Error

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

URL = input("Enter DATABASE_URL : ")

try:
    conn = psycopg2.connect(URL)
    cur = conn.cursor()
    sql = "CREATE TABLE users (uid bigint, sudo boolean DEFAULT FALSE);"
    cur.execute(sql)
    conn.commit()
    print("Done !")
except psycopg2.DatabaseError as error :
    LOGGER.error(error)
    exit(1)
finally:
    #closing database connection.
    if(conn):
        cur.close()
        conn.close()